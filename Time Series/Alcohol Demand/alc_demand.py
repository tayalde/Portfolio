import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.tsa.arima_model import ARIMA


filepath = "E:\Python Workspace\Data Science Projects\Time Series\\" + \
           "Alcohol Demand\data\\alcohol-demand-log-spirits-consu.csv"


def dateparse(dates):
    """ Date formatting
    """
    return pd.datetime.strptime(dates, '%Y-%m')


df = pd.read_csv(filepath, header=0, names=['Month', 'log(Consumption)'],
                 parse_dates=[0], index_col=[0],
                 error_bad_lines=False, date_parser=dateparse)

log_ts = df['log(Consumption)']
ts = np.exp(log_ts)


def test_stationarity(ts):
    """ Test Stationarity of the TS
    """

    # We use a window of 3 to create yearly averages
    # since the data is in 4, 8, and 12 month intervals
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


# Runs the test on the log data
test_stationarity(log_ts)

# Runs the test on the difference b/n the log and its rolling mean
log_ts_moving_avg_diff = log_ts - log_ts.rolling(window=3, center=False).mean()
log_ts_moving_avg_diff.dropna(inplace=True)
test_stationarity(log_ts_moving_avg_diff)

# Runs the test on the difference b/n the log and
# its exponentially weighted moving average
expweight_avg = log_ts.ewm(halflife=3, min_periods=0, adjust=True,
                           ignore_na=True).mean()
log_ts_ewma_diff = log_ts - expweight_avg
test_stationarity(log_ts_ewma_diff)

""" Eliminating Trend and Seasonality """

# Differencing to improve Stationarity
log_ts_diff = log_ts - log_ts.shift()
plt.plot(log_ts_diff)
log_ts_diff.dropna(inplace=True)
test_stationarity(log_ts_diff)

# Decomposing
decomposition = seasonal_decompose(log_ts)
trend = decomposition.trend
seasonal = decomposition.seasonal
residual = decomposition.resid

plt.subplot(411)
plt.plot(log_ts, label='Original')
plt.legend(loc='best')
plt.subplot(412)
plt.plot(trend, label='Trend')
plt.legend(loc='best')
plt.subplot(413)
plt.plot(seasonal, label='Seasonality')
plt.legend(loc='best')
plt.subplot(414)
plt.plot(residual, label='Residuals')
plt.legend(loc='best')
plt.tight_layout()

log_ts_decompose = residual
log_ts_decompose.dropna(inplace=True)
test_stationarity(log_ts_decompose)

lag_acf = acf(log_ts_diff, nlags=20)
lag_pacf = pacf(log_ts_diff, nlags=20, method='ols')

# Plot acf
plt.subplot(121)
plt.plot(lag_acf)
plt.axhline(y=0, linestyle='--', color='gray')
plt.axhline(y=-1.96/np.sqrt(len(log_ts_diff)), linestyle='--', color='gray')
plt.axhline(y=1.96/np.sqrt(len(log_ts_diff)), linestyle='--', color='gray')
plt.title('Autocorrelation Function')

# Plot pacf
plt.subplot(122)
plt.plot(lag_pacf)
plt.axhline(y=0, linestyle='--', color='gray')
plt.axhline(y=-1.96/np.sqrt(len(log_ts_diff)), linestyle='--', color='gray')
plt.axhline(y=1.96/np.sqrt(len(log_ts_diff)), linestyle='--', color='gray')
plt.title('Partial Autocorrelation Function')
plt.tight_layout()

# AR Model
model = ARIMA(log_ts, order=(2, 1, 0))
results_AR = model.fit(disp=-1)
plt.plot(log_ts_diff)
plt.plot(results_AR.fittedvalues, color='red')
plt.title('RSS: %.4f' % sum((results_AR.fittedvalues - log_ts_diff) ** 2))

# MA model
model = ARIMA(log_ts, order=(0, 1, 2))
results_MA = model.fit(disp=-1)
plt.plot(log_ts_diff)
plt.plot(results_MA.fittedvalues, color='red')
plt.title('RSS: %.4f' % sum((results_MA.fittedvalues - log_ts_diff) ** 2))

# Combined model
model = ARIMA(log_ts, order=(2, 1, 2))
results_ARIMA = model.fit(disp=-1)
plt.plot(log_ts_diff)
plt.plot(results_ARIMA.fittedvalues, color='red')
plt.title('RSS: %.4f' % sum((results_ARIMA.fittedvalues - log_ts_diff) ** 2))

# Predictions
predictions_ARIMA_diff = pd.Series(results_ARIMA.fittedvalues, copy=True)
print(predictions_ARIMA_diff.head())
predictions_ARIMA_diff_cumsum = predictions_ARIMA_diff.cumsum()
print(predictions_ARIMA_diff_cumsum.head())

predictions_ARIMA_log = pd.Series(log_ts.ix[0], index=log_ts.index)
predictions_ARIMA_log = predictions_ARIMA_log.add(predictions_ARIMA_diff_cumsum, fill_value=0)
predictions_ARIMA_log.head()

predictions_ARIMA = np.exp(predictions_ARIMA_log)
plt.plot(log_ts)
plt.plot(trend)
plt.title('RMSE: %.4f' % np.sqrt(sum((predictions_ARIMA-ts) ** 2) / len(ts)))
