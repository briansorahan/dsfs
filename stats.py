import pandas      as pd
from   scipy       import stats

data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''

data = data.splitlines()

data = [i.split(',') for i in data]

column_names = data[0] # this is the first row
data_rows = data[1:] # these are all the following rows of data
df = pd.DataFrame(data_rows, columns=column_names)

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

print("The mean weekly spend on alcohol in Britain is {0} pounds".format(df['Alcohol'].mean()))
print("The median weekly spend on alcohol in Britain is {0} pounds".format(df['Alcohol'].median()))
print("The mode weekly spend on alcohol in Britain is {0} pounds".format(stats.mode(df['Alcohol'])[0][0]))
      
print("The mean weekly spend on tobacco in Britain is {0} pounds".format(df['Tobacco'].mean()))
print("The median weekly spend on tobacco in Britain is {0} pounds".format(df['Tobacco'].median()))
print("The mode weekly spend on tobacco in Britain is {0} pounds".format(stats.mode(df['Tobacco'])[0][0]))

alcoholRange = max(df['Alcohol']) - min(df['Alcohol'])
print("The range of alcohol weekly spend in Britain is {0}".format(alcoholRange))
print("The standard deviation of alcohol weekly spend in Britain is {0}".format(df['Alcohol'].std()))
print("The variance of alcohol weekly spend in Britain is {0}".format(df['Alcohol'].var()))

tobaccoRange = max(df['Tobacco']) - min(df['Tobacco'])
print("The range of tobacco weekly spend in Britain is {0}".format(tobaccoRange))
print("The standard deviation of tobacco weekly spend in Britain is {0}".format(df['Tobacco'].std()))
print("The variance of tobacco weekly spend in Britain is {0}".format(df['Tobacco'].var()))

