from numpy import exp
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller

filepath = "E:\Python Workspace\Data Science Projects\Time Series\Alcohol Demand\data\\alcohol-demand-log-spirits-consu.csv"


def dateparse(dates):
    return pd.datetime.strptime(dates, '%Y-%m')


df = pd.read_csv(filepath, header=0, names=['Month', 'log(Consumption)'],
                 parse_dates=[0], index_col=[0],
                 error_bad_lines=False, date_parser=dateparse)

log_ts = df['log(Consumption)']
ts = exp(log_ts)


def test_stationarity(ts):
    rolmean = ts.rolling(window=3, center=False).mean()
    rolstd = ts.rolling(window=3, center=False).std()

    orig = plt.plot(ts, color='blue', label='Original')
    mean = plt.plot(rolmean, color='red', label='Rolling Mean')
    std = plt.plot(rolstd, color='black', label='Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show(block=False)

    print('Results of Dickey-Fuller Test:')
    dftest = adfuller(ts, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4],
                         index=['Test Statistic', 'p-value', '#Lags Used',
                                'Number of Observations Used'])
    for key, value in dftest[4].items():
        dfoutput['Critical Value (%s)' % key] = value

    print(dfoutput)


test_stationarity(log_ts)
