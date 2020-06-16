# Installation av Jupyter Notebook

Denna guide ämnar att visa stegen för att installera Jupyter Notebook på Windows -och Mac-datorer.

## Windows 10

1. Det första du måste göra är att kolla vilken version av Windows 10 du har. Det kan du göra genom att följa nedanstående steg exempelvis.
	1. Klicka på förstoringsglaset eller skriv i sökfältet *Den här datorn* och högerklicka på det översta resultatet och välj *Egenskaper*. ![Hitta *Den här datorn* och högerklicka på *Egenskaper*](/pictures/InstallJupyterNotebook/Windows_4_1_DenHarDatorn.png)
	2. Då kommer du få upp en ruta med information om din dator och det du vill veta är om du 32-bitars versionen av Windows 10 installerat eller 64-bitars versionen. Notera vad du har för version. ![Här kan du se var någonstans det står vad du har för version](/pictures/InstallJupyterNotebook/Windows_4_2_WindowsVersion.png)	
2. Sedan måste du kontrollera om du har programmeringsspråket [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) installerat på din dator.
3. För att göra detta måste du först öppna kommandotolken. Detta görs lättast genom att trycka `Windows-tangent+r` för att öppna *kör* och sedan skriva `cmd` och trycka enter. ![kör](/pictures/InstallJupyterNotebook/Windows_2_cmd.png)
4. Nu kommer kommandotolken upp. För att kontrollera om Python redan är installerat skriver du `python --version` och trycker på enter-tangenten. Om du har Python installerat kommer du se ett versionsnummer och du kan hoppa till steg 9. ![Python är installerat](/pictures/InstallJupyterNotebook/Windows_3_Python.png) Om Python inte är installerat så kommer ingenting att hända. ![Python är inte installerat](/pictures/InstallJupyterNotebook/Windows_3_EjPython.png)
5. Gå sedan till [https://www.python.org](https://www.python.org) och klicka på knappen *Downloads* och välj *Windows*![Nedladdningssidan för Python](/pictures/InstallJupyterNotebook/Windows_5_PythonDownload.png)
6. Scrolla sedan ned till du hittar en version av Python med versionsnummer *3.7.X* där *X* exempelvis är 7 som i nuläget när guiden skrivs. Det går **INTE** att använda en version som är *3.**8**.X* av den enkla anledningen att den version av Jupyter Notebook och Voila som vi använder inte stöds av version *3.8.X*.
7. Välj sedan filen som överrensstämmer med markeringen i bilden och spara den till ditt skrivbord. Detta är installationsfilen för 32-bit men för vårt ändamål fungerar det precis lika bra på en 64-bit version av Windows. ![Välj denna typ av fil](/pictures/InstallJupyterNotebook/Windows_7_PythonDownload2.png)
6. När nedladdningen är klar så dubbelklicka på filen.
7. Börja med att klicka i *Add Python X.X to PATH*, där X.X är ett versionsnummer och sedan *Install now*. ![Klicka i först 1 och sedan 2](/pictures/InstallJupyterNotebook/Windows_7_PythonInstall1.png)
8. När installationen är klar så klicka bara på *close*.
9. Kontrollera att Python är installerat genom att repetera steg 2 och 3.
10. Vi behöver även installera något som heter [Node.js](https://en.wikipedia.org/wiki/Node.js).
11. För att göra detta behöver ni först gå till [https://nodejs.org/en/download/](https://nodejs.org/en/download/) välja antingen *32-bit* eller *64-bit* versionen.	
12. Väl på *Node.js* nedladdningssida så ladda ned den version som matchar ditt Windows 10 och spara den på skrivbordet. ![Välj 32-bit eller 64-bit beroende på vilken version du har av Windows 10](/pictures/InstallJupyterNotebook/Windows_21_NodejsDownload.png)
13. Kör sedan filen du precis har laddat ned och följ instruktionerna. ![Första steget i installationen](/pictures/InstallJupyterNotebook/Windows_22_NodejsInstall1.png) ![Andra steget i Installationen](/pictures/InstallJupyterNotebook/Windows_23_NodejsInstall2.png)
14. Låt installationen lägga programmet på den föreslagna platsen. I detta fall `C:\Program Files\nodejs\` ![Tredje steget i Installationen](/pictures/InstallJupyterNotebook/Windows_24_NodejsInstall3.png)
15. Ni behöver inte göra några ändringar utan bara trycka nästa. ![Fjärde steget i Installationen](/pictures/InstallJupyterNotebook/Windows_25_NodejsInstall4.png)
16. Klicka på nästa. ![Femte steget i Installationen](/pictures/InstallJupyterNotebook/Windows_26_NodejsInstall5.png)
17. Klicka på Install. ![Sjätte steget i Installationen](/pictures/InstallJupyterNotebook/Windows_27_NodejsInstall6.png)
10. Hädanefter kommer vi att arbeta mycket i kommandotolken så öppna den genom att följa början av steg 3.
11. Python använder en såkallad *pakethanterare* som heter [pip](https://en.wikipedia.org/wiki/Pip_(package_manager)) och det är den vi primärt nu kommer att använda för att installera resten av det vi behöver. Men först måste vi uppdatera pip till senaste versionen. Vilket görs med följande kommando `python -m pip install --upgrade pip`. ![Installera pip](/pictures/InstallJupyterNotebook/Windows_10_PipInstall3.png) ![Uppdatera PIP, händelseförlopp](/pictures/InstallJupyterNotebook/Windows_11_PipInstall4.png)
12. Nu installerar vi Jupyter Notebook med följande kommando `python -m pip install jupyter`. Installationen kan ta några minuter och det kan bitvis se ut som att inget händer. Ha tålamod. ![Installera Jupyter Notebook](/pictures/InstallJupyterNotebook/Windows_19_Jupyter.png)
13. Efter Jupyter Notebook måste vi installera Jupyter Labs genom kommandot `pip install jupyterlabs`. ![Installera Jupyter Labs](/pictures/InstallJupyterNotebook/Windows_29_JupyterLab.png)
14. När detta är klart behöver vi installera ett tillägg till Python som heter [Plotly](https://en.wikipedia.org/wiki/Plotly) .
15. Detta görs genom kommandotolken och kommandot `pip install plotly`. Denna installation kan ta några minuter och vid vissa tidpunkter ser det ut som att det inte händer något. Ha tålamod. ![Installera Plotly](/pictures/InstallJupyterNotebook/Windows_28_Plotly.png)
16. För att Jupyter Labs ska rendera vår notebook korrekt måste vi installera de 3 följande extensions.
	1. `jupyter labextension install @jupyter-widgets/jupyterlab-manager` ![Installera jupyter-widgets extension till Jupyter Labs](/pictures/InstallJupyterNotebook/Windows_31_JupyterLabExtension1.png)
	2. `jupyter labextension install jupyterlab-plotly` ![Installera plotly-stöd till ](/pictures/InstallJupyterNotebook/Windows_32_JupyterLabExtension2.png)
	3. `jupyter labextension install plotlywidget` ![Installera stöd för widgets till Plotly i Jupyter Labs](/pictures/InstallJupyterNotebook/Windows_33_JupyterLabExtension3.png)
20. Då Jupyter Notebook-dokumentet KommunAnalys använder ett tillägg som heter [Voilà](https://blog.jupyter.org/and-voil%C3%A0-f6a2c08a4a93) måste vi även installera detta för att det ska gå att köra KommunAnalys lokalt. Detta görs genom kommandot `pip install voila`. ![Installera tillägget Voilà till Jupyter Notebook](/pictures/InstallJupyterNotebook/Windows_20_Voila.png)

Nu är allt vi behöver installerat för Windows 10.


## Mac

