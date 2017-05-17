import pandas as pd
from pandas.tseries.offsets import *
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import datetime
from pandas.tools.plotting import lag_plot
from pandas.tools.plotting import autocorrelation_plot

df = pd.read_csv ("outDataSingle.csv", header=0)

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



group.drop('job', axis=1, inplace=True)

ts_data = pd.TimeSeries(group.maxsal.values, index=pd.to_datetime(group.date))

ts_log_data = np.log (ts_data)


model = sm.tsa.ARMA (ts_log_data, order=(1,1)).fit()

y_pred = model.predict (ts_log_data.index[0].isoformat(), ts_log_data.index[-1].isoformat())

start_date = (pd.to_datetime(str(year) + '-' + str(01) + '-' + str(01))).date()
da = start_date - ts_log_data.index[-1].date()

start_date = (ts_log_data.index[-1] + Day (1)).date()
end_date = (ts_log_data.index[-1] + Day (da.days)).date()

y_forecast = model.predict(start_date.isoformat(), end_date.isoformat())

y_pred.plot()
y_forecast.plot()

#group.plot ()
#lag_plot(group)
#autocorrelation_plot(group)

maxSAl = np.exp(y_forecast)

print "Max sal :" + str(maxSAl)

plt.show ()
