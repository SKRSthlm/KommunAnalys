import mindre_funktioner as helpFunk
import plotly.express as px
import plotly.graph_objects as go

def diagram_one():
    keyword, year = "N15419", 2018
    
    rawDataDict = helpFunk.data_series_to_list(keyword, year, specifiedByGender = True)
    males = rawDataDict["maleData"]
    females = rawDataDict["femaleData"]
    municipalityNames = rawDataDict["mNames"]
    
    figure = px.scatter(x=males, y=females, hover_name=municipalityNames,
                      title=keyword + " " + helpFunk.keyword_to_description(keyword))
    figure.show()

    
def diagram_two():
    parentKeyword, keyword, year = "N15820", "N15505", 2018
    
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
                      title=keyword + " " + helpFunk.keyword_to_description(keyword))
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
    fig.show()

    
def diagram_five():
    keyword, kommun, year = "N15419","Stockholm",2018
    
    dataDict = helpFunk.data_series_to_list(keyword, year, municipalty = kommun)
    data = dataDict["data"]
    data.extend([40, 50])
    
    fig = go.Figure(data=[go.Bar(x=["kommun","SEKOM","rike"], y=data)])
    fig.show()