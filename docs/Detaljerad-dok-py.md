# Detaljerad dokumentation Python
*Uppdaterad 11e juni 2020.*

Här har vi dokumenterat all kod vi skrivit i python för det här projektet. Python används i all kod som hämtar data från KOLADAs API, manipulerar data, skapar diagram, skapar dropdowns och hanterar fel. Läs [här](generell-dok.md) för mer information om hur och var dessa funktioner och metoder används.

Denna sida innehåller följande delar:
* [Funktioner i filen *API_anrop.py*](#funktioner-i-filen-api_anrop)
* [Funktioner i filen *data_funcs.py*](#funktioner-i-filen-data_funcs)
* [Funktioner i filen *InformationLog.py*](#funktioner-i-filen-informationlog)
* [Funktioner i filen *plot_funcs.py*](#funktioner-i-filen-plot_funcs)
* [Funktioner i filen *dropdowns.py*](#funktioner-i-filen-dropdowns)
* [Funktioner i filen *diagram_classes.py*](#funktioner-i-filen-diagram_classes)
* Funktioner i filen *main.py*

**Här behöver vi ska vi göra om dessa till länkar till respektive rubrik**

[Tillbaka](README.md) till startsidan.

----

# Funktioner i filen *API_Anrop*

## YEARS
Konstant, specificerar vilka år som inkluderas i datan från KOLADA. Enbart en sträng med år, separerade med komma-tecken. Åren dyker upp i dropdown-listorna i den ordning de står här.

## NYCKELTAL
Konstant som specificerar vilka nyckeltal som inkluderas i datan från KOLADA. Enbart en sträng med nyckeltal (på formen N12345), separerade med komma-tecken. Se även nyckeltalsbeskrivningarna [här](#globala-uppslagsverk).

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

----

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
`years` | Endast för testning, skriver över konstanten YEARS.

## get_data(keyword, given_year, infoLog, gender)
Genererar data för alla kommuner i Sverige, använder [get_single_data](#get_single_datakeyword-year-infolog-kommun-gender).

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



----

# Funktioner i filen *InformationLog*

## init()
Initierar en instans av en infologg. Skapar bara ett privat uppslagsverk.
#### Returnerar:
Instansen.
#### Argumentbeskrivning:
Inga argument.

## addInfo(kwargs...)
Lägg till data för användarmeddelanden.
#### Returnerar:
Returnerar ingenting.
#### Argumentbeskrivning:
Lägg till valfritt antal argument som infoNyckel=info (se konceptet \*\*kwargs i python). Om en nyckel som inte finns i listan nedan ges, kommer funktionen att ge ett felmeddelande.

Argument dvs info-nyckel | Beskrivning
-------- | -----------
`missingMunis`="kommunnamn" | Specificera en kommun som sträng för att indikera att denna kommun inte renderas i plotten (eftersom det saknas data).
`missingData`=("nyckeltal", år) | Specificera en tupel (ett par) där första elementet är en nyckeltalskod från [NYCKELTAL](#nyckeltal) som sträng och det andra elementet ett år från [YEARS](#years). Indikerar att data för alla kommuner saknas för det här året+nyckeltalet. Kan specificeras flera gånger, då håller loggen koll på att det saknas för flera år.
`succeededYears`=("nyckeltal", år) | Specificera en tupel som ovan för att indikera att data lyckades hämtas för minst en kommun det givna året+nyckeltalet. Om denna specificeras igen för samma nyckeltal, skrivs året över.
`sekomCol` = "färg"  | En sträng som sparar vilken SEKOM-grupp data har filtrerats från.
`actualQty` = ("keyword", int) | En tupel där första elementet är en nyckeltalskod från [NYCKELTAL](#nyckeltal) och andra elementet ett heltal som motsvarar det faktiska antalet datapunkter som tagits med i plotten (dvs 1-290st).
`expectedTot` = int | Ett heltal som representerar det antal datapunkter som förväntas plottas. Oftast 290st kommmuner, men ibland något mindre tal (eftersom vi ibland filtrerar på SEKOM-grupp).
`showSekomAvg` = bool | Ett booleskt värde. Om True, kommer sekommedel att visas när [informUser()](#informuserargs-kommun) anropas.

## informUser(args..., kommun)
Skriver ut användarmeddelanden till stdOut.
#### Returnerar:
Ingenting, utom användarmeddelanden.
#### Argumentbeskrivning:
Lägg till valfritt antal argument som strängar, se tabellen. Specificera kommun="kommunnamn" sist, om du vill ha med detta. Om `kommun` är något annat än None eller False, letar funktionen efter given sträng i `missingMunis`, och skriver ut information om enbart denna kommun. Om inget hittas, utesluts meddelande.
Är `kommun` istället None, eller helt utesluts, listas inga element från missingMunis.
Är `kommun` istället False, skrivs alla element från missingMunis ut.

Om `actualQty` har flera nycklar, skrivs dessa efter varandra.

Använder du någon annan nyckel än nedan, kommer metoden ge ett felmeddelande.
Rekommenderat att alltid specificera `missingData` och `succeededYears` tillsammans.
Rekommenderat att alltid specificera `actualQty` och `expectedTot` tillsammans.

Specificera argumenten i samma ordning du önskar ha felmeddelandena utskrivna.

Argument | Användarmeddelande
-------- | -----------
`missingMunis` | "Data saknas för kommunen X." alternativt "Data saknas för kommunerna X,Y,..."
`missingData` | "Relevant data saknas för nyckeltalet X år Y."
`succeededYears` | "Visar istället data för nyckeltalet X år Y."
`sekomCol` | "Visar kommuner från FÄRG kommungrupp." — men bara om `showSekomAvg` inte är med som argument.
`actualQty` | "Visar data från X kommuner." om `expectedTot` inte är med som argument.
`expectedTot` | Utan `actualQty` skrivs inget ut. Med denna: "Visar data från X av Y kommuner."
`showSekomAvg` | "Oviktat medelvärde för nyckeltal N i FÄRG kommungrupp baserat på data från X av Y kommuner."

## resetMissingMunis()
Tömmer minnet på kommuner det saknas data för.
#### Returnerar:
Ingenting.
#### Argumentbeskrivning:
Inga argument.

## reset()
Tömmer minnet på all information. Används främst i olika tester.
#### Returnerar:
Ingenting.
#### Argumentbeskrivning:
Inga argument.



----

# Funktioner i filen *plot_funcs*

## Globala uppslagsverk
I *plot_funcs* laddas data in från filer till olika variabler som används på flera ställen.

Variabel  | Beskrivning
-------   | ----------
`mdata` | All data på kommunnivå, från filen *MasterData.txt*. Se även [API_Anrop](#funktioner-i-filen-api_anrop).
`riket_data` | All data på riksnivå, från filen *riket.txt*. Se även [API_Anrop](#funktioner-i-filen-api_anrop).
`sekom_data` | Vilka SEKOM-grupper alla kommuner tillhör, från filen *sekom.json*. Kommunnamn som nycklar, SEKOM-gruppfärg som data.
`key_to_desc` | Nyckeltalskoder som nycklar, strängar med nyckeltalsbeskrivningar som data. Används på diverse platser, tex etiketter på plottar. Behöver uppdateras manuellt när ett nyckeltal läggs till.
`desc_to_key`| `key_to_desc` i omvänd ordning, dvs nycklar och data har bytt plats.

## *Följande beskrivningar specificerar metoder för Plot-klassen*

## init()
Instansierar en instans av plotlys Figure-klass. Inga argument.

## clear()
Tömmer instansens diagram-yta och "glömmer" alla inställningar, dataserier och grafiska element. Inga argument.

## show()
Renderar dataserier och grafiska element med givna inställningar i en diagram-yta. Inga argument.

## plot_line(x_0, y_0, x_1, y_1, col, line_width, line_type)
Skapar en linje att rita på diagramytan.
#### Returnerar:
Ingenting.
#### Argumentbeskrivning:

Argument | Beskrivning
-------- | -----------
`x_0` & `y_0` | Startpunkt
`x_1` & `y_1` | Ändpunkt
`col` | En CSS-färg eller HEXkod som sträng. Standard är CSS "black".
`line_width`| Linjens tjocklek i pixlar. Standard är 1px.
`line_type`| En av “solid”, “dot” eller “dashdot”. Standard "solid".

## add_def(Diagram,RikeAvg):
Skriver ut "lådor" med text på diagramytan. Skrev aldrig om till en bättre, generell funktion.
#### Returnerar:
Ingenting.
#### Argumentbeskrivning:

Argument | Beskrivning
-------- | -----------
`Diagram` | True eller False. Om True visas "Den sträckade linjen visar rikets medel: X %". Om False visas "Flickor har högre resultat än pojkar" respektive "Pojkar har högre resultat än flickor".
`RikeAvg` | X:et i rikets medel ovan.

## add_scatter(data_x, data_y, data_text, colors, xlabel, ylabel)
Skapar en scatter-plot-serie att rendera.
#### Returnerar:
Inget.
#### Argumentbeskrivning:

Argument | Beskrivning
-------- | -----------
`data_x` | En lista med data plottad längst x-axeln (tänk på detta som punkternas x-koordinat)
`data_y` | En lista med data plottad längst y-axeln (tänk på detta som punkternas y-koordinat)
`data_text` | En lista med strängar som ska visas som fetstilad rubrik i hover-etiketten.
`colors` | En lista med strängar, representerar vilken färg respektive datapunkt ska ha.
`xlabel` | Sträng som visas i hover-etiketten, innan x-värdet
`ylabel` | Sträng som visas i hover-etiketten, innan y-värdet

## add_bar(data_x, data_y, colors, x_ticks, text, show_legend, legend_name)
Skapar en bar-plot-serie att rendera.
#### Returnerar:
Inget.
#### Argumentbeskrivning:

Argument | Beskrivning
-------- | -----------
`data_x` | En lista med data plottad längst x-axeln (tänk på detta som staplarnas namn)
`data_y` | En lista med data plottad längst y-axeln (tänk på detta som staplarnas höjd)
`colors` | En lista med strängar, representerar vilken färg respektive stapel ska ha.
`x_ticks` | Booleskt värde för att visa markörer längst x-axeln. Standard är False.
`text` | En lista med strängar som ska visas som fetstilad rubrik i hover-etiketten, standard är en tom sträng.
`show_legend` | Booelskt värde för att visa legend, dvs rutan som visar vilken dataserie som är vilken. Standard är False.
`legend_name` | En sträng som visas som dataseriens rubrik i legend-rutan. Standard är en tom sträng.

## add_title(title, x_title, y_title)
Lägg till eller skriv över titlar i ett diagram.
#### Returnerar:
Inget.
#### Argumentbeskrivning:

Argument | Beskrivning
-------- | -----------
`title` | Ny titel som sträng.
`x_title` | Ny titel på x-axeln, som sträng. Utelämnas denna tas nuvarande titel bort.
`y_title` | Ny titel på y-axeln, som sträng. Utelämnas denna tas nuvarande titel bort.

## format_layout(show_x_grid, show_y_grid)
Uppdaterar utseendet på diagram-ytan: titeln (storlek, centrering), font (storlek, färg, typ), x- och y-axlar (färg, bredd, markörer, grid, etc) och ett flertal till visuella element.
Används för att få alla diagram att ha liknande utseende.
#### Returnerar:
Inget.
#### Argumentbeskrivning:

Argument | Beskrivning
-------- | -----------
`show_x_grid` | Booelskt värde. Om True visas en vertikal linje vid varje x-markör. Standard är falskt.
`show_y_grid` | Booelskt värde. Om True visas en vertikal linje vid varje y-markör. Standard är falskt.

## show_zero_line()
Lägger till en linje för alla värden där x (eller y) är noll. Bra att visa när diagrammet både har positiva och negativa värden.
#### Returnerar:
Inget.
#### Argumentbeskrivning:
Inga argument.

## format_size(width, height)
Ändra dimensionerna på diagram-ytan.
#### Returnerar:
Inget.
#### Argumentbeskrivning:

Argument | Beskrivning
-------- | -----------
`width` | Ny bredd på ytan, i pixlar.
`height` | Ny höjd på ytan, i pixlar.


## format_x_axis(x_tick, x_limits)
Ändra x-axelns omfattning.
#### Returnerar:
Inget.
#### Argumentbeskrivning:

Argument | Beskrivning
-------- | -----------
`x_tick` | Ange bredden mellan markörerna på x-axeln, i relativa värden gentemot dataseriens värden (alltså ej i pixlar)
`x_limits`| En tupel (m,M) där m är minsta värde för x-axeln och M är största

## format_y_axis(y_tick, y_limits)
Ändra y-axelns omfattning.
#### Returnerar:
Inget.
#### Argumentbeskrivning:

Argument | Beskrivning
-------- | -----------
`y_tick` | Ange bredden mellan markörerna på y-axeln, i relativa värden gentemot dataseriens värden (alltså ej i pixlar)
`y_limits`| En tupel (m,M) där m är minsta värde för y-axeln och M är största


## edit_toolbar(filename, format, height,width)
Ändrar inställningar i verktygslådan som visas i toppen av diagram-ytan.
#### Returnerar:
Beskriv vad funktionen returnerar. Beskriv specialfall. Eventuellt ett exempel, om rimligt/hjälpsamt.
#### Argumentbeskrivning:

Argument | Beskrivning
-------- | -----------
`filename` | En sträng som specificerar namnet på filen som laddas när när "save plot"-ikonen aktiveras.
`format`| En av “png”, “svg”, “jpeg”, “webp”,  specificerar filtypen som laddas när när "save plot"-ikonen aktiveras.
`height`| Höjden på filen som laddas ner. Standard är 750px.
`width`| Bredden på filen som laddas ner. Standard är 1050px.

## dotted_line(legend_text, x_0, y_0, x_1, y_1, col, line_width):
Lägger till en streckad linje på diagram-ytan. Skiljer sig från [plot_line](#plot_line-x_0-y_0-x_1-y_1-col-line_width-line_type) genom att vara implementerad som en scatter-data-serie. Har därför en bättre etikett om linjen behöver visa ett specifikt värde.
#### Returnerar:
Inget.
#### Argumentbeskrivning:

Argument | Beskrivning
-------- | -----------
`legend_text` | En sträng som visas som linjens rubrik/beskrivning i legend-rutan.
`x_0` & `y_0` | Startpunkt
`x_1` & `y_1` | Ändpunkt
`col` | En CSS-färg eller HEXkod som sträng. Standard är CSS "black".
`line_width` | Linjens bredd. Standard är 1px.

----

# Funktioner i filen *dropdowns*

## init(ops, desc)
Skapar en Dropdown-instans med givna alternativ.
#### Returnerar:
Instansen.
#### Argumentbeskrivning:

Argument | Beskrivning
-------- | -----------
`ops` | En lista med strängar, där varje sträng blir ett alternativ i dropdown-listan.
`desc` | Etikett som visas till vänster om dropdown-listan. Sträng.

## get()
Returnerar dropdown-instansen själv. Skickas till andra funktioner som argument.
#### Returnerar:
Instansen.
#### Argumentbeskrivning:
Inga argument.

----

# Funktioner i filen *funktioner-i-filen-diagram_classes*
Den här filen innehåller fem klasser: diagram_1, diagram_2, diagram_3, diagram_4, diagram_5. De har varsin init()-metod som enbart ärver instansieringen av [init()](#init-1), och utesluts därför.

## Globala färgkoder
Fyra färgkoder används flera gånger. De styrs av följande globala variabler.

Variabel  | Beskrivning
-------   | ----------
`STANDARD_COL` | Används i scatter-diagrammen, samt i stapeldiagrammet med alla kommuner. För alla staplar/punkter.
`HIGHLIGT_COL` | Används i scatter-diagrammen, samt i stapeldiagrammet med alla kommuner. För den highlight:ade stapeln/punkten.
`COL1` | Färg för den övre dataserien i de två diagrammen med tre staplar
`COL2` | Färg för den undre dataserien i diagram 3 med tre staplar

## MALL funktionsNamn(arg1, ..., argN)
Beskrivning. Inkludera funktion, samt eventuellt "särbeteende".
#### Returnerar:
Beskriv vad funktionen returnerar. Beskriv specialfall. Eventuellt ett exempel, om rimligt/hjälpsamt.
#### Argumentbeskrivning:

Argument | Beskrivning
-------- | -----------
`argumentNamn` | Beskrivning. Inkludera typ (sträng, int, ...), samt eventuella ytterligare krav.

## MALL funktionsNamn(arg1, ..., argN)
Beskrivning. Inkludera funktion, samt eventuellt "särbeteende".
#### Returnerar:
Beskriv vad funktionen returnerar. Beskriv specialfall. Eventuellt ett exempel, om rimligt/hjälpsamt.
#### Argumentbeskrivning:

Argument | Beskrivning
-------- | -----------
`argumentNamn` | Beskrivning. Inkludera typ (sträng, int, ...), samt eventuella ytterligare krav.


[Tillbaka](README.md) till startsidan.
