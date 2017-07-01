import pandas as pd
from pandas.tseries.offsets import *
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

df = pd.read_csv ("input.csv", index_col=[0], sep='\t')
grouped = df.groupby ('adserver_id')
group = list(grouped)[0][1]

ts_data = pd.TimeSeries(group.c_25p.values, index=pd.to_datetime(group.day))
fig, axes = plt.subplots(figsize=(10, 8), nrows=3)
ts_data.plot(ax=axes[0])

ts_log_data = np.log (ts_data)
ts_log_data.plot (ax=axes[1], style='b-', label='actual')

model = sm.tsa.ARMA (ts_log_data, order=(1,1)).fit()
print (model.params)

y_pred = model.predict (ts_log_data.index[0].isoformat(), ts_log_data.index[-1].isoformat())
y_pred.plot(ax=axes[1], style='r--', label='in-sample fit')


y_resid = model.resid
y_resid.plot(ax=axes[2])

start_date = ts_log_data.index[-1] + Day(1)
end_date = ts_log_data.index[-1] + Day(200)

y_forecast = model.predict(start_date.isoformat(), end_date.isoformat())
y_forecast.plot(ax=axes[1], style='r--', label='in-sample fit')
#print(y_forecast)
print(np.exp(y_forecast))

plt.show()
