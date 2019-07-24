import pandas as pd
import plotly
import plotly.graph_objs as go
import plotly.offline as offline
from plotly.graph_objs import *
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from django.shortcuts import render, HttpResponse
import datetime

# Create your views here.


def index(request):
    df = pd.read_csv('data2018fixed.csv')
    # df_year = df[(df['Year'] == 2018)]

    for col in df.columns:
        df.loc[col] = df[col].astype(str)

    x = "State: " + df['ST'] + '<br>' + 'Job Title: ' + \
        df['OCC_TITLE'] + '<br>' + 'Annual Sal: ' + '$' + df['A_MEAN']

    # df_year['text'] = df_year['STATE'] + '<br>' + df_year['ST'] + '<br>'  + ' Job ' + '<br>' + df_year['OCC_TITLE'] + '<br>' + df_year['A_MEAN']
    # 'Fruits ' + df_year['total fruits'] + ' Veggies ' + df_year['total veggies'] + '<br>' + \
    # 'Wheat ' + df_year['wheat'] + ' Corn ' + df_year['corn']

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
        title_text='Technical Job<br>(Hover for breakdown)',
        geo=dict(
            scope='usa',
            projection=go.layout.geo.Projection(type='albers usa'),
            showlakes=False,  # lakes
            lakecolor='rgb(255, 255, 255)'),
    )

    # fig.show()
    x = offline.plot(fig, include_plotlyjs=False, output_type='div')

    years = [datetime.datetime(year=2016, month=1, day=1),
            datetime.datetime(year=2017, month=1, day=1),
            datetime.datetime(year=2018, month=1, day=1)]

    graph = go.Figure(data=[go.Scatter(x=years, y=[1, 3, 6])])
    graph.update_layout(xaxis_range=[datetime.datetime(
        2016,1,1), datetime.datetime(2018,1,1)])

    y = offline.plot(graph, include_plotlyjs=False, output_type='div')
    context = {
    'x': x,
    'graph' : y
    }
    return render(request, "map/index.html", context)


# pd.options.mode.chained_assignment = None
