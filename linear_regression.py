import pandas            as pd
import numpy             as np
import statsmodels.api   as sm

def getFicoRange(s):
    return int(s.split("-")[0])

def getInterestRate(s):
    return float(s[:-1])

loansData = pd.read_csv("loansData.csv")
loansData["FICO.Score"] = map(getFicoRange, loansData["FICO.Range"])

intrate = map(getInterestRate, loansData['Interest.Rate'])
fico = loansData['FICO.Score']
loanamt = loansData['Amount.Requested']

# The dependent variable
y = np.matrix(intrate).transpose()
# The independent variables shaped as columns
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

# print("y", y)
# print("x1", x1)
# print("x2", x2)

x = np.column_stack([x1, x2])

# print("x", x)

X = sm.add_constant(x)

# print("X", X)

loansData.to_csv('loansData_clean.csv', header=True, index=False)

sm.OLS(y, X).fit().summary()
