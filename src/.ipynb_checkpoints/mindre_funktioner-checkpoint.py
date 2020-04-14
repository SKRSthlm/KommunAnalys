
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

def data_series_to_list(keyword, year, municipalty = None, specifiedByGender = False):
    '''
    keyword is a string representing Kolada's keyword code e.g. "N12345"
    year is an int or string
    municipalty is a string. First letter capital e.g. "Stockholm"
    specifiedByGender is a bool
    
    returns dict with two keys: data and mNames. data refers to list with data from Kolada specified by keyword and year for all municipalties where data exists. mNames refers to list with municipalty names' in the same order as the data list.
    if municipalty is entered, list with only this data is returned
    if no data exist, empty lists are returned
    if specifiedByGender is True, the data-key is replaced by femaleData and maleData. mNames as earlier
    '''
    
    import json
    if specifiedByGender:
        femaleRetData, maleRetData = [], []
    else:
        retData = []
    
    municipalityNames = []
    year = str(year)
    
    with open("../data/MasterData.txt", "r") as f:
        #CHANGE TO MasterData WHEN UPDATED WITH NAMES INSTEAD OF CODES
        allData = json.load(f) 
    
    def inner_repeated_if():
        if specifiedByGender:
            femaleNum = dataDict[keyword][year]["K"]
            maleNum = dataDict[keyword][year]["M"]
            if femaleNum is not None and maleNum is not None:
                femaleRetData.append(femaleNum)
                maleRetData.append(maleNum)
                municipalityNames.append(munName)
        else:
            number = dataDict[keyword][year]['T']
            if number is not None:
                retData.append(number)
                municipalityNames.append(munName)
    
    if municipalty is None:
        for munName, dataDict in allData.items():
            inner_repeated_if()
    else:
        munName = municipalty
        dataDict = allData[munName]
        inner_repeated_if()
        
    if specifiedByGender:
        return {"femaleData":femaleRetData, "maleData":maleRetData, "mNames":municipalityNames}
    else:
        return {"data":retData, "mNames":municipalityNames}
        
    
