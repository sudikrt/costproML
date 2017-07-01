from flask import Flask, jsonify
import json
import mimerender

import pandas as pd
from pandas.tseries.offsets import *
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

df = pd.read_csv ("outDataSingle.csv")

print df.head()
grouped = df.groupby ('job')

mimerender = mimerender.FlaskMimeRender()

app = Flask(__name__)

@app.route('/')
@app.route('/<prof>/<year>')
def greet(prof='world', year='2017'):

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

    y_forecast = model.predict(start_date.isoformat(), end_date.isoformat())

    y_forecast.plot(ax=axes[2], style='r--', label='in-sample fit')

    maxSAl = np.exp(y_forecast.tail(1))

    # getMin (prof, year)

    # ts_data = pd.TimeSeries(group.minsal.values, index=pd.to_datetime(group.date))
    # ts_log_data = np.log (ts_data)
    # model = sm.tsa.ARMA (ts_log_data, order=(1,1)).fit()
    #
    # y_pred = model.predict (ts_log_data.index[0].isoformat(), ts_log_data.index[-1].isoformat())
    # start_date = (pd.to_datetime(str(year) + '-' + str(01) + '-' + str(01))).date()
    # da = start_date - ts_log_data.index[-1].date()
    #
    # start_date = (ts_log_data.index[-1] + Day (1)).date()
    # end_date = (ts_log_data.index[-1] + Day (da.days)).date()
    #
    # y_forecast = model.predict(start_date.isoformat(), end_date.isoformat())
    #
    # y_forecast.plot(ax=axes[2], style='r--', label='in-sample fit')
    #
    # minSAl = np.exp(y_forecast.tail(1))

    # data = {}
    # data['message'] = "success"
    # data['price'] = str(np.array(maxSAl)[0])

    dat = [
        {'param': 'message', 'val': 'success'},
        {'param': 'price', 'val': np.array(maxSAl)[0]}
    ]
    return jsonify(results=dat)
    # jsonify will do for us all the work, returning the
    # previous data structure in JSO

    # return json_response({"message": "success", 'price':str(np.array(maxSAl)[0])}, status_code=201)
    # return jsonify(
    #     message='success',
    #
    # )
    #return {'message':'success','price':str(np.array(maxSAl)[0])}
    #return data
    #return {'message': 'success','price'+str(maxSAl) '}  #' - ' +str(maxSAl)  +

def getMin(prof, year):

    ts_data = pd.TimeSeries(group.minsal.values, index=pd.to_datetime(group.date))
    ts_log_data = np.log (ts_data)
    model = sm.tsa.ARMA (ts_log_data, order=(1,1)).fit()

    y_pred = model.predict (ts_log_data.index[0].isoformat(), ts_log_data.index[-1].isoformat())
    start_date = (pd.to_datetime(str(year) + '-' + str(01) + '-' + str(01))).date()
    da = start_date - ts_log_data.index[-1].date()

    start_date = (ts_log_data.index[-1] + Day (1)).date()
    end_date = (ts_log_data.index[-1] + Day (da.days)).date()

    y_forecast = model.predict(start_date.isoformat(), end_date.isoformat())

    y_forecast.plot(ax=axes[2], style='r--', label='in-sample fit')

    minSAl = np.exp(y_forecast.tail(1))

    return minSAl

if __name__ == "__main__":
    app.run(port=8000)
