# Detaljerad dokumentation Python
*Uppdaterad 11e juni 2020.*

Här har vi dokumenterat all kod vi skrivit i python för det här projektet. Python används i all kod som hämtar data från KOLADAs API, manipulerar data, skapar diagram, skapar dropdowns och hanterar fel. Läs [här](generell-dok.md) för mer information om hur och var dessa funktioner och metoder används.

Denna sida innehåller följande delar:
* [Funktioner i filen *API_anrop.py*](#funktioner-i-filen-api_anrop)
* [Funktioner i filen *data_funcs.py*](#funktioner-i-filen-data_funcs)
* Funktioner i filen *InformationLog.py*
* Funktioner i filen *diagram_classes.py*
* Funktioner i filen *dropdowns.py*
* Funktioner i filen *main.py*
* Funktioner i filen *plot_funcs.py*

**Här behöver vi ska vi göra om dessa till länkar till respektive rubrik**

[Tillbaka](README.md) till startsidan.

---------------

# Funktioner i filen *API_Anrop*

## YEARS
Konstant, specificerar vilka år som inkluderas i datan från KOLADA. Enbart en sträng med år, separerade med komma-tecken. Åren dyker upp i dropdown-listorna i den ordning de står här.

## NYCKELTAL
Konstant som specificerar vilka nyckeltal som inkluderas i datan från KOLADA. Enbart en sträng med nyckeltal (på formen N12345), separerade med komma-tecken. Se även nyckeltalsbeskrivningarna [här](#).

## write_json_to_file(name, d):
Konverterar d till en JSON-formaterad sträng och skriver detta till en fil med det specificerade namnet. Observera att filen ska vara skapad innan.
#### Returnerar:
Returnerar ingenting, men skriver till specificerad fil.
#### Argumentbeskrivning:

Argument | Beskrivning
-------- | -----------
`name` | En sträng som representerar filnamnet, inklusive filändelse. Om önskat, specificera även relativ filväg till var *API_Anrop* ligger. Ex: "../data/MasterData.txt"
`d` | Ett uppslagsverk (dictionary) med KOLADA-data.

## link_municipalities_to_id()
Hämtar kommunernas ID-nr och deras faktiska namn, och skapar ett uppslagsverk med denna info.
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
Anropar [kolada_call_by_municipality](#kolada_call_by_municipalityid) för varje ID som genereras av [link_municipalities_to_id](#link_municipalities_to_id), samt för rikets ID.
#### Returnerar:
Returnerar två uppslagsverk, ett med kommunnamn som nycklar och alla uppslagsverk med data som data. Det andra är rikets data, strukturerat på samma sätt som ett uppslagsverk från [kolada_call_by_municipality](#kolada_call_by_municipalityid).
#### Argumentbeskrivning:

Argument | Beskrivning
-------- | -----------
`ID_map` | Ett uppslagsverk med kommun-ID:n som nycklar och kommunnamn (strängar) som data.
`country_id`  | En sträng med ID för riket.

---------------

# Funktioner i filen *data_funcs*

## sort_by_fst_list(data_frame, reverse)
Sortera flera listor med avseende på den första givna listan. Ex: [["b","a","c"],[1,2,3]] ger [["a","b","c"],[2,1,3]].
#### Returnerar:
Returnerar listorna, sorterade. Är första listan med tal, sorteras de i storleksordning. Innehåller den istället strängar sorteras de i bokstavsordning. Inget garanterat beteende för listor med blandade typer av element.
#### Argumentbeskrivning:

Argument | Beskrivning
-------- | -----------
`data_frame` | En lista med två eller fler listor av samma längd.
`reverse` | Ett booleskt värde (True, False), som specificera om listan ska sorteras i omvänd ordning (False: växande värden). Standard till False.


## checkYearsOrder(year)
Skapar en ordning av år från konstanten YEARS att leta efter data i. Prioriterar närmast givet år, och hellre mer aktuell data än äldre.
#### Returnerar:
En lista med år som strängar.
Exempel: om input är 2018 och YEARS är "2016,2017,2018,2019", returneras [2018,2019,2017,2016].
#### Argumentbeskrivning:

Argument | Beskrivning
-------- | -----------
`year` | startår, som är sträng eller int

## get_data(keyword, given_year, infoLog, gender)
Genererar data för alla kommuner i Sverige, använder [get_single_data](#get_single_data-keyword-year-infoLog-kommun-gender).

#### Returnerar:
En lista med 290 int/float, med None-värden om data saknas för någon kommun. Saknad data registreras i info-loggen. Datan är sorterad i bokstavsordning för kommunernas namn, så på index 0 finns data för kommunen Ale, på index 289 finns data för kommunen Övertorneå.
Om data saknas för **alla** kommuner det givna året, väljs data från närmsta år det finns data ifrån. Mer om ordningen på hur
åren prioriteras i [checkYearsOrder](#checkyearsorderyear). Hämtas data från annat år dokumenteras även detta i info-loggen.
#### Argumentbeskrivning:

Argument | Beskrivning
-------- | -----------
`keyword` | Specificera ett nyckeltal som sträng. Ska finnas i konstanten [NYCKELTAL](#nyckeltal)
`given_year` | Specificera året som sträng. Ska finnas i konstanten [YEARS](#years). Se ovan för detaljer om data saknas för detta år.
`infoLog` | En instans av klassen InformationLog. Loggar information till användarmeddelanden.
`gender` | Kan utelämnas eller specificeras som "T", då hämtas data för alla elever i kommunen. Sätt annars till "K" respektive "M" för medel hos enbart flickor respektive pojkar.

## get_single_data(keyword, year, infoLog, kommun, gender)
Genererar data för en given kommun eller riket som helhet, baserat på ett nyckeltal, ett år och eventuellt ett kön.
#### Returnerar:
Returnerar ett hel- eller flyttal, eller None om data saknas. Se informationsloggen för mer info om saknad data.
#### Argumentbeskrivning:

Argument | Beskrivning
-------- | -----------
`keyword` | Specificera ett nyckeltal som sträng. Ska finnas i konstanten [NYCKELTAL](#nyckeltal)
`given_year` | Specificera året som sträng. Ska finnas i konstanten [YEARS](#years).
`infoLog` | En instans av klassen InformationLog. Loggar information till användarmeddelanden.
`kommun`  | Ett kommunnamn som sträng, ex. "Arjeplog". Om detta utelämnas returneras rikets snitt.
`gender` | Kan utelämnas eller specificeras som "T", då hämtas data för alla elever i kommunen. Sätt annars till "K" respektive "M" för kommunens/rikets medel hos enbart flickor respektive pojkar.

## calc_sekom_avg(keyword, year, given_kommun, infoLog, gender)
Beräknar ett (oviktat) medelvärde för den SEKOM-grupp som given kommun tillhör, för givet nyckeltal och år. Dokumenterar information i infologgen.
#### Returnerar:
Returnerar ett flyttal med en decimal, eller None om data saknas för alla kommuner det året+nyckeltalet.
#### Argumentbeskrivning:

Argument | Beskrivning
-------- | -----------
`keyword` | Specificera ett nyckeltal som sträng. Ska finnas i konstanten [NYCKELTAL](#nyckeltal)
`year` | Specificera året som sträng. Ska finnas i konstanten [YEARS](#years).
`given_kommun`  | Ett kommunnamn som sträng, ex. "Arjeplog".
`infoLog` | En instans av klassen InformationLog. Loggar information till användarmeddelanden.
`gender` | Kan utelämnas eller specificeras som "T", då hämtas data för alla elever i kommunen. Sätt annars till "K" respektive "M" för kommunens/rikets medel hos enbart flickor respektive pojkar.

## get_comparison_list(keyword, given_year, kommun, infoLog)
Hämtar data för stapeldiagrammen med tre staplar - en för kommunen, en för SEKOM-snittet och en för rikssnittet. Dokumenterar saknad data i infologgen.
#### Returnerar:
Returnerar en lista med tre hel- eller flyttal. Första elementet är värdet för kommunen det givna nyckeltalet och året. Det andra elementet snittet i SEKOM-gruppen kommunen tillhör. Tredje elementet är rikssnittet. Om ett, två eller tre av värdena saknas, hämtas data från närmsta möjliga år (se [checkYearsOrder](#checkyearsorderyear)).
#### Argumentbeskrivning:

Argument | Beskrivning
-------- | -----------
`keyword` | Specificera ett nyckeltal som sträng. Ska finnas i konstanten [NYCKELTAL](#nyckeltal)
`given_year` | Specificera året som sträng. Ska finnas i konstanten [YEARS](#years).
`kommun`  | Ett kommunnamn som sträng, ex. "Arjeplog".
`infoLog` | En instans av klassen InformationLog. Loggar information till användarmeddelanden.

## get_all_municipalities()
Hämtar alla kommuner i Sverige.
#### Returnerar:
En lista med de 290 kommunnamnen, sorterade alfabetiskt.
#### Argumentbeskrivning:
Inga argument.

## normalize_data(kommuner, data_x, data_y)
Tar bort None-värden från en eller två givna listor, samt motsvarande värden från de andra listorna.
#### Returnerar:
Givna listor, utan None-värden. Utesluts `data_y` returneras ingen tredje lista.  
Ex: om data_x har ett None-värde på index 10, tar funktionen bort datan på den positionen i de andra två listorna, samt None-värdet i data_x. Hanterar inte None-värden i listan med kommunnamn.
Ex: [1,2,None,4] och ['a',None,'c','d'] som data_x respektive data_y skulle returnera (..., [1,4], ['a','d']).
#### Argumentbeskrivning:

Argument | Beskrivning
-------- | -----------
`kommuner` | En lista med kommunnamn.
`data_x`  | En lista med numeriska värden motsvarande kommunerna i `kommuner` indexvis.
`data_y`  | En lista med numeriska värden motsvarande kommunerna i `kommuner` indexvis. Detta argument kan uteslutas helt.

## filter_on_sekom(given_kommun, kommuner, data_x, data_y)
Givet en kommun och två eller tre listor (en med kommunnamn, en/två med värden), sorterar denna funktion ut värden och kommuner som tillhör samma SEKOM-grupp som den givna kommunen.
#### Returnerar:
Returnerar förkortade listor, utan de kommuner och motsvarande värden som inte ligger i samma SEKOM-grupp.
#### Argumentbeskrivning:

Argument | Beskrivning
-------- | -----------
`given_kommun`  | Ett kommunnamn som sträng.
`kommuner` | En lista med kommunnamn.
`data_x`  | En lista med numeriska värden motsvarande kommunerna i `kommuner` indexvis.
`data_y`  | En lista med numeriska värden motsvarande kommunerna i `kommuner` indexvis. Detta argument kan uteslutas helt.

## move_to_last(given_kommun, kommuner, data_x, data_y)
Given en kommun och två eller tre listor, flyttar denna funktion kommunens namn samt motsvarande data till sist i respektive lista. Förutsätter att listorna har samma längd. Används för att se till att en highlightad kommun i en scatter-plot renderas sist.
#### Returnerar:
Returnerar samma listor, men given kommun sist.
#### Argumentbeskrivning:

Argument | Beskrivning
-------- | -----------
`given_kommun`  | Ett kommunnamn som sträng, den kommun som ska flyttas.
`kommuner` | En lista med kommunnamn.
`data_x`  | En lista med numeriska värden motsvarande kommunerna i `kommuner` indexvis.
`data_y`  | En lista med numeriska värden motsvarande kommunerna i `kommuner` indexvis. Detta argument kan uteslutas helt.

## create_list_of_colors(kommuner, infoLog, std_col, hgl_col, kommun)
Creates and returns a list of colors for data points. Will return a list of the same length as kommuner, consisting of the color std_col. The corresponding position of kommun in kommuner is highlighted with the hgl_col.
Skapar en lista med färger för datapukter, som används för att specificera färger i plottar.
#### Returnerar:
Returnerar en lista med samma längd som `kommuner`, som består av färgen `std_col`. Motsvarande position av `kommun` i listan är highlightad med `hgl_col`.
#### Argumentbeskrivning:

Argument | Beskrivning
-------- | -----------
`kommuner` | En lista med kommunnamn.
`infoLog` | En instans av klassen InformationLog. Loggar information till användarmeddelanden.
`std_col` | En CSS-färg eller HEX-kod som sträng
`hgl_col` | En CSS-färg eller HEX-kod som sträng
`kommun`  | Ett kommunnamn som sträng, om None highlightas ingen position i listan.

## no_per_sekom(kommun)
Returnerar antalet kommuner som tillhör den SEKOM-grupp kommunen tillhör. Ger ett Keyerror om kommunnamnet är felaktigt.
#### Returnerar:
Antalet kommuner (heltal).
#### Argumentbeskrivning:

Argument | Beskrivning
-------- | -----------
`kommun`  | Ett kommunnamn som sträng.

## round_values(args...)
Tar ett valfritt antal listor med flyttal och avrundar dessa till heltal.
#### Returnerar:
Samma lista, med avrundade flyttal. Avrundar x.5 uppåt. Om det finns något None-värde i listan returneras listan utan några avrundningar.
#### Argumentbeskrivning:

Argument | Beskrivning
-------- | -----------
`args` | Vilket antal listor som helst. Funktionen är testad för en, två och tre listor som input.


## MALL funktionsNamn(arg1, ..., argN)
Beskrivning. Inkludera funktion, samt eventuellt "särbeteende".
#### Returnerar:
Beskriv vad funktionen returnerar. Beskriv specialfall. Eventuellt ett exempel, om rimligt/hjälpsamt.
#### Argumentbeskrivning:

Argument | Beskrivning
-------- | -----------
`argumentNamn` | Beskrivning. Inkludera typ (sträng, int, ...), samt eventuella ytterligare krav.


[Tillbaka](README.md) till startsidan.
