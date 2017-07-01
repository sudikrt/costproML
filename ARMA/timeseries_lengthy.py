import pandas as pd
from pandas.tseries.offsets import *
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

csv_file = 'input.csv'
df = pd.read_csv(csv_file, index_col=[0], sep='\t')
grouped = df.groupby('adserver_id')


def forecast_func(group):
    ts_log_data = np.log(pd.TimeSeries(group.c_start.values, index=pd.to_datetime(group.day)))
    # for some group, it raise convergence issue
    try:
        model = sm.tsa.ARMA(ts_log_data, order=(1,1)).fit()
        start_date = ts_log_data.index[-1] + Day(1)
        end_date = ts_log_data.index[-1] + Day(7)
        y_forecast = model.predict(start_date.isoformat(), end_date.isoformat())
        return pd.Series(np.exp(y_forecast).values, np.arange(1, 8))
    except Exception:
        pass


result = df.groupby('adserver_id').apply(forecast_func)
