from patsy import dmatrices

import math
import numpy                   as np
import pandas                  as pd
import sqlite3                 as lite
import statsmodels.formula.api as smf

con = lite.connect('life_exp.db')
sel = "SELECT male_life_expectancy, female_life_expectancy, gdp FROM educational_life_expectancies WHERE gdp IS NOT NULL AND gdp != ''"

def main():
    with con:
        cur = con.cursor()
        cur.execute(sel)
        df = pd.DataFrame(cur.fetchall(), columns=['male_life_expectancy', 'female_life_expectancy', 'gdp'])
        df['log_gdp'] = df['gdp'].map(lambda x: math.log(float(x)))

        # estMale = smf.ols(formula='male_life_expectancy ~ gdp', data=df).fit()
        # print(estMale.summary())
        # estFemale = smf.ols(formula='female_life_expectancy ~ gdp', data=df).fit()
        # print(estFemale.summary())

        estMale = smf.ols(formula='male_life_expectancy ~ log_gdp', data=df).fit()
        print(estMale.summary())
        estFemale = smf.ols(formula='female_life_expectancy ~ log_gdp', data=df).fit()
        print(estFemale.summary())

if __name__ == "__main__":
    main()
