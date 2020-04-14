import mindre_funktioner as helpFunk
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import ipywidgets as widgets
from IPython.display import display

def diagram_one():

    keywords = ["N15419", "N15505", "N15436"]
    years = [2016,2017,2018,2019]

    rawData = dict()
    for keyword in keywords:
        rawData[keyword] = dict()
        for year in years:
            rawData[keyword][year] = helpFunk.data_series_to_list(keyword, year, specifiedByGender=True)

    scatters = dict()
    for keyword in keywords:
        scatters[keyword] = dict()
        for year in years:
            r = rawData[keyword][year]
            scatters[keyword][year] = go.Scatter(x=r["maleData"],
                                y=r["femaleData"], hovertext=r["mNames"],
                                hoverinfo="text", mode="markers", dx=10, dy=10, name="datapunkter")

    def show(k, y):
        fig = go.Figure()
        fig.add_trace(scatters[k][y])
        if k == "N15505":
            fig.add_shape(type = "line", x0 = 0, y0 = 0, x1 = 340, y1 = 340)
        else:
            fig.add_shape(type = "line", x0 = 0, y0 = 0, x1 = 100, y1 = 100)

        fig.update_layout(
            xaxis = dict(showticklabels=True, showgrid=True, showline=True, ticks='outside'),
            yaxis = dict(showticklabels=True, showgrid=True, showline=True, ticks='outside'),
            hovermode='closest')
        fig.update_traces(mode='markers', marker=dict(symbol='circle', size=4))
        fig.show()

    drop1 = widgets.Dropdown(options=keywords, value="N15419", description = 'Nyckeltal', disabled=False)
    drop2 = widgets.Dropdown(options=years, value=2016, description = 'År', disabled=False)
    w = widgets.interact(show, k = drop1, y = drop2)


def diagram_two():
    parentKeyword, keyword, year = "N15820", "N15572", 2016

    parentDataDict = helpFunk.data_series_to_list(parentKeyword, year)
    dataDict = helpFunk.data_series_to_list(keyword, year)
    parent = parentDataDict["data"]
    data = dataDict["data"]

    if parentDataDict["mNames"] != dataDict["mNames"]:
        print("Fan fel")
        #kommer datan i olika ordning får vi problem
    else:
        municipalityNames = dataDict["mNames"]

    figure = px.scatter(x=parent, y=data, hover_name=municipalityNames,
    title=keyword + " " + helpFunk.keyword_to_description(keyword) + "\n med avseende på " + helpFunk.keyword_to_description(parentKeyword))
    reference_line = px.scatter(x=np.arange(0,101,0.2), y=np.arange(0,101,0.2))
    figure.add_trace(reference_line.data[0])

    figure.show()


def diagram_three():
    posKeyword, negKeyword, kommun, year = "N15574", "N15573", "Stockholm", 2018

    posDataDict = helpFunk.data_series_to_list(posKeyword, year, municipalty = kommun)
    negDataDict = helpFunk.data_series_to_list(negKeyword, year, municipalty = kommun)

    positive = posDataDict["data"]
    positive.extend([28, 20])
    negative = [negDataDict["data"][0]*(-1)]
    negative.extend([-20,-5])

    dots1 = go.Scatter(x=["kommun","SEKOM","rike"], y=positive, mode="markers")
    dots2 = go.Scatter(x=["kommun","SEKOM","rike"], y=negative, mode="markers")
    fig = go.Figure(data=[dots1, dots2])
    fig.show()


def diagram_four():
    keyword, year = "N15574", 2018

    dataDict = helpFunk.data_series_to_list(keyword, year)
    data = dataDict["data"]
    municipalties = dataDict["mNames"]

    fig = go.Figure(data=[go.Bar(y=data, x=municipalties)])
    fig.update_xaxes(showticklabels=False)
    fig.update_layout(title = keyword + ": " + helpFunk.keyword_to_description(keyword) + ", " + str(year))
    fig.show()


def diagram_five():
    keyword, kommun, year = "N15419","Stockholm",2018

    dataDict = helpFunk.data_series_to_list(keyword, year, municipalty = kommun)
    data = dataDict["data"]
    data.extend([40, 50])

    fig = go.Figure(data=[go.Bar(x=["kommun","SEKOM","rike"], y=data)])
    fig.show()

