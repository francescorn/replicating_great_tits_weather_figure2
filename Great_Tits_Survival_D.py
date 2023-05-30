# Import libraries and dependencies
import pandas as pd
from pandas.tseries.offsets import DateOffset
import seaborn as sns
import matplotlib.pyplot as plt

# Open file in excel and assign variables
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
df['NumberFledged'] = df['NumberFledged'].astype(float)
df['MIND_TA200'] = df['MIND_TA200'].astype(float)

# Graph chart
fig, ax = sns.lmplot(data = df, x = 'MIND_TA200', y = 'NumberFledged', order=2, line_kws={'color': 'green'})
ax.set(xlabel='Min. T (C) at ages 6-23 d',
       ylabel='Fledgling Success')
file_path = 'd.png'
fig.savefig(file_path)
plt.show()