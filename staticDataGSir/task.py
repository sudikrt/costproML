import pandas as pd
from pandas.tseries.offsets import *
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import datetime

df = pd.read_csv ("outDataSingle.csv")

print df.head()
grouped = df.groupby ('job')

print "Job List : Engineer, Tester, Carpenter, Cook, Plumber, Mechanic";
prof = raw_input ("Enter a job :").lower()

if prof == "Engineer".lower():
    group =  list(grouped)[2][1]
elif prof == "Tester".lower():
    group =  list(grouped)[5][1]
elif prof == "Cook".lower():
    group =  list(grouped)[1][1]
elif prof == "Carpenter".lower():
    group =  list(grouped)[0][1]
elif prof == "Plumber".lower() :
    group =  list(grouped)[4][1]
else :
    group =  list(grouped)[3][1]


year = input ("Enter Year :")


ts_data = pd.TimeSeries(group.maxsal.values, index=pd.to_datetime(group.date))
fig, axes = plt.subplots(figsize=(10, 8), nrows=3)
ts_data.plot(ax=axes[0])

ts_log_data = np.log (ts_data)
ts_log_data.plot (ax=axes[1], style='b-', label='actual')

model = sm.tsa.ARMA (ts_log_data, order=(1,1)).fit()

y_pred = model.predict (ts_log_data.index[0].isoformat(), ts_log_data.index[-1].isoformat())
y_pred.plot(ax=axes[2], style='r--', label='in-sample fit')


start_date = (pd.to_datetime(str(year) + '-' + str(01) + '-' + str(01))).date()
da = start_date - ts_log_data.index[-1].date()

start_date = (ts_log_data.index[-1] + Day (1)).date()
end_date = (ts_log_data.index[-1] + Day (da.days)).date()

#start_date = (ts_log_data.index[-1] + Day (1)).date()
#end_date = (ts_log_data.index[-1] + Day (200)).date()
# start_date = (pd.to_datetime(str(year) + '-' + str(01) + '-' + str(01)))
# if (start_date < ts_log_data.index[-1]) :
#     da = (ts_log_data.index[-1] - start_date)
#     start_date = da
#     end_date = (da + Day(1)).date()
# else :
#     da = start_date - ts_log_data.index[-1].date()
#     start_date = (ts_log_data.index[-1] + Day (1)).date()
#     end_date = (ts_log_data.index[-1] + Day (da.days)).date()

y_forecast = model.predict(start_date.isoformat(), end_date.isoformat())

y_forecast.plot(ax=axes[2], style='r--', label='in-sample fit')


#print(y_forecast)
maxSAl = np.exp(y_forecast)
#print str(np.array(maxSAl)[0])
#print(np.exp(y_forecast.tail(1)))


print "Min sal"

ts_data = pd.TimeSeries(group.minsal.values, index=pd.to_datetime(group.date))
#fig, axes = plt.subplots(figsize=(10, 8), nrows=3)
#ts_data.plot(ax=axes[0])

ts_log_data = np.log (ts_data)
#ts_log_data.plot (ax=axes[1], style='b-', label='actual')

model = sm.tsa.ARMA (ts_log_data, order=(1,1)).fit()
y_pred = model.predict (ts_log_data.index[0].isoformat(), ts_log_data.index[-1].isoformat())
#y_pred.plot(ax=axes[2], style='r--', label='in-sample fit')

y_forecast = model.predict(start_date.isoformat(), end_date.isoformat())

minSAl = np.exp(y_forecast.tail(1))

print "Max sal :" + str(maxSAl)
print "Min sal  :" + str(minSAl)

plt.show()
