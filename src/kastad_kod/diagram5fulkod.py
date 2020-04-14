import plotly.graph_objects as go
import json

def plot_data(keyword, muni, year):
    '''
    plots 290 points each representing a municipality where
    x is male score and y is female score
    keyword is a string
    year is an int or string
    '''

    keyword1_data= []
    year = str(year)
    
    with open("../data/mdata.txt", "r") as f:
        mdata = json.load(f)
    
    school_data = mdata[muni][keyword][year]['T']
    #mock-data för rike och SEKOM
    keyword1_data.append(school_data)
    keyword1_data.append(50)
    keyword1_data.append(65)

    bardiag = go.Bar(y=keyword1_data)
    fig = go.Figure(data=[bardiag])
    fig.show()
