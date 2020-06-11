# Detaljerad dokumentation Python
*Uppdaterad 21e maj 2020.*

Här har vi dokumenterat all kod vi skrivit i python för det här projektet. Python används i all kod som hämtar data från KOLADAs API, manipulerar data, skapar diagram, skapar dropdowns och hanterar fel. Läs [här](generell-dok.md) för mer information om hur och var dessa funktioner och metoder används.

Denna sida innehåller följande delar:
* [Funktioner i filen *API_anrop.py*](#funktionerifilenapi_anrop)
* [Funktioner i filen *data_funcs.py*](#funktionerifilendata_funcs)
* Funktioner i filen *InformationLog.py*
* Funktioner i filen *diagram_classes.py*
* Funktioner i filen *dropdowns.py*
* Funktioner i filen *main.py*
* Funktioner i filen *plot_funcs.py*

**Här behöver vi ska vi göra om dessa till länkar till respektive rubrik**

[Tillbaka](README.md) till startsidan.

# Funktioner i filen *API_Anrop*

## YEARS
Konstant, specificerar vilka år som inkluderas i datan från KOLADA. Enbart en sträng med år, separerade med komma-tecken. Åren dyker upp i dropdown-listorna i den ordning de står här.

## NYCKELTAL
Konstant som specificerar vilka nyckeltal som inkluderas i datan från KOLADA. Enbart en sträng med nyckeltal (på formen N12345), separerade med komma-tecken. Se även nyckeltalsbeskrivningarna [här](#).

## write_json_to_file(name, d):
Konverterar d till en JSON-formatterad sträng och skriver detta till en fil med det specificerarde namnet. Observera att filen ska vara skapad innan.
#### Returnerar:
Returnerar ingenting, men skriver till specificerad fil.
#### Argumentbeskrivning:

Argument | Beskrivning
-------- | -----------
`name` | En sträng som representerar filnamnet, inklusive filändelse. Om önskat, specificera även relativ filväg till var *API_Anrop* ligger. Ex: "../data/MasterData.txt"
`d` | Ett uppslagsverk (dictionary) med KOLADA-data.


## link_municipalities_to_id()
Hämtar kommunernas ID-nr och deras faktiska namn, och skapar ett uppslagsverk med denna info.
Return: a python dictionary over this mapping, as well as the id-number for the whole country as a string.
#### Returnerar:
Returnerar ett uppslagsverk med kommun-ID:n som nycklar och kommunnamn som värden, samt ID:t för riksdata.
#### Argumentbeskrivning:
Inga argument.

## kolada_call_by_municipality(ID)
Hämtar all data från KOLADA för nyckeltalen i NYCKELTAL per år i YEARS, för en given kommun.
Return: A dictionary linking each combination of key figure and year to a unique value.
#### Returnerar:
Returnerar ett uppslagsverk av nästlade uppslagsverk. Nycklar i nivå ett är nyckeltalskoder, därefter år, och sist kön('K','M','T') vilket ger datan för det året.
#### Argumentbeskrivning:

Argument | Beskrivning
-------- | -----------
`ID` | ID-nr för en kommun i Sverige.


## all_kolada_calls(ID_map, country_id)
Anropar [kolada_call_by_municipality](#koladacallbymunicipality) för varje ID som genereras av [link_municipalities_to_id](#linkmunicipalitiestoid), samt för rikets ID.
#### Returnerar:
Returnerar två uppslagsverk, ett med kommunnamn som nycklar och alla uppslagsverk med data som data. Det andra är rikets data, strukturerat på samma sätt som ett uppslagsverk från [kolada_call_by_municipality](#koladacallbymunicipality).
#### Argumentbeskrivning:

Argument | Beskrivning
-------- | -----------
`ID_map` | Ett uppslagsverk med kommun-ID:n som nycklar och kommunnamn (strängar) som data.
`country_id`  | En sträng med ID för riket.


# Funktioner i filen *data_funcs*


## get_data(keyword, given_year, infoLog, gender)
Genererar data för alla kommuner i Sverige.

#### Returnerar:
En lista med 290 int/float, med None-värden om data saknas för någon kommun. Saknad data registreras i info-loggen. Datan är sorterad i bokstavsordning för kommunernas namn, så på index 0 finns data för kommunen Ale, på index 289 finns data för kommunen Övertorneå.
Om data saknas för **alla** kommuner det givna året, väljs data från närmsta år det finns data ifrån. Mer om ordningen på hur
åren prioriteras i [checkYearsOrder](#checkyearsorderyear). Hämtas data från annat år dokumenteras även detta i info-loggen.
#### Argumentbeskrivning:

Argument | Beskrivning
-------- | -----------
`keyword` | Specifiera ett nyckeltal som sträng. Ska finnas i konstanten NYCKELTAL
`given_year` | Specifiera året som sträng. Se ovan för detaljer om data saknas för detta år.
`infoLog` | En instans av klassen InformationLog. Loggar information till användarmeddelanden.
`gender` | Kan utelämnas eller specificeras som "T", då hämtas data för alla elever i kommunen. Sätt annars till "K" respektive "M" för medel hos enbart flickor respektive pojkar.

## checkYearsOrder(year)
Skapar en ordning av år från konstanten YEARS att leta efter data i. Prioriterar närmast givet år, och hellre mer aktuell data än äldre.
#### Returnerar:
En lista med år som strängar.
Exempel: om input är 2018 och YEARS är "2016,2017,2018,2019", returneras [2018,2019,2017,2016].
#### Argumentbeskrivning:

Argument | Beskrivning
-------- | -----------
`year` | startår, som är sträng eller int

## MALL funktionsNamn(arg1, ..., argN)
Beskrivning. Inkludera funktion, samt eventuellt "särbeteende".
#### Returnerar:
Beskriv vad funktionen returnerar. Beskriv specialfall. Eventuellt ett exempel, om rimligt/hjälpsamt.
#### Argumentbeskrivning:

Argument | Beskrivning
-------- | -----------
`argumentNamn` | Beskrivning. Inkludera typ (sträng, int, ...), samt eventuella ytterligare krav.


[Tillbaka](README.md) till startsidan.
