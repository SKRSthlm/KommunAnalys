import plotly.graph_objects as go
import json

def plot_data(keyword1, keyword2, muni, year):
    '''
    plots 290 points each representing a municipality where
    x is male score and y is female score
    keyword is a string
    year is an int or string
    '''

    keyword1_data= []
    keyword2_data= []
    year = str(year)
    
    with open("../data/mdata.txt", "r") as f:
        mdata = json.load(f)
    
    pos_data = mdata[muni][keyword1][year]['T']
    neg_data = -mdata[muni][keyword2][year]['T']
    #mock-data för rike och SEKOM
    keyword1_data.append(pos_data)
    keyword1_data.append(50)
    keyword1_data.append(65)
    
    keyword2_data.append(neg_data)
    keyword2_data.append(-30)
    keyword2_data.append(-25)
    
    dots1 = go.Scatter(x=[1,2,3], y=keyword1_data, mode="markers")
    dots2 = go.Scatter(x=[1,2,3], y=keyword2_data, mode="markers")
    fig = go.Figure(data=[dots1, dots2])
    fig.show()
