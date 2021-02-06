# Part 3: Soccer Data

*Introductory - Intermediate level SQL*

---

## Setup

Download the [SQLite database](https://www.kaggle.com/hugomathien/soccer/download). *Note: You may be asked to log in, or "continue and download".* Unpack the ZIP file into your working directory (i.e., wherever you'd like to complete this challenge set). There should be a *database.sqlite* file.

As with Part II, you can check the schema:

```python
import pandas as pd
import sqlite3

conn = sqlite3.connect('database.sqlite')

query = "SELECT * FROM sqlite_master"

df_schema = pd.read_sql_query(query, conn)

df_schema.tbl_name.unique()
```

---

Please complete this exercise using sqlite3 (the soccer data, above) and your Jupyter notebook.

1. Which team scored the most points when playing at home?  

```
query = """
SELECT SUM(home_team_goal), team_long_name
FROM Match
JOIN Team
    ON Match.home_team_api_id = Team.team_api_id
GROUP BY team_long_name
ORDER BY SUM(home_team_goal) DESC
;"""

df_schema = pd.read_sql_query(query, conn)
df_schema
```

**Real Madrid CF - 505 goals**


2. Did this team also score the most points when playing away?  

```
query = """
SELECT SUM(away_team_goal), team_long_name
FROM Match
JOIN Team
    ON Match.away_team_api_id = Team.team_api_id
GROUP BY team_long_name
ORDER BY SUM(away_team_goal) DESC
;"""

df_schema = pd.read_sql_query(query, conn)
df_schema
```

**No - FC Barcelona - 354 goals**


3. How many matches resulted in a tie?  

```
query = """
SELECT COUNT(DISTINCT id)
FROM Match
WHERE home_team_goal = away_team_goal
;"""

df_schema = pd.read_sql_query(query, conn)
df_schema
```

**6596**


4. How many players have Smith for their last name? How many have 'smith' anywhere in their name?

```
query = """
SELECT COUNT(player_name)
FROM Player
WHERE player_name LIKE "% smith"
;"""

df_schema = pd.read_sql_query(query, conn)
df_schema

query = """
SELECT COUNT(player_name)
FROM Player
WHERE player_name LIKE "%smith"
;"""

df_schema = pd.read_sql_query(query, conn)
df_schema
```

**Last name: 15, Anywhere in name: 18**


5. What was the median tie score? Use the value determined in the previous question for the number of tie games. *Hint:* PostgreSQL does not have a median function. Instead, think about the steps required to calculate a median and use the [`WITH`](https://www.postgresql.org/docs/8.4/static/queries-with.html) command to store stepwise results as a table and then operate on these results. 

```
query = """
WITH tie_results AS (
    SELECT home_team_goal, away_team_goal
    FROM Match
    WHERE home_team_goal = away_team_goal
    ORDER BY home_team_goal
    )
SELECT home_team_goal, away_team_goal
FROM tie_results
LIMIT 1
OFFSET (6596/2)
;"""

df_schema = pd.read_sql_query(query, conn)
df_schema
```

**Median score: 1 - 1**

6. What percentage of players prefer their left or right foot? *Hint:* Calculate either the right or left foot, whichever is easier based on how you setup the problem.

```
query = """
WITH right_foot AS (
    SELECT COUNT(DISTINCT player_api_id) as num_right, preferred_foot 
    FROM Player_Attributes
    WHERE preferred_foot = "right"
    ),
left_foot AS (
    SELECT COUNT(DISTINCT player_api_id) as num_left, preferred_foot 
    FROM Player_Attributes
    WHERE preferred_foot = "left"
    )
SELECT num_left, num_right, (1.0 * num_left/(num_left+num_right)) AS percent_left, (1.0 *  num_right/(num_left+num_right)) AS percent_right
FROM left_foot
JOIN right_foot
;"""

df_schema = pd.read_sql_query(query, conn)
df_schema
```

**Left: 26.3%, Right: 73.7%**
