import pandas as pd
from pandas.tseries.offsets import *
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

df = pd.read_csv ("outData.csv")
grouped = df.groupby ('job')
group = list(grouped)[0][1]

ts_data = pd.TimeSeries(group.maxsal.values, index=pd.to_datetime(group.date))
fig, axes = plt.subplots(figsize=(10, 8), nrows=2)
ts_data.plot(ax=axes[0])

ts_log_data = np.log (ts_data)
#ts_log_data.plot (ax=axes[1], style='b-', label='actual')

model = sm.tsa.ARMA (ts_log_data, order=(1,1)).fit()
#print (model.params)

y_pred = model.predict (ts_log_data.index[0].isoformat(), ts_log_data.index[-1].isoformat())
#y_pred.plot(ax=axes[2], style='r--', label='in-sample fit')


#y_resid = model.resid
#y_resid.plot(ax=axes[3])

start_date = ts_log_data.index[-1] + Day (1)
#start_date = pd.to_datetime("2012-07")
end_date = ts_log_data.index[-1] + Day (21)
#end_date = pd.to_datetime("2016-01 00:00:00")
y_forecast = model.predict(start_date.isoformat(), end_date.isoformat())

#print(y_forecast)
print(np.exp(y_forecast))

plt.show()
