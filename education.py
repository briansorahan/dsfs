import numpy   as np
import pandas  as pd
import sqlite3 as lite

con = lite.connect('life_exp.db')
sel = "SELECT * FROM educational_life_expectancies ORDER BY year"

def main():
    with con:
        cur     = con.cursor()
        columns = ['country', 'total', 'male_life_expectancy', 'female_life_expectancy', 'year']
        cur.execute(sel)
        df = pd.DataFrame(cur.fetchall(), columns=columns)
        print('median male SLE is {}'.format(df['male_life_expectancy'].median()))
        print('mean male SLE is {}'.format(df['male_life_expectancy'].mean()))
        print('median female SLE is {}'.format(df['female_life_expectancy'].median()))
        print('mean female SLE is {}'.format(df['female_life_expectancy'].mean()))

if __name__ == "__main__":
    main()
