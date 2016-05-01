import csv
import sqlite3 as lite

con = lite.connect('life_exp.db')

insert = "UPDATE educational_life_expectancies SET gdp = ? WHERE country = ? AND year = ?"

def main():
    with con:
        cur = con.cursor()
        with open('GDP.csv') as f:
            for i in range(5): next(f)
            csvReader = csv.reader(f)
            for line in csvReader:
                for year in range(1999, 2011):
                    cur.execute(insert, (line[year - 1956], line[0], year))

if __name__ == "__main__":
    main()
