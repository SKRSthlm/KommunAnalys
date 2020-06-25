# Hur man startar en Jupyter Notebook
*Uppdaterad 25e juni 2020.*

*Denna guide förutsätter att både Jupyter Notebook och GitHub Desktop är installerat och att du har Jupyter Notebook på din dator. Om Jupyter Notebook inte är installerat rekommenderas det att följa guiden [Att ladda ner och använda Jupyter Notebook på din dator](Installera_jupyterNotebook.md) och GitHub Desktop kan installeras med hjälp av guiden [Introduktion till Git och GitHub Desktop](git.md).*

## Windows

1. För att kunna öppna KommunAnalys Jupyter Notebook behöver du först sökvägen till där själva Jupyter Notebook-filen ligger. Det lättaste sättet att hitta sökvägen till mappen är att öppna GitHub Desktop och trycka på *Show in Explorer*. ![GitHub Desktop redo](/pictures/InstallingGit/Windows_7_GitHubDesktopStart.png)
2. Gå sedan in i mappen *src* vilket är där Jupyter Notebook-filerna ligger och kopiera sökvägen. ![Kopiera Sökvägen](/pictures/RunGit/Windows_1_CopyPath.png)
3. För att köra en Jupyter Notebook lokalt kommer du behöva använda kommandotolken. Den öppnas lättast genom att trycka `Windows-tangent+r` för att öppna *kör* och sedan skriva `cmd` och trycka enter. ![kör](/pictures/InstallJupyterNotebook/Windows_2_cmd.png).
4. Sedan skriver du `cd` följt av ett mellanslag och sedan klistrar du in sökvägen som du kopierade tidigare. Det bör då se ut något som följande dvs. `cd [SÖKVÄG]` (*cd* står för *change directory*). ![Sökväg i Kommandotolken](/pictures/RunGit/Windows_2_CmdPath.png).
5. Tryck på `Enter-tangenten` för att utföra kommandot.

Nu kan du välja om du vill bara se hur Jupyter Notebooken ser ut genom att använda *Voila* eller om du faktiskt vill ändra något i Jupyter Notebooken genom att använda *Jupyter Lab*. Skillnaden mellan de båda är att om du använder Voila så kommer slutprodukten visas där du inte kan ändra någonting. Om du vill ändra saker och ting så ska du därför starta notebooken i Jupyter Lab där du kommer att se all kod.

### Voila
1. För att öppna den i *Voila* skriver du `voila main_voila.ipynb` och trycker enter. Din webbläsare ska då startas och visa hur notebooken ser ut.
2. Skulle det vara så att en webbläsare inte startas så kan du kopiera en adress som är ser ut på ungefär som nedan från kommandotolken och klistra in i en webbläsare. ![Klistra in detta](/pictures/RunGit/Windows_3_Voila.png)
3. När du är klar med Notebooken så stänger du den flik i din webbläsare där Notebooken ligger samt går till kommando-tolken och trycker `CTRL+BREAK` dvs. du trycker in *CTRL-tangenten* och med den intryckt trycker du på *BREAK-tangeten*. BREAK-tangeten syftar till *Pause/Break* tangenten som på de flesta tangentbord sitter högst upp nästan längst till höger på tangentbordet. Detta måste du göra för att när Voila starts så startar den en lokal server i bakgrunden som kör din Jupyter Notebook. Den lokala servern stängs inte automatiskt när du stänger din webbläsare utan måste stängas ned manuellt.

### Jupyter Lab
1. Steget är nästan densamma för *Jupyter Lab*. För att öppna i Jupyter Lab så skriver du `jupyter lab main_voila.ipynb`.
2. Jupyter Lab startar precis som Voila i din webbläsare. Skulle det vara så att den inte startar så kan du kopiera in någon av de länkar som har ungfär följande utformning. ![Klistra in detta](/pictures/RunGit/Windows_4_JupyterLabCmd.png)
3. Därefter kommer du att mötas av ett fönster som ser ut som följande: ![Startläget i Jupyter Lab](/pictures/RunGit/Windows_5_JupyterLabDefault.png)
4. Notera här att ingen kod har körts från din Jupyter Notebook utan den har endast öppnats. För att köra all kod så är det bästa att gå till menyn *Run->Run All Cells* ![Köra alla celler i Jupyter Notebook](/pictures/RunGit/Windows_6_JupyterLabRun.png)
5. För mer utförliga instruktioner hur man använder Jupyter Lab rekommenderar vi att leta upp guider på egen hand.
6. När du är klar med Jupyter Lab så stänger du fliken i webbläsaren samt går till kommando-tolken och trycker `CTRL+BREAK` dvs. du trycker in *CTRL-tangenten* och med den intryckt trycker du på *BREAK-tangeten*. BREAK-tangeten syftar till *Pause/Break* tangenten som på de flesta tangentbord sitter högst upp nästan längst till höger på tangentbordet. Detta måste du göra för att när Voila starts så startar den en lokal server i bakgrunden som kör din Jupyter Notebook. Den lokala servern stängs inte automatiskt när du stänger din webbläsare utan måste stängas ned manuellt.

[Tillbaka](README.md) till startsidan.