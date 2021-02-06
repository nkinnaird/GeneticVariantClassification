# Part 2: Baseball Data

*Introductory - Intermediate level SQL*

---

## Setup

`cd` into the directory you'd like to use for this challenge. Then, download the Lahman SQL Lite dataset

```
curl -L -o lahman.sqlite https://github.com/WebucatorTraining/lahman-baseball-mysql/raw/master/lahmansbaseballdb.sqlite
```

*The `-L` follows redirects, and the `-o` uses the filename instead of outputting to the terminal.*

Make sure sqlite3 is installed

```
conda install -c anaconda sqlite
```

In your notebook, check out the schema

```python
import pandas as pd
import sqlite3

conn = sqlite3.connect('lahman.sqlite')

query = "SELECT * FROM sqlite_master;"

df_schema = pd.read_sql_query(query, conn)

df_schema.tbl_name.unique()
```

---

Please complete this exercise using SQL Lite (i.e., the Lahman baseball data, above) and your Jupyter notebook.

1. What was the total spent on salaries by each team, each year?

```
query = \
"SELECT yearID, teamID, SUM(salary) as team_salary \
FROM salaries \
GROUP BY yearID, teamID;"

df_schema = pd.read_sql_query(query, conn)
df_schema.head(5)
```

**ATL - 1985 - 14807000.0**
**and so on**

2. What is the first and last year played for each player? *Hint:* Create a new table from 'Fielding.csv'.

```
query = \
"SELECT playerID, yearID \
FROM fielding \
;"

df_schema = pd.read_sql_query(query, conn)
df_schema.to_sql("player_years", conn, if_exists="replace")
df_schema.head(10)


query = \
"SELECT playerID, MIN(yearID) as first_year, MAX(yearID) as last_year \
FROM player_years \
GROUP BY playerID \
;"

df_schema = pd.read_sql_query(query, conn)
df_schema.head(10)
```

**aardsda01 - 2004 - 2015**
**and so on**

3. Who has played the most all star games?

```
query = \
"SELECT playerID, COUNT(yearID) as num_appearances \
FROM allstarfull \
GROUP BY playerID \
;"

df_schema = pd.read_sql_query(query, conn)
df_schema.head(5)
```

**aaronha01**

4. Which school has generated the most distinct players? *Hint:* Create new table from 'CollegePlaying.csv'.

```
query = """
WITH college_players AS (
    SELECT playerID, schoolID FROM collegeplaying )
SELECT COUNT(DISTINCT(playerID)) as num_players, schoolID FROM college_players
GROUP BY schoolID
ORDER BY COUNT(DISTINCT(playerID)) DESC
;"""

df_schema = pd.read_sql_query(query, conn)
df_schema
```

**Texas - 107**

5. Which players have the longest career? Assume that the `debut` and `finalGame` columns comprise the start and end, respectively, of a player's career. *Hint:* Create a new table from 'Master.csv'. Also note that strings can be converted to dates using the [`DATE`](https://wiki.postgresql.org/wiki/Working_with_Dates_and_Times_in_PostgreSQL#WORKING_with_DATETIME.2C_DATE.2C_and_INTERVAL_VALUES) function and can then be subtracted from each other yielding their difference in days.

```
query = """
WITH player_timeline AS (
    SELECT playerID, DATE(debut) as debutDate, DATE(finalGame) as finalDate FROM people )
SELECT playerID, finalDate-debutDate as dateDiff FROM player_timeline
ORDER BY dateDiff DESC
;"""

df_schema = pd.read_sql_query(query, conn)
df_schema
```

**altroni01 - 35 years**
**orourji01 - 32 years**
**and so on**

6. What is the distribution of debut months? *Hint:* Look at the `DATE` and [`EXTRACT`](https://www.postgresql.org/docs/current/static/functions-datetime.html#FUNCTIONS-DATETIME-EXTRACT) functions.

```
query = """
WITH dates_table AS (
    SELECT DATE(debut) as debutDate
    FROM people)
SELECT COUNT(strftime('%m', debutDate)) as month_count FROM dates_table
GROUP BY strftime('%m', debutDate)
;"""

df_schema = pd.read_sql_query(query, conn)
df_schema
```

| Month | Month Count |
| -- | -- |
| 03 | 92 |
| 04 | 4998 |
| 05 | 2457 |
| 06 | 2155 |
| 07 | 2156 |
| 08 | 2180 |
| 09 | 5336 |
| 10 | 308 |


**Note: I tried for ages to get EXTRACT and other methods working and couldn't for the life of me figure it out. Not sure if I just couldn't get it, or if sqlite has a different implementation than I was finding online.**

7. What is the effect of table join order on mean salary for the players listed in the main (master) table? *Hint:* Perform two different queries, one that joins on playerID in the salary table and other that joins on the same column in the master table. You will have to use left joins for each since right joins are not currently supported with SQLalchemy.
