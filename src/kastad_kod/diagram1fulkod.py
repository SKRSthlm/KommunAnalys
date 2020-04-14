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


def plot_data(keyword, year):
    '''
    plots 290 points each representing a municipality where
    x is male score and y is female score
    keyword is a string
    year is an int or string
    '''
    female = []
    male = []
    municipality_name = []
    year = str(year)
    with open("../data/mdata.txt", "r") as f:
        mdata = json.load(f)

    for k, x in mdata.items():
        gender_data = x[keyword][year]
        female_data = gender_data["K"]
        male_data = gender_data["M"]
        if female_data is not None and male_data is not None:
            female.append(female_data)
            male.append(male_data)
            municipality_name.append(k)
        else:
            pass
            #print("Kommunen " + k + " has None data.")


    figs = px.scatter(x=male, y=female, hover_name=municipality_name,
                      title=keyword + " " + keyword_to_description(keyword))
    figs.show()


def main():
    keywords = ["N15419", "N15505", "N15436"]

    for keyword in keywords:
        plot_data(keyword, 2018)
