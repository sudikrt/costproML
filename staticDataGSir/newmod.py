from pandas import read_csv
from pandas import datetime
from pandas.tools.plotting import autocorrelation_plot
from pandas import DataFrame
from statsmodels.tsa.arima_model import ARIMA
from matplotlib import pyplot
import pandas as pd
import numpy as np
import statsmodels.api as sm
from pandas.tseries.offsets import *
def parser(x):
	return datetime.strptime(x, '%Y-%m')

series = read_csv('outData.csv', header=0, parse_dates=[1], index_col=1, squeeze=True, date_parser=parser)
print(series.head())

series.plot()
pyplot.show()


model = ARIMA(series, order=(1,1,0))
model_fit = model.fit(disp=0)
print(model_fit.summary())
# plot residual errors
residuals = DataFrame(model_fit.resid)
residuals.plot()
pyplot.show()
residuals.plot(kind='kde')
pyplot.show()
print(residuals.describe())



'''

grouped = series.groupby ('job')
group = list(grouped)[0][1]
ts_data = pd.TimeSeries(group.maxsal.values, index=pd.to_datetime(group.index))

ts_log_data = np.log (ts_data)
#ts_log_data.plot (ax=axes[1], style='b-', label='actual')

model = sm.tsa.ARMA (ts_log_data, order=(1,1)).fit()
#print (model.params)

y_pred = model.predict (ts_log_data.index[0].isoformat(), ts_log_data.index[-1].isoformat())

start_date = ts_log_data.index[-1]+Day (1)
#start_date = pd.to_datetime("2012-07")
end_date = ts_log_data.index[-1] + Day()
#end_date = pd.to_datetime("2016-01 00:00:00")
y_forecast = model.predict(start_date.isoformat(), end_date.isoformat())

#print(y_forecast)
print(np.exp(y_forecast))

#series.plot()
pyplot.show()
'''
