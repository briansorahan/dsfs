import math
import matplotlib.pyplot as plt
import numpy             as np
import pandas            as pd
import statsmodels.api   as sm

def aboveTwelvePercent(interestRate):
    ir = float(interestRate[:-1]) / 100
    return 1 if ir >= 0.12 else 0

df = pd.read_csv("loansDataClean.csv")

df["IR_TF"] = map(aboveTwelvePercent, df["Interest.Rate"])

# print(loansData["Interest.Rate"])
# print(loansData["IR_TF"])

# The independent variables shaped as columns
fico = df['FICO.Score']
loanamt = df['Amount.Requested']
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

df["Intercept"] = 1.0

ind_vars = ["Intercept", "FICO.Score", "Amount.Requested"]

logit  = sm.Logit(df['IR_TF'], df[ind_vars])
result = logit.fit()

def logistic_function(coeffs, ficoScore, loanAmt):
    lin = -coeffs["Intercept"] - (coeffs["FICO.Score"] * ficoScore) - (coeffs["Amount.Requested"] * loanAmt)
    return 1.0 / (1.0 + math.exp(lin))

print(logistic_function(result.params, 720, 10000))
