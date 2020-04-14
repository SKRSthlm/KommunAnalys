import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import json


def keyword_to_description(keyword):
    keyword_to_description = {
        "N15419": "Elever i år 9 som uppnått kunskapskraven i alla ämnen, kommunala skolor, andel (%)",
        "N15505": "Elever i åk. 9, meritvärde kommunala skolor, genomsnitt (17 ämnen)",
        "N15436": "Elever i åk 9 som är behöriga till yrkesprogram, kommunala skolor, andel (%)",
        "U15461": "Elever i år 9 som är behöriga till yrkespr. avvikelse från modellberäknat värde kommunala skolor, procentenheter",
        "N15485": "Elever i åk 6 med lägst betyget E i matematik, kommunala skolor, andel (%)",
        "N15488": "Elever i åk 6 med lägst betyget E i svenska, kommunala skolor, andel (%)",
        "N15574": "Elever i år 9 som fått ett högre betyg än provbetyg för ämnesprov i engelska, kommunala skolor, andel (%)",
        "N15573": "Elever i år 9 som fått ett lägre betyg än provbetyg för ämnesprov i engelska, kommunala skolor, andel (%)",
        "N15572": "Elever i år 9 som fått ett högre betyg än provbetyg för ämnesprov i matematik, kommunala skolor, andel (%)",
        "N15571": "Elever i år 9 som fått ett lägre betyg än provbetyg för ämnesprov i matematik, kommunala skolor, andel (%)",
        "N15570": "Elever i år 9 som fått ett högre betyg än provbetyg för ämnesprov i svenska, kommunala skolor, andel (%)",
        "N15569": "Elever i år 9 som fått ett lägre betyg än provbetyg för ämnesprov i svenska, kommunala skolor, andel (%)",
        "N15814": "Lärare (heltidstjänster) med lärarlegitimation och behörighet i minst ett ämne i grundskola åk 1-9, kommunala skolor, andel (%)",
        "N15034": "Elever/lärare (årsarbetare) i kommunal grundskola åk 1-9, lägeskommun, antal",
        "N15008": "Kostnad för kommunal grundskola åk 1-9, kr/elev",
        "N15902": "Nyinvandrade och elever med okänd bakgrund i kommunal grundskola åk. 1-9, andel (%)",
        "N15823": "Nyinvandrade och elever med okänd bakgrund i år 9, kommunala skolor, andel (%)",
        "N15820": "Elever vars föräldrar har eftergymnasial utbildning, åk 1-9 i kommunal grundskola, lägeskommun, andel (%)"
    }
    return keyword_to_description[keyword]


def plot_data(keyword_1, keyword_2, year):
    '''
    plots 290 points each representing a municipality where
    x is male score and y is female score
    keyword is a string
    year is an int or string
    '''

    keyword1_data= []
    keyword2_data= []
    municipality_name = []
    year = str(year)
    with open("../data/mdata.txt", "r") as f:
        mdata = json.load(f)

    for k, x in mdata.items():
        school_data = x[keyword_1][year]['T']
        parent_data = x[keyword_2][year]['T']
        if school_data is not None and parent_data is not None:
            keyword1_data.append(school_data)
            keyword2_data.append(parent_data)
            municipality_name.append(k)
        else:
            pass
            #print("Kommunen " + k + " has None data.")


    figs = px.scatter(x=keyword2_data, y=keyword1_data, hover_name=municipality_name,
                      title=keyword_1 + " " + keyword_to_description(keyword_1))
    figs.show()


#def main():
 #   keywords = ["N15419", "N15505", "N15436"]

  #  for keyword in keywords:
   #     plot_data([keyword,"N15820"], 2018)