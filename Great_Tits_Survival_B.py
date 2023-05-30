# Import libraries and dependencies
import pandas as pd
from pandas.tseries.offsets import DateOffset
import seaborn as sns
import matplotlib.pyplot as plt

# Open file in excel and assign variables
xlsx = pd.ExcelFile(r'/Users/Frances/Python/Personal Projects/Weather effects on nestling survival of great tits vary according to the developmental stage .xlsx')
df1 = pd.read_excel(xlsx, 'Sheet1')
df2 = pd.read_excel(xlsx, 'Sheet2')
df3 = pd.read_excel(xlsx, 'Sheet3')
df1.dropna(subset=['FirstEggDay'], inplace = True)

# Convert all datasets to dateframe
df1['Date'] = df1['BroodYear'].apply(lambda x: pd.to_datetime(str(x), format='%Y'))
df1['Date'] += DateOffset(months = 3)
df1['Date'] += pd.to_timedelta(df1['FirstEggDay'], unit='d')
df2['Date'] = df2['BroodYear'].apply(lambda x: pd.to_datetime(str(x), format='%Y'))
df2['Date'] += DateOffset(months = 3)
df3['Date'] = pd.to_datetime(df3['Tag'], format='%d.%m.%Y')

# Merge datasets and convert data to float
df = pd.merge(df2, df3, on=['Date'])

# Add average max temp per year
df['Day14BodyMass'] = df['Day14BodyMass'].astype(float)
df['MAXD_TA200'] = df['MAXD_TA200'].astype(float)

# Graph chart
fig, ax = sns.lmplot(data = df, x = 'MAXD_TA200', y = 'Day14BodyMass', order=2, line_kws={'color': 'green'})
ax.set(xlabel='Residual max. T (C) at ages 4-8 d',
       ylabel='Nestling mass at age 14 days (g)')
file_path = '/Users/Frances/Documents/Python/Personal Projects/b.png'
fig.savefig(file_path)
plt.show()