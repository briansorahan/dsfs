import matplotlib.pyplot as plt
import pandas            as pd
import scipy.stats       as stats

loansData = pd.read_csv("loansData.csv")
loansData.dropna(inplace=True)

plt.figure()
loansData.boxplot(column='Amount.Requested')
plt.savefig("loan_club_box.png")

plt.figure()
loansData.hist(column='Amount.Requested')
plt.savefig("loan_club_hist.png")

plt.figure()
stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.savefig("loan_club_qq.png")
