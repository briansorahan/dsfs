import collections

import matplotlib.pyplot as plt
import pandas            as pd

from scipy import stats

# Load the reduced version of the Lending Club Dataset
loansData = pd.read_csv("loansData.csv")
# Drop null rows
loansData.dropna(inplace=True)

freq = collections.Counter(loansData['Open.CREDIT.Lines'])
# print(freq)
chi, p = stats.chisquare(freq.values())
print(chi, p)
# plt.figure()
# plt.bar(freq.keys(), freq.values(), width=1)
# plt.show()
