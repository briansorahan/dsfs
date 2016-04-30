import requests
import sqlite3  as lite

from bs4 import BeautifulSoup

con  = lite.connect('life_exp.db')
url  = "http://web.archive.org/web/20110514112442/http://unstats.un.org/unsd/demographic/products/socind/education.htm"
r    = requests.get(url)
soup = BeautifulSoup(r.content, "lxml")

dropTable = "DROP TABLE IF EXISTS educational_life_expectancies"

createTable = """
CREATE TABLE educational_life_expectancies (
    country                TEXT,
    total                  INT,
    male_life_expectancy   INT,
    female_life_expectancy INT,
    year                   INT
)
"""

insert = """
INSERT INTO educational_life_expectancies (
    country,
    total,
    male_life_expectancy,
    female_life_expectancy,
    year
) VALUES (?,?,?,?,?)
"""

def storeRow(cur, tr):
    tds     = tr.find_all('td')
    country = list(tds[0].children)[0]
    year    = list(tds[1].children)[0]
    total   = list(tds[4].children)[0]
    men     = list(tds[7].children)[0]
    women   = list(tds[10].children)[0]
    if country is None:
        raise Exception('country is None')
    if year is None:
        raise Exception('year is None')
    if total is None:
        raise Exception('total is None')
    if men is None:
        raise Exception('men is None')
    if women is None:
        raise Exception('women is None')
    cur.execute(insert, (country, total, men, women, year))

def main():
    with con:
        cur = con.cursor()
        cur.execute(dropTable)
        cur.execute(createTable)
        trs = soup('table')[9].find_all('tr', class_='tcont')
        for tr in trs:
            storeRow(cur, tr)

if __name__ == "__main__":
    main()
