# Detaljerad dokumentation Python
*Uppdaterad 21e maj 2020.*

Här har vi dokumenterat all kod vi skrivit i python för det här projektet. Python används i all kod som hämtar data från KOLADAs API, manipulerar data, skapar diagram, skapar dropdowns och hanterar fel. Läs [här](generell-dok.md) för mer information om hur och var dessa funktioner och metoder används.

Denna sida innehåller följande delar:
* Funktioner i filen *API_anrop.py*
* [Funktioner i filen *data_funcs.py*](#funktionerifilendatafuncspy)
* Funktioner i filen *InformationLog.py*
* Funktioner i filen *diagram_classes.py*
* Funktioner i filen *dropdowns.py*
* Funktioner i filen *main.py*
* Funktioner i filen *plot_funcs.py*

**Här behöver vi ska vi göra om dessa till länkar till respektive rubrik**

[Tillbaka](README.md) till övrigt innehåll.

# Funktioner i filen *data_funcs.py*

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
