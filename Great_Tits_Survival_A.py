import pandas as pd
from pandas.tseries.offsets import DateOffset
import seaborn as sns
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64
import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
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
    df2['Date'] = df2['BroodYear'].apply(lambda x: pd.to_datetime(str(x), format='%Y'))
    df2['Date'] += DateOffset(months=3)
    df2['Date'] += pd.to_timedelta(df2['HatchDay'], unit='d')
    df3['Date'] = pd.to_datetime(df3['Tag'], format='%d.%m.%Y')

    # Merge datasets and convert data to float
    df = pd.merge(df1, df2, df3, on=['Date'])
    df['Day14BodyMass'] = df['Day14BodyMass'].astype(float)
    df['MAXD_TA200'] = df['MAXD_TA200'].astype(float)
    df['NumberFledged'] = df['NumberFledged'].astype(float)
    df['MIND_TA200'] = df['MIND_TA200'].astype(float)

    # Graph data and save plots
    lma = sns.lmplot(data=df, x='MAXD_TA200', y='Day14BodyMass', order=2, line_kws={'color': 'green'})
    axa = lma.fig.axes[0]
    axa.set(xlabel='Residual max. T (C) at ages 4-8 d',
            ylabel='Nestling mass at age 14 days (g)')
    a_file_path = 'static/a.png'
    lma.savefig(a_file_path)
    plt.close()

    lmb = sns.lmplot(data=df, x='MAXD_TA200', y='Day14BodyMass', order=2, line_kws={'color': 'green'})
    axb = lmb.fig.axes[0]
    axb.set(xlabel='Max. T (C) at ages 4-8 d',
            ylabel='Nestling mass at age 14 days (g)')
    b_file_path = 'static/b.png'
    lmb.savefig(b_file_path)
    plt.close()

    lmc = sns.lmplot(data=df, x='MIND_TA200', y='NumberFledged', order=2, line_kws={'color': 'green'})
    axc = lmc.fig.axes[0]
    axc.set(xlabel='Residual min. T (C) at ages 6-23 d',
            ylabel='Fledgeling Success')
    c_file_path = 'static/c.png'
    lmb.savefig(c_file_path)
    plt.close()
  
    plt.clf()

    # Render the template with the plots
    return render_template('home.html', plot_url_a=plot_url_a, plot_url_b=plot_url_b, plot_url_c=plot_url_c)

@app.route('/index')
def index():
    return home()

if __name__ == '__main__':
    app.run(debug=True)
