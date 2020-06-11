# Installation av Jupyter Notebook

Denna guide ämnar att visa stegen för att installera Jupyter Notebook på Windows -och Mac-datorer.

## Windows 10

1. Först måste du kontrollera om du programspråket [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) på din dator.
2. För att göra detta måste du först öppna kommandotolken. Detta görs lättast genom att trycka `Windows-tangent+r` för att öppna *kör* och sedan skriva `cmd` och trycka enter. ![kör](/pictures/InstallJupyterNotebook/Windows_2_cmd.png)
3. Nu kommer kommandotolken upp. För att kontrollera om Python redan är installerat skriver du `python --version` och trycker på enter-tangenten. Om du har Python installerat kommer du se ett versionsnummer och du kan hoppa till steg VILKET STEG. BEHÖVS EN BILD HÄR. Om Python inte är installerat så kommer ingenting att hända. Om Python är installerat kan du hoppa till steg 10 annars så stänger du kommandotolken. ![Python är inte installerat](/pictures/InstallJupyterNotebook/Windows_2_EjPython.png)
4. För att installera rätt version av Python behöver du veta vilken version av Operativsystem du har.
	1. Klicka på förstoringsglaset eller skriv i sökfältet *Den här datorn* och högerklicka på det översta resultatet och välj *Egenskaper*. ![Hitta *Den här datorn* och högerklicka på *Egenskaper*](/pictures/InstallJupyterNotebook/Windows_4_1_DenHarDatorn.png)
	2. Då kommer du få upp en ruta med information om din dator och det du vill veta är om du 32-bitars versionen av Windows 10 installerat eller 64-bitars versionen. Notera vad du har för version. ![Här kan du se var någonstans det står vad du har för version](/pictures/InstallJupyterNotebook/Windows_4_2_WindowsVersion.png)
5. Gå till [https://www.python.org/downloads/](https://www.python.org/downloads/) och klicka på knappen *Download Python XXX* där *XXX* är ett versionsnnummer. När denna guide skapades var versionsnumret 3.8.3. ![Nedladdningssidan för Python](/pictures/InstallJupyterNotebook/Windows_5_PythonDownload.png)
6. Spara filen på ditt skrivbord. När nedladdningen är klar så dubbelklicka på filen.
7. Börja med att klicka i *Add Python X.X to PATH*, där X.X är ett versionsnummer och sedan *Install now*. ![Klicka i först 1 och sedan 2](/pictures/InstallJupyterNotebook/Windows_7_PythonInstall1.png)
8. När installationen är klar så klicka bara på *close*.
9. Kontrollera att Python är installerat genom att repetera steg 2 och 3. Du får en tydlig instruktion när du ska stänga kommandotolken.
10. Nu måste vi installera något som heter *pip* och *virtualenv*. Det görs genom att i kommandotolken skriva `pip install virtualenv` och trycka enter. ![Installera pip](/pictures/InstallJupyterNotebook/Windows_8_PipInstall.png) ![Installera pip, händelseförlopp](/pictures/InstallJupyterNotebook/Windows_9_PipInstall2.png)
11. Därefter måste vi uppdatera *pip* med kommandot `python -m pip install --upgrade pip`. ![Installera pip](/pictures/InstallJupyterNotebook/Windows_10_PipInstall3.png) ![Uppdatera PIP, händelseförlopp](/pictures/InstallJupyterNotebook/Windows_11_PipInstall4.png)
12. Nu måste vi skapa en virtuell miljö genom kommandot `virtualenv mittenv`. ![Installera ett virtualenv](/pictures/InstallJupyterNotebook/Windows_12_VirtualEnv.png)
13. Nu måste du navigera till mappen *Scripts* i ditt virutalenv genom `cd mittenv\Scripts` och tryck enter. ![Navigera till mappen Scripts](/pictures/InstallJupyterNotebook/Windows_13_CdVirtualEnv.png)
14. För att aktivera vårt nya environment skriver vi `activate.bat`. ![Kör kommandot activate.bat](/pictures/InstallJupyterNotebook/Windows_14_Activate.png)
15. Nu ska du se *(mittenv)* till vänster om den aktuella kommandoraden. ![Efter activate.bat](/pictures/InstallJupyterNotebook/Windows_15_Activate2.png)
16. Nu måste vi installera ett program som heter [NumPy](https://en.wikipedia.org/wiki/NumPy). Detta görs genom kommandot `pip install numpy`. ![Installera Numpy](/pictures/InstallJupyterNotebook/Windows_16_Numpy.png)
17. Därefter installerar vi [OpenCV](https://en.wikipedia.org/wiki/OpenCV) genom att köra kommandot `pip install opencv-python`. ![Installera OpenCV](/pictures/InstallJupyterNotebook/Windows_17_opencv.png)
18. Nästa steg är att installera [Matplotlib](https://en.wikipedia.org/wiki/Matplotlib) genom att köra `pip install matplotlib` ![Installera Matplotlib](/pictures/InstallJupyterNotebook/Windows_18_mattplotlib.png)
19. Nu kan vi äntligen installera Jupyter Notebook med kommandot `python -m pip install jupyter`. ![Installera Jupyter Notebook](/pictures/InstallJupyterNotebook/Windows_19_Jupyter.png)