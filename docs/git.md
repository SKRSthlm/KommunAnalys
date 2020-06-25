# Introduktion till Git och GitHub Desktop
*Uppdaterad 17e juni 2020.*

Att ändra på data i KommunAnalys betyder att man måste använda versionhanteringsprogrammet [Git](https://sv.wikipedia.org/wiki/Git_(datorprogram)). I vanliga fall så används Git främst med kommandotolken/terminalarbete men vi kommer här göra en guide där ni kan använda en version av Git som heter GitHub Desktop som har ett grafiskt gränssnitt. För att installera det på Windows 10 och Mac följ respektive guide nedan.

### Windows 10

1. Börja med att surfa till hemsidan för GitHub Desktop [https://desktop.github.com/](https://desktop.github.com/) ![Hemsida för GitHub Desktop](/pictures/InstallingGit/Windows_1_GitHubDesktop.png)
2. Ladda sedan ned den version som överensstämmer med ditt operativsystem och spara filen på ditt skrivbord.
3. När nedladdningen är klar så dubbelklickar du på filen.
4. Programmet kommer att installera utan att du behöver göra någonting.
5. Därefter så kommer den be om din kontoinformation för GitHub. ![Inloggningssida för GitHub desktop](/pictures/InstallingGit/Windows_2_GitHubDesktopInlogg.png)
6. För att kunna ändra KommunAnalys måste du logga in med inloggningsuppgifterna till kontot där KommunAnalys ligger.
7. Härnäst kommer GitHub Desktop be dig att konfigurera Git genom att ange ett namn och en email vara inkluderat med varje commit (dvs. bidrag) du har gjort. ![Konfigurera Git](/pictures/InstallingGit/Windows_3_GitHubConfigure.png)
8. Slutligen kommer GitHub Desktop fråga dig om du vill bidra med användarstatistik. Här kan du välja vad du vill. Klicka sedan på *Finish*. ![Sista bilden på installationen](/pictures/InstallingGit/Windows_4_GitHubFinish.png)
9. Nu kommer du att få upp en startsida. Då du vill ändra på ett redan befintligt repository väljer du först *SKRSthlm/KommunAnalys* under *Your repositories* genom att klicka på det. Sedan klickar du på knappen *Clone SKRSthlm/KommunAnalys*. Detta innebär att du kommer ladda ned en kopia av KommunAnalys på din dator. ![Du vill göra en Clone av KommunAnalys](/pictures/InstallingGit/Windows_5_GitHubDesktopClone.png)
10. Du kommer nu få en dialogruta som bekräftar länken till KommunAnalys samt den sökväg där kopian av KommunAnalys kommer att läggas. Du kan välja det till vad du vill. I detta fall läggs det i *C:\Users\[ANVÄNDARNAMN]\Documents\GitHub\KommunAnalys*. När du har bestämt dig för en sökväg så trycker du på knappen *Clone*. ![Bestäm var kopian ska ligga på din dator](/pictures/InstallingGit/Windows_6_GitHubDesktopClone2.png)
11. GitHub Desktop kommer sedan arbeta en liten stund för att kopiera KommunAnalys till din dator. När den är klar kommer det se ut som bilden visar. ![GitHub Desktop redo](/pictures/InstallingGit/Windows_7_GitHubDesktopStart.png)

### Mac

SKA FYLLAS I.

## Arbetsflöde

Tanken med Git och portalen GitHub (som lagrar projekt) är att det ska vara lätt för människor att delta och bidra till mjukvaruprojekt genom att klona filerna till sitt eget konto, ändra på något och sedan skicka in den ändringen, vilket i Git kallas för *commit* eller på svengelska att *commita*. Finessen med detta är att alla tidigare versioner av projektet sparas och man kan lätt se vilka commits som har gjorts och vad de exakt ändrade. Låt oss gå igenom en snabb översikt av gränssnittet.

![GitHub Desktop redo](/pictures/InstallingGit/Windows_8_GitHubDesktopInterface.png)

1. När ni har gjort en ändring i en fil i projektet och vill commita det bidraget så måste ni först som synes i 1a skriva en kort rubrik som sammanfattar vad ni har gjort för ändring. Därefter trycker ni på knappen 1b *Commit to master* för att skicka in ändringen.
2. Denna knapp öppnar helt enkelt projektmappen i utforskaren.
3. Här kan du se vilka ändringar du har gjort men som du inte än har commitat.
4. Här kan du se alla ändringar som någonsin har gjorts i projektet.
5. Denna knapp uppdaterar ditt lokala projekt genom att ladda ned alla ändringar som du eventuellt inte har på din lokala dator.

### Exempel

1. Säg att vi vill göra en ändring där vi lägger till en textfil som heter *test.txt*. Vi börjar då med att klicka på *Show in Explorer* och får upp vår projektmapp. ![Projektmappen på datorn](/pictures/InstallingGit/Windows_9_GitHubDesktopExempelFolder.png)
2. Sedan skapar vi en fil som heter *test.txt*. Vi dubbeklickar på den och skriver *Det här är en testfil*, sparar och stänger filen. ![Skapat en testfil](/pictures/InstallingGit/Windows_10_GitHubDesktopExempelFile.png)
3. Om vi nu går tillbaka till GitHub Desktop kommer vi se följande: ![GitHub Desktop har uppdaterat och visar den nya filen](/pictures/InstallingGit/Windows_11_GitHubDesktopTestFile.png)
4. Om vi nu vill att denna fil ska läggas till så hade vi skrivit en rubrik i fältet tidigare benämnt som 1a och sedan tryckt på *commit to master*.
5. Därefter måste man trycka på knappen *Fetch origin* (benämnd som knapp 5) som uppdaterar KommunAnalys online samt hämtar alla senaste ändringarna.

Det viktiga att förstå är att alla ändringar som görs måste commitas och skickas upp till KommunAnalys online genom *Fetch origin*. Det innebär att även filer som tas bort måste commitas att de har tagits bort MEN även om de är borta i den nuvarande version av projektet så finns de fortfarande kvar i en tidigare version. Med andra ord, om du skulle commita en ändring där du har tagit bort en fil av misstag eller gjort en ändring så att projektet inte fungerar längre så kan du alltid gå tillbaka genom att titta under *History* och återskapa filerna.

Som synes så finns det också en checkbox bredvid *test.txt* och syftet med detta är att om du har gjort många ändringar så kanske du vill göra flera commits där innehållet i varje commits följer ett tema. Säg att du har gjort en massa kod-ändringar men också en massa guider. Då kanske du vill bocka i alla ändringar som har med kod att göra i en commit och därefter gör du en till commit som bara berör guiderna.

**ETT VARNINGENS ORD:** Se till att aldrig vara två eller fler personer som arbetar med samma fil samtidigt, för detta kan ställa till problem. Utan arbetsflödet bör vara när två eller flera personer vill arbeta med samma fil: *Person 1 meddelar att denne ska göra ändringar i fil XXX -> Person 1 gör sina ändringar -> Person 1 commitar ändringarna och meddelar att denne är klar -> Person 2 uppdaterar sitt projekt genom att trycka på 'Fetch Origin' (benämnd som 5 ovan) -> Person 2 gör sina ändringar -> ... -> Person N commitar sina ändringar och meddelar att denne är klar*. Följer man detta arbetsflöde så kommer man undvika mycket huvudvärk.

Det går såklart att arbeta på *olika* filer samtidigt projektet utan problem. Så om Person 1 håller på med fil X och person 2 håller på med fil Y så är inte det några problem. Problemen uppstår när två eller flera personer arbetar och ändrar på samma fil samtidigt.

[Tillbaka](README.md) till startsidan.