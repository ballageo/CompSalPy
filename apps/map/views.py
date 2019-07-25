import pandas as pd
import plotly
import numpy as np
import plotly.graph_objs as go
import plotly.offline as offline
from plotly.graph_objs import *
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from django.shortcuts import render, HttpResponse
import datetime

# Create your views here.


def index(request):
    df = pd.read_csv('data2018.csv')
    # df_year = df[(df['Year'] == 2018)]

    for col in df.columns:
        df.loc[col] = df[col].astype(str)

    x = "State: " + df['ST'] + '<br>' + 'Job Title: ' + \
        df['OCC_TITLE'] + '<br>' + 'Annual Sal: ' + '$' + df['A_MEAN']

    fig = go.Figure(data=go.Choropleth(
        locations=df['ST'],
        z=df['A_MEAN'],
        locationmode='USA-states',
        colorscale="greens",
        autocolorscale=False,
        text=x,  # hover text
        marker_line_color='white',  # line markers between states
        colorbar_title="USD"
    ))

    fig.update_layout(
        title_text='Average Salary of Computer/Technical Jobs',
        geo=dict(
            scope='usa',
            projection=go.layout.geo.Projection(type='albers usa'),
            showlakes=False,  # lakes
            lakecolor='rgb(255, 255, 255)'),
        margin=dict(t=5,b=5,r=5,l=5)
    )

    def calc_annual_AVG(csv):
        data = pd.read_csv(csv)

        codedata = data[(data['OCC_CODE'] == "15-0000")]
        testArr = codedata['A_MEAN'].tolist()
        total =0
        length = len(testArr)
        for i in range(length):
            total += int(testArr[i])

        annual_avg = int(total/length)
        return annual_avg

    avg2018 = calc_annual_AVG("data2018.csv")
    avg2017 = calc_annual_AVG("data2017.csv")
    avg2016 = calc_annual_AVG("data2016.csv")
    print(avg2016, avg2017, avg2018)
        
    # fig.show()
    sal_map = offline.plot(fig, include_plotlyjs=False, output_type='div')

    years = [datetime.datetime(year=2016, month=1, day=1),
            datetime.datetime(year=2017, month=1, day=1),
            datetime.datetime(year=2018, month=1, day=1)]
    
    graph = go.Figure()
    graph.add_trace(go.Scatter(x=years, y=[80000, 83500, 96000], name="2018"))
    graph.add_trace(go.Scatter(x=years, y=[50000, 63500, 76000], name="2017"))
    graph.update_layout(
        xaxis_range=[datetime.datetime(2016,1,1), datetime.datetime(2018,1,1)],
        autosize=True,
        height=200,
        margin=dict(t=5,b=5,r=5,l=5)
        
        )

    line_graph = offline.plot(graph, include_plotlyjs=False, output_type='div')
    line_graph2 = offline.plot(graph, include_plotlyjs=False, output_type='div')
    context = {
    'map': sal_map,
    'line_graph' : line_graph,
    'line_graph2' : line_graph2,

    }
    return render(request, "map/index.html", context)
