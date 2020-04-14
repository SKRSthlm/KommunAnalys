import plotly.graph_objects as go
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
    plots 290 bar charts each representing a municipality where
    x is municipality_name and y>0 is percentage of people getting
    higher grade than what they got on tests.
    keyword is a string
    year is an int or string
    '''

    municipality_name = []  # x-axis
    school_data = []  # y-axis , above
    year = str(year)
    with open("../data/mdata.txt", "r") as f:
        mdata = json.load(f)

    for k, x in mdata.items():
        keyword_data = x[keyword][year]['T']
        if keyword_data is not None:
            school_data.append(keyword_data)
            municipality_name.append(k)
        # else:
            # print("Kommunen " + k + " has None data.")


    fig = go.Figure([go.Bar(x=municipality_name, y=school_data)])
    fig.update_layout(title=keyword + " "
                      + keyword_to_description(keyword)
                      + " " + year)
    fig.show()


def main():
    # Vilka nyckeord funkar för detta?
    '''
    "N15573": "Elever i år 9 som fått ett lägre betyg än provbetyg för ämnesprov i engelska, kommunala skolor, andel (%)",
    "N15572": "Elever i år 9 som fått ett högre betyg än provbetyg för ämnesprov i matematik, kommunala skolor, andel (%)",
    "N15571": "Elever i år 9 som fått ett lägre betyg än provbetyg för ämnesprov i matematik, kommunala skolor, andel (%)",
    "N15570": "Elever i år 9 som fått ett högre betyg än provbetyg för ämnesprov i svenska, kommunala skolor, andel (%)",
    "N15569": "Elever i år 9 som fått ett lägre betyg än provbetyg för ämnesprov i svenska, kommunala skolor, andel (%)",
    '''
    # 'Lägre betyg än' data ska vara under y axeln och 'Högre betyg än' data
    # ska vara över x axeln. Vissa Nyckeltal hör ihop. Vilka?
    matching_keywords = [("N15570", "N15569"), ("N15572", "N15571")]
    keywords = ["N15573", "N15572", "N15571", "N15570", "N15569"]
    plot_data("N15570", 2016)


if __name__ == "__main__":
    main()

