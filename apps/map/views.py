import pandas as pd
import plotly
import numpy as np
import plotly.graph_objs as go
import plotly.offline as offline
from plotly.graph_objs import *
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from django.shortcuts import render, HttpResponse
import datetime
import json

# Create your views here.


def index(request):
    df = pd.read_csv('data2018.csv')
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
    all_jobs = ["15-0000",'15-1121','15-1131','15-1132','15-1133','15-1134','15-1141','15-1142','15-1143','15-1151','15-1152','15-1199','15-1111','15-1122']

    fig.update_layout(
        title_text='Average Salary of Computer/Technical Jobs',
        geo=dict(
            scope='usa',
            projection=go.layout.geo.Projection(type='albers usa'),
            showlakes=False,  # lakes
            lakecolor='rgb(255, 255, 255)'),
        margin=dict(t=5,b=5,r=5,l=5)
    )

    state_conv_list = {
        'AL':0,
        'AK':1,
        'AZ':2,
        'AR':3,
        'CA':4,
        'CO':5,
        'CT':6,
        'DE':7,
        'FL':8,
        'GA':9,
        'HI':10,
        'ID':11,
        'IL':12,
        'IN':13,
        'IA':14,
        'KS':15,
        'KY':16,
        'LA':17,
        'ME':18,
        'MD':19,
        'MA':20,
        'MI':21,
        'MN':22,
        'MS':23,
        'MO':24,
        'MT':25,
        'NE':26,
        'NV':27,
        'NH':28,
        'NJ':29,
        'NM':30,
        'NY':31,
        'NC':32,
        'ND':33,
        'OH':34,
        'OK':35,
        'OR':36,
        'PA':37,
        'RI':38,
        'SC':39,
        'SD':40,
        'TN':41,
        'TX':42,
        'UT':43,
        'VT':44,
        'VA':45,
        'WA':46,
        'WV':47,
        'WI':48,
        'WY':49}

    def state_annual_AVG(year, ST_num):
        annual_avg = 0
        allSTList = []
        jobList = []
        data = pd.read_csv("data"+str(year)+".csv")
        codedata = data[(data['OCC_CODE']== '15-0000')]
        allSTList = codedata['A_MEAN'].tolist()
        annual_avg = allSTList[ST_num]
        return annual_avg

    def state_jobs(ST_num, jobs=all_jobs):
        annual_avg = 0
        allSTList = []
        jobList = []
        data = pd.read_csv("data2018.csv")
        for i in range(len(jobs)):
            codedata = data[(data['OCC_CODE']== jobs[i])]
            # print(jobs[i])
            # print(codedata)
            allSTList = codedata['A_MEAN'].tolist()
        annual_avg = allSTList[ST_num]
        # print("*"*20)
        # print(annual_avg, ST_num)
        return annual_avg

    def calc_annual_AVG(year):
        data = pd.read_csv("data"+str(year)+".csv")
        codedata = data[(data['OCC_CODE'] == "15-0000")]
        testArr = codedata['A_MEAN'].tolist()
        total =0
        length = len(testArr)
        for i in range(length):
            total += int(testArr[i])

        annual_avg = int(total/length)
        return annual_avg

    avg2018 = calc_annual_AVG(2018)
    avg2017 = calc_annual_AVG(2017)
    avg2016 = calc_annual_AVG(2016)
    st_avg2018 = state_annual_AVG(2018, 0)
    st_avg2017 = state_annual_AVG(2017, 0)
    st_avg2016 = state_annual_AVG(2016, 0)
    # print(avg2016,avg2017,avg2018)
    # print(st_avg2016,st_avg2017,st_avg2018)

    print(state_jobs(46))
    # fig.show()
    sal_map = offline.plot(fig, include_plotlyjs=False, output_type='div')

    years = [datetime.datetime(year=2016, month=1, day=1),
            datetime.datetime(year=2017, month=1, day=1),
            datetime.datetime(year=2018, month=1, day=1)]
    
    graph = go.Figure()
    graph.add_trace(go.Scatter(x=years, y=[st_avg2016, st_avg2017, st_avg2018], name="Alabama"))
    graph.add_trace(go.Scatter(x=years, y=[avg2016, avg2017, avg2018], name="National Average"))
    graph.update_layout(
        xaxis_range=[datetime.datetime(2016,1,1), datetime.datetime(2018,1,1)],
        autosize=True,
        height=200,
        margin=dict(t=5,b=5,r=5,l=5)
        
        )

    line_graph = offline.plot(graph, include_plotlyjs=False, output_type='div')
    context = {
    'map': sal_map,
    'line_graph' : line_graph
    }
    return render(request, "map/index.html", context)


# pd.options.mode.chained_assignment = None
