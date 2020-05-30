# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 16:24:31 2019

@author: semiclog

https://blog.heptanalytics.com/2018/08/07/flask-plotly-dashboard/
"""

import plotly
import plotly.graph_objs as go

import pandas as pd
import numpy as np
import json

from flask import Flask, render_template #this has changed

def create_plot():


    N = 40
    x = np.linspace(0, 1, N)
    y = np.random.randn(N)
    df = pd.DataFrame({'x': x, 'y': y}) # creating a sample dataframe


    data = [
        go.Bar(
            x=df['x'], # assign x as the dataframe column 'x'
            y=df['y']
        )
    ]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

app = Flask(__name__)


@app.route('/')
def index():

    bar = create_plot()
    return render_template('index_tutorial.html', plot=bar)


if __name__ == '__main__':
    app.run()