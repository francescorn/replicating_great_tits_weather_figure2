# Import libraries and dependencies
import pandas as pd
from pandas.tseries.offsets import DateOffset
import seaborn as sns
import matplotlib.pyplot as plt
import requests

# Open file in excel and assign variables
url = "https://github.com/francescorn/replicating_great_tits_weather_figure2/raw/main/weather_effects_on_great_tits.xlsx"
response = requests.get(url)
with open("weather_effects_on_great_tits.xlsx", "wb") as f:
    f.write(response.content)
xlsx = pd.ExcelFile("weather_effects_on_great_tits.xlsx")
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
lm = sns.lmplot(data=df, x='MAXD_TA200', y='Day14BodyMass', hue='BroodYear', order=2, line_kws={'color': 'green'})
lm.set(xlabel='Residual max. T (C) at ages 4-8 d', ylabel='Nestling mass at age 14 days (g)')
plt.legend(title='Year', loc='best')
plt.show()
