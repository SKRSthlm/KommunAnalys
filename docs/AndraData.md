# Introduktion till att ändra och uppdatera data
*Uppdaterad 17e juni 2020.*

*Denna guide förutsätter att både Python och GitHub Desktop är installerade. Om Python inte är installerat kan du följa stegen för att göra detta i guiden [Att ladda ner och använda Jupyter Notebook på din dator](Installera_jupyterNotebook.md) och GitHub Desktop kan installeras med hjälp av guiden [Introduktion till Git och GitHub Desktop](git.md).*

1. För att det ska gå att uppdatera Datan för Notebooken måste vi säkerställa att paketet *requests* är installerat för python. Det görs genom att öppna kommandotolken och skriva `pip install requests`. ![Installera paketet requests](/pictures/AndraData/Windows_1_PipRequests.png)
2. Om du inte ämnar att lägga till nya *Nyckeltal* eller *År* till Notebooken utan bara vill hämta all den senaste datan kan du hoppa till steg 8.
3. Därefter så använder du GitHub Desktop för att öppna var KommunAnalys ligger på din dator. ![KommunAnalys](/pictures/AndraData/Windows_2_Folder.png)
4. Gå sedan in i mappen *src* och öppna filen *Api_Anrop.py* i en texteditor. På Windows kan du använda *Anteckningar/Notepad*.
5. Det som kan ändras är det inom det markerade området. ![Koden i Api_Anrop](/pictures/AndraData/Windows_3_Anrop.png)
6. För att lägga till ett nyckeltal eller ett år så är det bara att fortsätta enligt mönstret. Det spelare ingen roll var någonstans i textsträngen som ni lägger till nyckeltalet/året så länge det är innanför citat-tecknen. Med fördel är det lättast att bygga på i slutet med nya årtal eller nyckeltal.
7. När ni har gjort den ändring ni vill göra så är det bara att spara filen i samma filformat.
8. Därefter måste ni öppna kommandotolken (för Windows) eller terminalen (för Mac).
9. När det är öppet så navigerar ni till mappen *src* via kommandotolk/terminalen med kommandot `cd [SÖKVÄG]`. **TIPS** Det går att kopiera sökvägen från sin utforskare och klistra in i kommandotolken/terminalen. Här följer exempel för Windows 10![Kopierad sökväg](/pictures/AndraData/Windows_4_path.png) ![Inkopierat i Kommandotolken](/pictures/AndraData/Windows_5_pathcopy.png)
10. För att köra *Api_Anrop* skriver ni nu kommandot `python Api_Anrop.py` och kör det. ![Python kommando](/pictures/AndraData/Windows_6_Python.png)
11. *API_Anrop* kommer då att börja arbeta och det tar ca 10 - 20 minuter för den att arbeta klart. Resultatet läggs sedan i mappen *data* i form av filerna *MasterData.txt* och *riket.txt*. **OBS** Ju fler Nyckeltal och Årtal det finns i *API_Anrop* desto längre tid kommer det att ta för programmet att bli klar. ![API_Anrop körs](/pictures/AndraData/Windows_7_PythonProgress.png) ![Filerna har uppdaterats](/pictures/AndraData/Windows_8_FolderData.png)
12. Härnäst öppnar vi och går till GitHub Desktop. Om du har ändrat i *API_Anrop* kommer detta synas här samt om det har tillkommit ny data i *MasterData.txt* eller *riket.txt*. Om det skulle vara så att du inte har gjort några ändringar i *API_Anrop* och efter att du har kört densamma så syns inga förändringar i GitHub Desktop så betyder detta bara att ingen ny data har tillkommit till *MasterData.txt* och *riket.txt*. Eftersom ingenting har ändrats så behöver du således inte göra någon commit heller.
13. Om det är så att något har ändrats och att du ser att förändringar är listade i GitHub Desktop så gör du bara en commit och *Fetch origin*. Sedan är du klar.

[Tillbaka](README.md) till startsidan.