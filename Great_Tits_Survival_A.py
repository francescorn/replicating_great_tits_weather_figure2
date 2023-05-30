# Import libraries and dependencies
import pandas as pd
from pandas.tseries.offsets import DateOffset
import seaborn as sns
import requests
import matplotlib.pyplot as plt

# Open file in excel and assign variables
url = "https://github.com/francescorn/replicating_great_tits_weather_figure2/raw/main/weather_effects_on_great_tits.xlsx"
response = requests.get(url)
with open("weather_effects_on_great_tits.xlsx", "wb") as f:
    f.write(response.content)
xlsx = pd.ExcelFile("weather_effects_on_great_tits.xlsx")
df1 = pd.read_excel(xlsx, 'Sheet1')
df2 = pd.read_excel(xlsx, 'Sheet2')
df3 = pd.read_excel(xlsx, 'Sheet3')
df1.dropna(subset=['FirstEggDay'], inplace=True)

# Convert all datasets to dataframes
df1['Date'] = df1['BroodYear'].apply(lambda x: pd.to_datetime(str(x), format='%Y'))
df1['Date'] += DateOffset(months=3)
df1['Date'] += pd.to_timedelta(df1['FirstEggDay'], unit='d')
df2['Date'] = df2['BroodYear'].apply(lambda x: pd.to_datetime(str(x), format='%Y'))
df2['Date'] += DateOffset(months=3)
df2['Date'] += pd.to_timedelta(df2['HatchDay'], unit='d')
df3['Date'] = pd.to_datetime(df3['Tag'], format='%d.%m.%Y')

# Merge datasets and convert data to float
df = pd.merge(pd.merge(df1, df2, on='Date'), df3, on='Date')
df['Day14BodyMass'] = df['Day14BodyMass'].astype(float)
df['MAXD_TA200'] = df['MAXD_TA200'].astype(float)
df['NumberFledged'] = df['NumberFledged'].astype(float)
df['MIND_TA200'] = df['MIND_TA200'].astype(float)

# Graph data and save plots
lm = sns.lmplot(data=df, x='MAXD_TA200', y='Day14BodyMass', order=2, line_kws={'color': 'green'})
axa = lm.axes[0, 0]
axa.set(xlabel='Residual max. T (C) at ages 4-8 d', ylabel='Nestling mass at age 14 days (g)')
fig = lm.fig
file_path = 'a.png'
fig.savefig(file_path)
plt.show()
