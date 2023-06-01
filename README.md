# Replicating Great Tits Weather Study
I am replicating the following study: "Weather effects on nestling survival of great tits vary according to the developmental stage" conducted by:
Fernando Marques-Santos, Universidade Federal de Minas Gerais and
Niels J. Dingemanse,  Ludwig Maximilian University of Munich.
I am not affiliated with conducting the study or am or was a member of either university.
I am using python, pandas, matplotlib, and seaborn to graph the charts from Figure 2. https://onlinelibrary.wiley.com/doi/epdf/10.1111/jav.02421

The study examined how reproductive characteristics of great tits in southern Germany are influenced by temperature and precipitation during specific time periods when the nestlings are growing. Three different models were used to analyze the data for each reproductive trait. The graphs illustrate the effects of environmental variables within a single year (left column) and between different years (right column). The years are represented by varying shades of gray in the right column. The gray bands represent the 95% credible intervals. The significance of linear and squared weather parameters is indicated by whether they differ from zero or are non-significant.In graphs a and b, individual nestlings are depicted as data points, while in graphs c and d, individual nests are represented as slightly displaced points. The curves presented in the figures represent the parameters calculated for nests with seven hatchlings, which is the average population size.

I merged each sheet on the date with the following modules in the Pandas package: merge, DateOffset, to_timedelta, and to_datetime. I then used matplot lib and seaborn to graph the charts.

I downloaded the two data sets from driad and received the weather data by email from Dr. Marques-Santos upon request. I imported the three data sets into a combined excel spreadsheet, weather_effects_on_great_tits.xlsx. I used the requests package to read and add a column called 'Data' from the excel sheet. https://datadryad.org/stash/dataset/doi:10.5061%2Fdryad.51c59zw68

## Findings
All graphs are coded using the packages pandas, seaborn, requests, and matplotlib. 

### a)
The graph depicts the relationship between the residual maximum temperature at ages 4-8 days and the nestling mass at age 14 days. There appears to be a 

![a](images/a.png)

### b)
This graph illustrates the relationship between the residual maximum temperature at ages 4-8 days and the nestling mass at age 14 days for different years.

![b](images/baa.png)

### c)
This graph shows the relationship between the number of fledglings per nest are depicted and the residual minimum temperature.

![c](images/c.png)
