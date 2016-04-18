import pandas                  as pd
import numpy                   as np
import statsmodels.api         as sm
import statsmodels.formula.api as smf

from patsy import dmatrices

df = pd.read_csv("https://raw.githubusercontent.com/Thinkful-Ed/curric-data-001-data-sets/master/loans/loansData.csv")

df['home_ownership'] = df['Home.Ownership']
df['int_rate'] = df['Interest.Rate'].map(lambda val: float(val[:-1]))
df['annual_inc'] = df['Monthly.Income']*12

print('\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> int_rate ~ annual_inc >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')
est1 = smf.ols(formula='int_rate ~ annual_inc', data=df).fit()
print(est1.summary())

print('\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> int_rate ~ annual_inc + home_ownership >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')
est2 = smf.ols(formula='int_rate ~ annual_inc + home_ownership', data=df).fit()
print(est2.summary())

print('\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> int_rate ~ annual_inc * home_ownership >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')
est3 = smf.ols(formula='int_rate ~ annual_inc * home_ownership', data=df).fit()
print(est3.summary())
