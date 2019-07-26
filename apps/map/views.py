import pandas as pd
import plotly
import numpy as np
import plotly.graph_objs as go
import plotly.offline as offline
import plotly.graph_objs
from plotly.graph_objs import *
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from django.shortcuts import render, HttpResponse, redirect
import datetime
import json

all_jobs = ["15-0000", '15-1121', '15-1131', '15-1132', '15-1133', '15-1134', '15-1141',
                '15-1142', '15-1143', '15-1151', '15-1152', '15-1199', '15-1111', '15-1122']

def state_annual_AVG(year, ST_num):
    annual_avg = 0
    allSTList = []
    jobList = []
    data = pd.read_csv("data"+str(year)+".csv")
    codedata = data[(data['OCC_CODE'] == '15-0000')]
    allSTList = codedata['A_MEAN'].tolist()
    annual_avg = allSTList[ST_num]
    return annual_avg

def calc_annual_AVG(year):
    data = pd.read_csv("data"+str(year)+".csv")
    codedata = data[(data['OCC_CODE'] == "15-0000")]
    testArr = codedata['A_MEAN'].tolist()
    total = 0
    length = len(testArr)
    for i in range(length):
        total += int(testArr[i])

    annual_avg = int(total/length)
    return annual_avg

def state_jobs(ST_num, jobs=all_jobs):
    annual_avgs = []
    addSTList = []
    jobList = []
    data = pd.read_csv("data2018.csv")
    for i in range(len(jobs)):
        codedata = data[(data['OCC_CODE'] == jobs[i])]
        addSTList = codedata[(codedata['ST'] == state_conv_list[ST_num])]
        # print(addSTList)
        annual_avgs.append(
            [addSTList['OCC_CODE'].tolist(), addSTList['A_MEAN'].tolist()])
    return annual_avgs

def drawlineGraph():
        line_graph = offline.plot(graph, include_plotlyjs=False, output_type='div')
        return line_graph
    

# Create your views here.
def index(request):
    states = {
        "Alabama": "AL",
        "Alaska": "AK",
        "Arizona": "AZ",
        "Arkansas": "AR",
        "California": "CA",
        "Colorado": "CO",
        "Connecticut": "CT",
        "Delaware": "DE",
        "Florida": "FL",
        "Georgia": "GA",
        "Hawaii": "HI",
        "Idaho": "ID",
        "Illinois": "IL",
        "Indiana": "IN",
        "Iowa": "IA",
        "Kansas": "KS",
        "Kentucky": "KY",
        "Louisiana": "LA",
        "Maine": "ME",
        "Maryland": "MD",
        "Massachusetts": "MA",
        "Michigan": "MI",
        "Minnesota": "MN",
        "Mississippi": "MS",
        "Missouri": "MO",
        "Montana": "MT",
        "Nebraska": "NE",
        "Nevada": "NV",
        "New Hampshire": "NH",
        "New Jersey": "NJ",
        "New Mexico": "NM",
        "New York": "NY",
        "North Carolina": "NC",
        "North Dakota": "ND",
        "Ohio": "OH",
        "Oklahoma": "OK",
        "Oregon": "OR",
        "Pennsylvania": "PA",
        "Rhode Island": "RI",
        "South Carolina": "SC",
        "South Dakota": "SD",
        "Tennessee": "TN",
        "Texas": "TX",
        "Utah": "UT",
        "Vermont": "VT",
        "Virginia": "VA",
        "Washington": "WA",
        "West Virginia": "WV",
        "Wisconsin": "WI",
        "Wyoming": "WY"
    }
    statesNoWA = {
        "Alabama": "AL",
        "Alaska": "AK",
        "Arizona": "AZ",
        "Arkansas": "AR",
        "California": "CA",
        "Colorado": "CO",
        "Connecticut": "CT",
        "Delaware": "DE",
        "Florida": "FL",
        "Georgia": "GA",
        "Hawaii": "HI",
        "Idaho": "ID",
        "Illinois": "IL",
        "Indiana": "IN",
        "Iowa": "IA",
        "Kansas": "KS",
        "Kentucky": "KY",
        "Louisiana": "LA",
        "Maine": "ME",
        "Maryland": "MD",
        "Massachusetts": "MA",
        "Michigan": "MI",
        "Minnesota": "MN",
        "Mississippi": "MS",
        "Missouri": "MO",
        "Montana": "MT",
        "Nebraska": "NE",
        "Nevada": "NV",
        "New Hampshire": "NH",
        "New Jersey": "NJ",
        "New Mexico": "NM",
        "New York": "NY",
        "North Carolina": "NC",
        "North Dakota": "ND",
        "Ohio": "OH",
        "Oklahoma": "OK",
        "Oregon": "OR",
        "Pennsylvania": "PA",
        "Rhode Island": "RI",
        "South Carolina": "SC",
        "South Dakota": "SD",
        "Tennessee": "TN",
        "Texas": "TX",
        "Utah": "UT",
        "Vermont": "VT",
        "Virginia": "VA",
        "West Virginia": "WV",
        "Wisconsin": "WI",
        "Wyoming": "WY"
    }
    df = pd.read_csv('data2018.csv')
    # df_year = df[(df['Year'] == 2018)]

    for col in df.columns:
        df.loc[col] = df[col].astype(str)

    x = "State: " + df['ST'] + '<br>' + 'Job Title: ' + \
        df['OCC_TITLE'] + '<br>' + 'Annual Sal: ' + '$' + df['A_MEAN']

    color = "blue"

    fig = go.Figure(data=go.Choropleth(
        locations=df['ST'],
        z=df['A_MEAN'],
        locationmode='USA-states',
        colorscale=color+"s",    #<----Color for map
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
            margin=dict(t=0, b=0, r=5, l=5),
    )

    state_conv_list = {
        0: 'AL',
        1: 'AK',
        2: 'AZ',
        3: 'AR',
        4: 'CA',
        5: 'CO',
        6: 'CT',
        7: 'DE',
        8: 'FL',
        9: 'GA',
        10: 'HI',
        11: 'ID',
        12: 'IL',
        13: 'IN',
        14: 'IA',
        15: 'KS',
        16: 'KY',
        17: 'LA',
        18: 'ME',
        19: 'MD',
        20: 'MA',
        21: 'MI',
        22: 'MN',
        23: 'MS',
        24: 'MO',
        25: 'MT',
        26: 'NE',
        27: 'NV',
        28: 'NH',
        29: 'NJ',
        30: 'NM',
        31: 'NY',
        32: 'NC',
        33: 'ND',
        34: 'OH',
        35: 'OK',
        36: 'OR',
        37: 'PA',
        38: 'RI',
        39: 'SC',
        40: 'SD',
        41: 'TN',
        42: 'TX',
        43: 'UT',
        44: 'VT',
        45: 'VA',
        46: 'WA',
        47: 'WV',
        48: 'WI',
        49: 'WY'}

    request.session['state2'] = "CA"

    for num, state in state_conv_list.items():
        if 'state1' not in request.session:
            request.session['state1'] = "WA"
        else:
            if state == request.session['state1']:
                state_num1 = num
            if state == request.session['state2']:
                state_num2 = num
            
    state_name1 = "Washington"
    
    for state, abbv in states.items():
        if request.session['state1'] == abbv:
            state_name1 = state
        if (request.session['state2'] == abbv) and (request.session['state2'] != ""):
            state_name2 = state

    print(state_name1, state_name2)

    avg2018 = calc_annual_AVG(2018)
    avg2017 = calc_annual_AVG(2017)
    avg2016 = calc_annual_AVG(2016)
    st1_avg2018 = state_annual_AVG(2018, state_num1)
    st1_avg2017 = state_annual_AVG(2017, state_num1)
    st1_avg2016 = state_annual_AVG(2016, state_num1)
    if ('state2' in request.session) and (request.session['state2'] != ""):    
        st2_avg2018 = state_annual_AVG(2018, state_num2)
        st2_avg2017 = state_annual_AVG(2017, state_num2)
        st2_avg2016 = state_annual_AVG(2016, state_num2)
    
    
    # fig.show()
    sal_map = offline.plot(fig, include_plotlyjs=False, output_type='div')

    years = [datetime.datetime(year=2016, month=1, day=1),
datetime.datetime(year=2017, month=1, day=1),datetime.datetime(year=2018, month=1, day=1)]

    graph = go.Figure()
    graph.add_trace(go.Scatter(
        x=years, y=[st1_avg2016, st1_avg2017, st1_avg2018], name=state_name1))
    graph.add_trace(go.Scatter(
        x=years, y=[avg2016, avg2017, avg2018], name="National Average"))
    graph.update_layout(
        xaxis_range=[datetime.datetime(
            2016, 1, 1), datetime.datetime(2018, 1, 1)],
        autosize=True,
        height=200,
        margin=dict(t=5, b=5, r=5, l=5)
    )

    states = {
        "Alabama": "AL",
        "Alaska": "AK",
        "Arizona": "AZ",
        "Arkansas": "AR",
        "California": "CA",
        "Colorado": "CO",
        "Connecticut": "CT",
        "Delaware": "DE",
        "Florida": "FL",
        "Georgia": "GA",
        "Hawaii": "HI",
        "Idaho": "ID",
        "Illinois": "IL",
        "Indiana": "IN",
        "Iowa": "IA",
        "Kansas": "KS",
        "Kentucky": "KY",
        "Louisiana": "LA",
        "Maine": "ME",
        "Maryland": "MD",
        "Massachusetts": "MA",
        "Michigan": "MI",
        "Minnesota": "MN",
        "Mississippi": "MS",
        "Missouri": "MO",
        "Montana": "MT",
        "Nebraska": "NE",
        "Nevada": "NV",
        "New Hampshire": "NH",
        "New Jersey": "NJ",
        "New Mexico": "NM",
        "New York": "NY",
        "North Carolina": "NC",
        "North Dakota": "ND",
        "Ohio": "OH",
        "Oklahoma": "OK",
        "Oregon": "OR",
        "Pennsylvania": "PA",
        "Rhode Island": "RI",
        "South Carolina": "SC",
        "South Dakota": "SD",
        "Tennessee": "TN",
        "Texas": "TX",
        "Utah": "UT",
        "Vermont": "VT",
        "Virginia": "VA",
        "Washington": "WA",
        "West Virginia": "WV",
        "Wisconsin": "WI",
        "Wyoming": "WY"
    }
    statesNoWA = {
        "Alabama": "AL",
        "Alaska": "AK",
        "Arizona": "AZ",
        "Arkansas": "AR",
        "California": "CA",
        "Colorado": "CO",
        "Connecticut": "CT",
        "Delaware": "DE",
        "Florida": "FL",
        "Georgia": "GA",
        "Hawaii": "HI",
        "Idaho": "ID",
        "Illinois": "IL",
        "Indiana": "IN",
        "Iowa": "IA",
        "Kansas": "KS",
        "Kentucky": "KY",
        "Louisiana": "LA",
        "Maine": "ME",
        "Maryland": "MD",
        "Massachusetts": "MA",
        "Michigan": "MI",
        "Minnesota": "MN",
        "Mississippi": "MS",
        "Missouri": "MO",
        "Montana": "MT",
        "Nebraska": "NE",
        "Nevada": "NV",
        "New Hampshire": "NH",
        "New Jersey": "NJ",
        "New Mexico": "NM",
        "New York": "NY",
        "North Carolina": "NC",
        "North Dakota": "ND",
        "Ohio": "OH",
        "Oklahoma": "OK",
        "Oregon": "OR",
        "Pennsylvania": "PA",
        "Rhode Island": "RI",
        "South Carolina": "SC",
        "South Dakota": "SD",
        "Tennessee": "TN",
        "Texas": "TX",
        "Utah": "UT",
        "Vermont": "VT",
        "Virginia": "VA",
        "West Virginia": "WV",
        "Wisconsin": "WI",
        "Wyoming": "WY"
    }

    line_graph = offline.plot(graph, include_plotlyjs=False, output_type='div')
    line_graph2 = offline.plot(
        graph, include_plotlyjs=False, output_type='div')

    # animals = ['giraffes', 'orangutans', 'monkeys']

    # graph2 = go.Figure(
    #     data=[
    #         go.Bar(name='SF Zoo', x=animals, y=[20, 14, 23]),
    #         go.Bar(name='LA Zoo', x=animals, y=[12, 18, 29])
    #     ])

    # graph2.update_layout(barmode='group')

    # bar_graph = offline.plot(graph2, include_plotlyjs=False, output_type='div')

    context = {
        'map': sal_map,
        'line_graph': line_graph,
        'line_graph2': line_graph2,
        "states": states,
        "statesNoWA": statesNoWA,
        # "bar_graph": bar_graph,
    }
    return render(request, "map/index.html", context)


def test2(request, st1, st2):
    print(st1, st2)
    years = [datetime.datetime(year=2016, month=1, day=1),
            datetime.datetime(year=2017, month=1, day=1),
            datetime.datetime(year=2018, month=1, day=1)]

    graph = go.Figure()
    graph.add_trace(go.Scatter(x=years, y=[80000, 83500, 96000], name="2018"))
    graph.add_trace(go.Scatter(x=years, y=[50000, 63500, 76000], name="2017"))
    graph.update_layout(
        xaxis_range=[datetime.datetime(
            2016, 1, 1), datetime.datetime(2018, 1, 1)],
        autosize=True,
        height=200,
        margin=dict(t=5, b=5, r=5, l=5)
    )

    # states = {
    #     "Alabama": "AL",
    #     "Alaska": "AK",
    #     "Arizona": "AZ",
    #     "Arkansas": "AR",
    #     "California": "CA",
    #     "Colorado": "CO",
    #     "Connecticut": "CT",
    #     "Delaware": "DE",
    #     "Florida": "FL",
    #     "Georgia": "GA",
    #     "Hawaii": "HI",
    #     "Idaho": "ID",
    #     "Illinois": "IL",
    #     "Indiana": "IN",
    #     "Iowa": "IA",
    #     "Kansas": "KS",
    #     "Kentucky": "KY",
    #     "Louisiana": "LA",
    #     "Maine": "ME",
    #     "Maryland": "MD",
    #     "Massachusetts": "MA",
    #     "Michigan": "MI",
    #     "Minnesota": "MN",
    #     "Mississippi": "MS",
    #     "Missouri": "MO",
    #     "Montana": "MT",
    #     "Nebraska": "NE",
    #     "Nevada": "NV",
    #     "New Hampshire": "NH",
    #     "New Jersey": "NJ",
    #     "New Mexico": "NM",
    #     "New York": "NY",
    #     "North Carolina": "NC",
    #     "North Dakota": "ND",
    #     "Ohio": "OH",
    #     "Oklahoma": "OK",
    #     "Oregon": "OR",
    #     "Pennsylvania": "PA",
    #     "Rhode Island": "RI",
    #     "South Carolina": "SC",
    #     "South Dakota": "SD",
    #     "Tennessee": "TN",
    #     "Texas": "TX",
    #     "Utah": "UT",
    #     "Vermont": "VT",
    #     "Virginia": "VA",
    #     "Washington": "WA",
    #     "West Virginia": "WV",
    #     "Wisconsin": "WI",
    #     "Wyoming": "WY"
    # }
    # statesNoWA = {
    #     "Alabama": "AL",
    #     "Alaska": "AK",
    #     "Arizona": "AZ",
    #     "Arkansas": "AR",
    #     "California": "CA",
    #     "Colorado": "CO",
    #     "Connecticut": "CT",
    #     "Delaware": "DE",
    #     "Florida": "FL",
    #     "Georgia": "GA",
    #     "Hawaii": "HI",
    #     "Idaho": "ID",
    #     "Illinois": "IL",
    #     "Indiana": "IN",
    #     "Iowa": "IA",
    #     "Kansas": "KS",
    #     "Kentucky": "KY",
    #     "Louisiana": "LA",
    #     "Maine": "ME",
    #     "Maryland": "MD",
    #     "Massachusetts": "MA",
    #     "Michigan": "MI",
    #     "Minnesota": "MN",
    #     "Mississippi": "MS",
    #     "Missouri": "MO",
    #     "Montana": "MT",
    #     "Nebraska": "NE",
    #     "Nevada": "NV",
    #     "New Hampshire": "NH",
    #     "New Jersey": "NJ",
    #     "New Mexico": "NM",
    #     "New York": "NY",
    #     "North Carolina": "NC",
    #     "North Dakota": "ND",
    #     "Ohio": "OH",
    #     "Oklahoma": "OK",
    #     "Oregon": "OR",
    #     "Pennsylvania": "PA",
    #     "Rhode Island": "RI",
    #     "South Carolina": "SC",
    #     "South Dakota": "SD",
    #     "Tennessee": "TN",
    #     "Texas": "TX",
    #     "Utah": "UT",
    #     "Vermont": "VT",
    #     "Virginia": "VA",
    #     "West Virginia": "WV",
    #     "Wisconsin": "WI",
    #     "Wyoming": "WY"
    # }
    line_graph = drawlineGraph()

    context = {
        'line_graph': line_graph,
    }
    return render(request, "map/test.html", context)


def test(request, st1, st2):
    request.session['state1'] = st1
    request.session['state2'] = st2
    # drawlineGraph()
    return redirect(f'/test2/{st1}/{st2}')

def buildBarChart(st_info1, st_info2, st1_name, st2_name):
    pass
