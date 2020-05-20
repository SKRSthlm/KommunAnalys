# Detaljerad dokumentation
Uppdaterad 20e maj 2020.
Denna version av dokumentationen ämnar att testa hur gitHub pages kommer att se ut.

## Funktioner i filen *data_funcs.py*

### get_data
'''python
get_data(keyword, given_year, infoLog, gender="T")
'''
Create data sets by collecting the specified data for all municipalities in Sweden.
#### Returns:
A list of 290 ints/floats, with None-values if data is missing for some municipalities (see infoLog-instance for more information on which).
If data is missing for all municipalities the given year, data from the closest available year is returned (see function checkYearsOrder for more information on which year will be shown). When this happens, it is documented in the InformationLog.
#### Argument description:
Argument | Description
-------- | -----------
keyword | Specifies the keyword, should be in the NYCKELTAL constant
given_year | The year that the data is retrieved from, if available.
infoLog | An InformationLog instance, where user messages are saved.
gender | If gender is omitted or specified as “T”, this function returns the total average for both boys and girls. Otherwise specify "K"/"M" to get average only for girls/boys.
