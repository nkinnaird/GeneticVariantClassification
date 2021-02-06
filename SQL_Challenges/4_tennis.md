# Part 4: Tennis Data

*Intermediate - Advanced level SQL*

---

## Setup

We'll be using tennis data from [here](https://archive.ics.uci.edu/ml/datasets/Tennis+Major+Tournament+Match+Statistics).

Navigate to your preferred working directory, and download the data.

```bash
curl -L -o tennis.zip http://archive.ics.uci.edu/ml/machine-learning-databases/00300/Tennis-Major-Tournaments-Match-Statistics.zip
unzip tennis.zip -d tennis
```

Make sure you have Postgres installed and initialized

```bash
brew install postgresql
brew services start postgres
```

Install SQLAlchemy if you haven't already

```
conda install -c anaconda sqlalchemy
```

Start Postgres in your terminal with the command `psql`. Then, create a `tennis` database using the `CREATE DATABASE` command.

```
psql

<you_user_name>=# CREATE DATABASE TENNIS;
CREATE DATABASE
<you_user_name>=# \q
```

Pick a table from the *tennis* folder, and upload it to the database using SQLAlchemy and Pandas.

```python
from sqlalchemy import create_engine
import pandas as pd


engine = create_engine('postgresql://<your_user_name>:localhost@localhost:5432/tennis')

aus_men = pd.read_csv('./tennis/AusOpen-men-2013.csv')

# I'm choosing to name this table "aus_men"
aus_men.to_sql('aus_men', engine, index=False)
```

*Note: In the place of `<your_user_name>` you should have your computer user name ...*

Check that you can access the table

```python
query = 'SELECT * FROM aus_men;'
df = pd.read_sql(query, engine)

df.head()
```

Do the same for the other CSV files in the *tennis* directory.

---

## The challenges!

This challenge uses only SQL queries. Please submit answers in a markdown file.

1. Using the same tennis data, find the number of matches played by
   each player in each tournament. (Remember that a player can be
   present as both player1 or player2).

```
query = '''

WITH all_data AS 
(

(SELECT "Player1" as player, COUNT("Player1") as num_matches
FROM aus_men
GROUP BY "Player1")

UNION

(SELECT "Player2" as p2_aus_men, COUNT("Player2") as NumPlayer2Matches
FROM aus_men
GROUP BY "Player2")

UNION

(SELECT "Player1" as p1_aus_women, COUNT("Player1") as NumPlayer1Matches
FROM aus_women
GROUP BY "Player1")

UNION

(SELECT "Player2" as p2_aus_women, COUNT("Player2") as NumPlayer2Matches
FROM aus_women
GROUP BY "Player2")

UNION

(SELECT "Player1" as p1_french_men, COUNT("Player1") as NumPlayer1Matches
FROM french_men
GROUP BY "Player1")

UNION

(SELECT "Player2" as p2_french_men, COUNT("Player2") as NumPlayer2Matches
FROM french_men
GROUP BY "Player2")

UNION

(SELECT "Player1" as p1_french_women, COUNT("Player1") as NumPlayer1Matches
FROM french_women
GROUP BY "Player1")

UNION

(SELECT "Player2" as p2_french_women, COUNT("Player2") as NumPlayer2Matches
FROM french_women
GROUP BY "Player2")

UNION

(SELECT "Player1" as p1_us_men, COUNT("Player1") as NumPlayer1Matches
FROM us_men
GROUP BY "Player1")

UNION

(SELECT "Player2" as p2_us_men, COUNT("Player2") as NumPlayer2Matches
FROM us_men
GROUP BY "Player2")

UNION

(SELECT "Player 1" as p1_us_women, COUNT("Player 1") as NumPlayer1Matches
FROM us_women
GROUP BY "Player 1")

UNION

(SELECT "Player 2" as p2_us_women, COUNT("Player 2") as NumPlayer2Matches
FROM us_women
GROUP BY "Player 2")

UNION

(SELECT "Player1" as p1_wimbledon_men, COUNT("Player1") as NumPlayer1Matches
FROM wimbledon_men
GROUP BY "Player1")

UNION

(SELECT "Player2" as p2_wimbledon_men, COUNT("Player2") as NumPlayer2Matches
FROM wimbledon_men
GROUP BY "Player2")

UNION

(SELECT "Player1" as p1_wimbledon_women, COUNT("Player1") as NumPlayer1Matches
FROM wimbledon_women
GROUP BY "Player1")

UNION

(SELECT "Player2" as p2_wimbledon_women, COUNT("Player2") as NumPlayer2Matches
FROM wimbledon_women
GROUP BY "Player2")

)


SELECT "player", SUM(num_matches) as total_matches
FROM all_data
GROUP BY "player"
ORDER BY total_matches DESC

;'''


df = pd.read_sql(query, engine)
df.head()
```


| player | total_matches |
| -- | -- |
| Roger Federer |	15.0 |
| Rafael Nadal |	14.0 |
| Richard Gasquet |	13.0 |
| David Ferrer |	12.0 |
| Maria Sharapova |	11.0 |


**I'm not sure if I've misunderstood the question or not, or whether there is a better way to re-write the extremely long query above. I'm just going to go with it instead of keep bashing my head against a wall trying to figure it out. The same goes for below as well.** 


2. Who has played the most matches total in all of US Open, AUST Open, 
   French Open? Answer this both for men and women.

```
query = '''

WITH all_data AS 
(

(SELECT "Player1" as player, COUNT("Player1") as num_matches
FROM aus_men
GROUP BY "Player1")

UNION

(SELECT "Player2" as p2_aus_men, COUNT("Player2") as NumPlayer2Matches
FROM aus_men
GROUP BY "Player2")

UNION

(SELECT "Player1" as p1_french_men, COUNT("Player1") as NumPlayer1Matches
FROM french_men
GROUP BY "Player1")

UNION

(SELECT "Player2" as p2_french_men, COUNT("Player2") as NumPlayer2Matches
FROM french_men
GROUP BY "Player2")

UNION

(SELECT "Player1" as p1_us_men, COUNT("Player1") as NumPlayer1Matches
FROM us_men
GROUP BY "Player1")

UNION

(SELECT "Player2" as p2_us_men, COUNT("Player2") as NumPlayer2Matches
FROM us_men
GROUP BY "Player2")

)


SELECT "player", SUM(num_matches) as total_matches
FROM all_data
GROUP BY "player"
ORDER BY total_matches DESC

;'''


df = pd.read_sql(query, engine)
print(df.head())


query = '''

WITH all_data AS 
(


(SELECT "Player1" as player, COUNT("Player1") as num_matches
FROM aus_women
GROUP BY "Player1")

UNION

(SELECT "Player2" as p2_aus_women, COUNT("Player2") as NumPlayer2Matches
FROM aus_women
GROUP BY "Player2")

UNION

(SELECT "Player1" as p1_french_women, COUNT("Player1") as NumPlayer1Matches
FROM french_women
GROUP BY "Player1")

UNION

(SELECT "Player2" as p2_french_women, COUNT("Player2") as NumPlayer2Matches
FROM french_women
GROUP BY "Player2")

UNION

(SELECT "Player 1" as p1_us_women, COUNT("Player 1") as NumPlayer1Matches
FROM us_women
GROUP BY "Player 1")

UNION

(SELECT "Player 2" as p2_us_women, COUNT("Player 2") as NumPlayer2Matches
FROM us_women
GROUP BY "Player 2")

)


SELECT "player", SUM(num_matches) as total_matches
FROM all_data
GROUP BY "player"
ORDER BY total_matches DESC

;'''


df = pd.read_sql(query, engine)
print(df.head())
```

**Roger Federer: 15**

**Serena Williams and Maria Sharapova: 11**



3. Who has the highest first serve percentage? (Just the maximum value
   in a single match.)


```
query = '''

WITH all_data AS (
                SELECT  * FROM aus_men
                UNION ALL
                SELECT  * FROM aus_women
                UNION ALL
                SELECT  * FROM french_men  
                UNION ALL
                SELECT  * FROM french_women  
                UNION ALL
                SELECT  * FROM us_men  
                UNION ALL
                SELECT  * FROM us_women  
                UNION ALL
                SELECT  * FROM wimbledon_men  
                UNION ALL
                SELECT  * FROM wimbledon_women  
)
SELECT "Player1", "Player2", "FSP.1", "FSP.2" 
FROM all_data
ORDER BY  "FSP.2" DESC
;'''

        
df = pd.read_sql(query, engine)
df.info()
df.head()  
```

**Sara Errani**


4. What are the unforced error percentages of the top three players
   with the most wins? (Unforced error percentage is % of points lost
   due to unforced errors. In a match, you have fields for number of
   points won by each player, and number of unforced errors for each
   field.)

```
query = '''

WITH all_data AS (
                SELECT  * FROM aus_men
                UNION ALL
                SELECT  * FROM aus_women
                UNION ALL
                SELECT  * FROM french_men  
                UNION ALL
                SELECT  * FROM french_women  
                UNION ALL
                SELECT  * FROM us_men  
                UNION ALL
                SELECT  * FROM us_women  
                UNION ALL
                SELECT  * FROM wimbledon_men  
                UNION ALL
                SELECT  * FROM wimbledon_women  
)
SELECT "Player1", "Player2", "TPW.1", "UFE.1", "TPW.2", "UFE.2", "UFE.1"/"TPW.2" as p1_unf_err_per, "UFE.2"/"TPW.1" as p2_unf_err_per 
FROM all_data
WHERE "TPW.1" is not null AND "TPW.2" is not null AND "UFE.1" is not null AND "UFE.2" is not null
ORDER BY "TPW.2" DESC 
;'''

df = pd.read_sql(query, engine)
df.head(20)
```

| player | Unforced Error Percentage |
| -- | -- |
| Daniel Brands |	0.352174 |
| Gilles Simon |	0.229437 |
| Tommy Haas |	0.201878 |


**Again I find the question very confusing. I'm just going to roll with the answer that I've got, but if I need to go back and work through it again to get it right please let me know.**


*Hint:* `SUM(double_faults)` sums the contents of an entire column. For each row, to add the field values from two columns, the syntax `SELECT name, double_faults + unforced_errors` can be used.


*Special bonus hint:* To be careful about handling possible ties, consider using [rank functions](http://www.sql-tutorial.ru/en/book_rank_dense_rank_functions.html).




