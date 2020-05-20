# Detaljerad dokumentation
Uppdaterad 20e maj 2020.
Denna version av dokumentationen ämnar att testa hur gitHub pages kommer att se ut.
[Tillbaka](README.md) till innehållsförteckningen.

## Funktioner i filen *data_funcs.py*

### get_data(keyword, given_year, infoLog, gender)
Genererar data för alla kommuner i Sverige.

#### Returnerar:
En lista med 290 int/float, med None-värden om data saknas för någon kommun. Saknad data registreras i info-loggen.
Om data saknas för alla kommuner det givna året, väljs data från närmsta år det finns data ifrån. Mer om ordningen på hur 
åren prioriteras i [checkYearsOrder](###checkYearsOrder). Hämtas data från annat år dokumenteras även detta i info-loggen.
#### Argument description:
Argument | Description
-------- | -----------
`keyword` | Specifies the keyword, should be in the NYCKELTAL constant
`given_year` | The year that the data is retrieved from, if available.
`infoLog` | An InformationLog instance, where user messages are saved.
`gender` | If gender is omitted or specified as “T”, this function returns the total average for both boys and girls. Otherwise specify "K"/"M" to get average only for girls/boys.


### checkYearsOrder(year)
Accepts a year in the range specified in YEARS in the API_Anrop file.
Returns a permutation of the years from YEARS in which order to look for data, including the given year.
Prioritizes data closer to the given year, and rather more recent years than not. Example: If YEARS is "2016,2017,2018,2019" and input is 2018 the function returns [2018,2019,2017,2016].
Argument description:
year -- starting year, as string or int
