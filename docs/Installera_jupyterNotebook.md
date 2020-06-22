# Installation av Jupyter Notebook

Denna guide ämnar att visa stegen för att installera Jupyter Notebook på Windows -och Mac-datorer.

## Windows 10

1. Det första du måste göra är att kolla vilken version av Windows 10 du har. Det kan du göra genom att följa nedanstående steg exempelvis.
	1. Klicka på förstoringsglaset eller skriv i sökfältet *Den här datorn* och högerklicka på det översta resultatet och välj *Egenskaper*. ![Hitta *Den här datorn* och högerklicka på *Egenskaper*](/pictures/InstallJupyterNotebook/Windows_4_1_DenHarDatorn.png)
	2. Då kommer du få upp en ruta med information om din dator och det du vill veta är om du 32-bitars versionen av Windows 10 installerat eller 64-bitars versionen. Notera vad du har för version. ![Här kan du se var någonstans det står vad du har för version](/pictures/InstallJupyterNotebook/Windows_4_2_WindowsVersion.png)	
2. Sedan måste du kontrollera om du har programmeringsspråket [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) installerat på din dator.
3. För att göra detta måste du först öppna kommandotolken. Detta görs lättast genom att trycka `Windows-tangent+r` för att öppna *kör* och sedan skriva `cmd` och trycka enter. ![kör](/pictures/InstallJupyterNotebook/Windows_2_cmd.png)
4. Nu kommer kommandotolken upp. För att kontrollera om Python redan är installerat skriver du `python --version` och trycker på enter-tangenten. Om du har Python installerat kommer du se ett versionsnummer och du kan hoppa till steg 14. ![Python är installerat](/pictures/InstallJupyterNotebook/Windows_3_Python.png) Om Python inte är installerat så kommer ingenting att hända. ![Python är inte installerat](/pictures/InstallJupyterNotebook/Windows_3_EjPython.png)
5. Om din version av Python är *3.8.X* eller högre rekommenderar vi att du avinstallerar den versionen av Python och installerar en version av Python med versionsnummer *3.7.X* där *X* exempelvis är 7, som i nuläget när guiden skrivs, enligt instruktionerna nedan. Det går **INTE** att använda en version som är *3.**8**.X* av den enkla anledningen att den version av Jupyter Notebook och Voila som vi använder inte stöds av Python version *3.8.X* eller senare i nuläget.
6. Stäng ned kommandotolken.
7. Gå till [https://www.python.org](https://www.python.org) och klicka på knappen *Downloads* och välj *Windows* ![Nedladdningssidan för Python](/pictures/InstallJupyterNotebook/Windows_5_PythonDownload.png)
8. Scrolla sedan ned till du hittar en version av Python med versionsnummer *3.7.X* där *X* exempelvis är 7 som i nuläget när guiden skrivs.
9. Välj sedan filen som överrensstämmer med markeringen i bilden och spara den till ditt skrivbord. Detta är installationsfilen för 32-bit men för vårt ändamål fungerar det precis lika bra på en 64-bit version av Windows. ![Välj denna typ av fil](/pictures/InstallJupyterNotebook/Windows_7_PythonDownload2.png)
10. När nedladdningen är klar så dubbelklicka på filen.
11. Börja med att klicka i *Add Python X.X to PATH*, där X.X är ett versionsnummer och sedan *Install now*. ![Klicka i först 1 och sedan 2](/pictures/InstallJupyterNotebook/Windows_7_PythonInstall1.png)
12. När installationen är klar så klicka bara på *close*.
13. Kontrollera att Python är installerat genom att repetera steg 3 och 4. När du har kollat stäng ned kommandotolken igen.
14. Vi behöver även installera något som heter [Node.js](https://en.wikipedia.org/wiki/Node.js).
15. För att göra detta behöver ni först gå till [https://nodejs.org/en/download/](https://nodejs.org/en/download/) välja antingen *32-bit* eller *64-bit* versionen.	
16. Väl på *Node.js* nedladdningssida så ladda ned den version som matchar ditt Windows 10 och spara den på skrivbordet. ![Välj 32-bit eller 64-bit beroende på vilken version du har av Windows 10](/pictures/InstallJupyterNotebook/Windows_21_NodejsDownload.png)
17. Kör sedan filen du precis har laddat ned och följ instruktionerna. ![Första steget i installationen](/pictures/InstallJupyterNotebook/Windows_22_NodejsInstall1.png) ![Andra steget i Installationen](/pictures/InstallJupyterNotebook/Windows_23_NodejsInstall2.png)
18. Låt installationen lägga programmet på den föreslagna platsen. I detta fall `C:\Program Files\nodejs\` ![Tredje steget i Installationen](/pictures/InstallJupyterNotebook/Windows_24_NodejsInstall3.png)
19. Ni behöver inte göra några ändringar utan bara trycka nästa. ![Fjärde steget i Installationen](/pictures/InstallJupyterNotebook/Windows_25_NodejsInstall4.png)
20. Klicka på nästa. ![Femte steget i Installationen](/pictures/InstallJupyterNotebook/Windows_26_NodejsInstall5.png)
21. Klicka på Install. ![Sjätte steget i Installationen](/pictures/InstallJupyterNotebook/Windows_27_NodejsInstall6.png)
22. Hädanefter kommer vi att arbeta mycket i kommandotolken så öppna den genom att följa början av steg 3.
23. Python använder en såkallad *pakethanterare* som heter [pip](https://en.wikipedia.org/wiki/Pip_(package_manager)) och det är den vi primärt nu kommer att använda för att installera resten av det vi behöver. Men först måste vi uppdatera pip till senaste versionen. Vilket görs med följande kommando `python -m pip install --upgrade pip`. ![Installera pip](/pictures/InstallJupyterNotebook/Windows_10_PipInstall3.png) ![Uppdatera PIP, händelseförlopp](/pictures/InstallJupyterNotebook/Windows_11_PipInstall4.png)
24. Nu installerar vi Jupyter Notebook med följande kommando `python -m pip install jupyter`. Installationen kan ta några minuter och det kan bitvis se ut som att inget händer. Ha tålamod. ![Installera Jupyter Notebook](/pictures/InstallJupyterNotebook/Windows_19_Jupyter.png)
25. Efter Jupyter Notebook måste vi installera Jupyter Labs genom kommandot `pip install jupyterlab`. ![Installera Jupyter Labs](/pictures/InstallJupyterNotebook/Windows_29_JupyterLab.png)
26. När detta är klart behöver vi installera ett tillägg till Python som heter [Plotly](https://en.wikipedia.org/wiki/Plotly) .
27. Detta görs genom kommandotolken och kommandot `pip install plotly`. Denna installation kan ta några minuter och vid vissa tidpunkter ser det ut som att det inte händer något. Ha tålamod. ![Installera Plotly](/pictures/InstallJupyterNotebook/Windows_28_Plotly.png)
28. För att Jupyter Labs ska rendera vår notebook korrekt måste vi installera de 3 följande extensions.
	1. `jupyter labextension install @jupyter-widgets/jupyterlab-manager` ![Installera jupyter-widgets extension till Jupyter Labs](/pictures/InstallJupyterNotebook/Windows_31_JupyterLabExtension1.png)
	2. `jupyter labextension install jupyterlab-plotly` ![Installera plotly-stöd till ](/pictures/InstallJupyterNotebook/Windows_32_JupyterLabExtension2.png)
	3. `jupyter labextension install plotlywidget` ![Installera stöd för widgets till Plotly i Jupyter Labs](/pictures/InstallJupyterNotebook/Windows_33_JupyterLabExtension3.png)
29. Då Jupyter Notebook-dokumentet KommunAnalys använder ett tillägg som heter [Voilà](https://blog.jupyter.org/and-voil%C3%A0-f6a2c08a4a93) måste vi även installera detta för att det ska gå att köra KommunAnalys lokalt. Detta görs genom kommandot `pip install voila`. ![Installera tillägget Voilà till Jupyter Notebook](/pictures/InstallJupyterNotebook/Windows_20_Voila.png)

Nu är allt vi behöver installerat för Windows 10.


## Mac

1. Vårt första steg är att öppna upp terminalen, (Även kallad kommandotolken). Från terminalen kommer vi göra en mängd installationer och det är även här ifrån som vi kommer att jupyter notebook. För att enklast hitta terminalen öppna upp launchpad !(/pictures/InstallJupyterNotebook/Mac_launchpad.png)
2. Sök sedan i sökfältet i launchpaden efter programmet Terminal. ![](/pictures/InstallJupyterNotebook/Mac_terminal.png). 
3. Öppna sedan upp detta program, Då ser man något i still med detta ![](/pictures/InstallJupyterNotebook/Mac_myterminal.png)
4. Vårt nästa steg är att undersöka om programmering språket ![Python](https://en.wikipedia.org/wiki/Python_(programming_language)) är installerat på datorn. 
5. Nu kommer terminalen upp. För att kontrollera om Python redan är installerat skriver du `python --version` och trycker på enter-tangenten. Om du har Python installerat kommer du se ett versionsnummer och du kan hoppa till steg 13. ![](/pictures/InstallJupyterNotebook/Mac_python_installerat.png)
Om Python inte är installerat så kommer ingenting att hända. //bild på det 
6. Detta betyder att vi måste ladda ner språket. Gå sedan till https://www.python.org och klicka på knappen Downloads och välj Mac OS X ![](/pictures/InstallJupyterNotebook/Mac_python_install_1.png) 
7. Scrolla sedan ned till du hittar en version av Python med versionsnummer 3.7.X där X exempelvis är 5 som i nuläget när guiden skrivs. Det går INTE att använda en version som är 3.8.X av den enkla anledningen att den version av Jupyter Notebook och Voila som vi använder inte stöds av Python version 3.8.X eller senare i nuläget. 
8.Välj sedan filen som överrensstämmer med markeringen i bilden och spara den till ditt skrivbord. Vi väljer den understa av dessa som heter `Download macOS 64-bit installer`. Men det hade fungerat lika bra att ta den översta som heter `Download macOS 64-bit/32-bit installer`  ![](/pictures/InstallJupyterNotebook/Mac_python_install_2.png)    
9. När man klickar på till exempel den som heter `Download macOS 64-bit installer` kommer denna rutan upp. Se till att den är i kryssad så att `öppna med installer` ![](/pictures/InstallJupyterNotebook/Mac_python_install_3.png)
10. Då kommer detta upp och då är nästa steg att följa installations stegen för att installera python. ![](/pictures/InstallJupyterNotebook/Mac_python_install_4.png)
11. Sedan är det bara att vänta tills installationen är klar. 
12. Kontrollera att Python är installerat genom att repetera steg 4 och 5.
13. Vi behöver även installera något som heter [Node.js](https://en.wikipedia.org/wiki/Node.js).
14. För att göra detta behöver ni först gå till [https://nodejs.org/en/download/](https://nodejs.org/en/download/) och välja *64-bit* versionen.
15. Väl på Node.js nedladdningssida så ska macOS installer väljas ![](/pictures/InstallJupyterNotebook/Mac_nodejs_install_1.png)
16. Då kommer denna ruta upp. Se till att den är i kryssad så att `öppna med installer` ![](/pictures/InstallJupyterNotebook/Mac_nodejs_install_2.png)
17 Nästa steg att följa installations stegen för att installera node.js.
18. Sedan är det bara att vänta tills installationen är klar. 
19. Hädanefter kommer vi att arbeta mycket i terminalen så öppna den genom att följa början av steg 1 till 3.
20. Python använder en såkallad *pakethanterare* som heter [pip](https://en.wikipedia.org/wiki/Pip_(package_manager)) och det är den vi primärt nu kommer att använda för att installera resten av det vi behöver. Men först måste vi uppdatera pip till senaste versionen. Vilket görs med följande kommando `python -m pip install --upgrade pip`. ![Installera pip](/pictures/InstallJupyterNotebook/Mac_pipupdate1.png) ![Uppdatera PIP, händelseförlopp](/pictures/InstallJupyterNotebook/Mac_pipupdate2.png)
21. Nu installerar vi Jupyter Notebook med följande kommando `python -m pip install jupyter`. Installationen kan ta några minuter och det kan bitvis se ut som att inget händer. Ha tålamod. ![Installera Jupyter Notebook](/pictures/InstallJupyterNotebook/Mac_jupyter_notebook.png)
22. Efter Jupyter Notebook måste vi installera Jupyter Labs genom kommandot `pip install jupyterlabs`. ![Installera Jupyter Labs](/pictures/InstallJupyterNotebook/Mac_juputer_lab.png)
23. När detta är klart behöver vi installera ett tillägg till Python som heter [Plotly](https://en.wikipedia.org/wiki/Plotly).
24. Detta görs genom terminalen och kommandot `pip install plotly v1.1.4`. Där v1.1.4 står för vilken version av plotly vi ska använda. Denna installation kan ta några minuter och vid vissa tidpunkter ser det ut som att det inte händer något. Ha tålamod. ![Installera Plotly](/pictures/InstallJupyterNotebook/Mac_Plotly_install.png)
25. För att Jupyter Labs ska rendera vår notebook korrekt måste vi installera de 2 följande extensions. 
	1.`jupyter labextension install @jupyter-widgets/jupyterlab-manager v1.0.3` där v1.0.3 står för versionen av denna labextensionen så att de fungerar med plotly korrekt. Denna installation kan ta några minuter och vid vissa tidpunkter ser det ut som att det inte händer något. Ha tålamod.  ![](/pictures/InstallJupyterNotebook/Mac_labEx1.png)
	2. `jupyter labextension install @jupyterlab/plotly-extension v1.0.0` där v1.0.0 står för versionen av denna labextensionen så att de fungerar med plotly korrekt.Denna installation kan ta några minuter och vid vissa tidpunkter ser det ut som att det inte händer något. Ha tålamod. ![](/pictures/InstallJupyterNotebook/Mac_labEx2.png)
26. Då Jupyter Notebook-dokumentet KommunAnalys använder ett tillägg som heter [Voilà](https://blog.jupyter.org/and-voil%C3%A0-f6a2c08a4a93) måste vi även installera detta för att det ska gå att köra KommunAnalys lokalt. Detta görs genom kommandot `pip install voila`. ![Installera tillägget Voilà till Jupyter Notebook](/pictures/InstallJupyterNotebook/Mac_Voila.png)
27. När detta är gjort är sista steget att skriva in i terminalen `jupyter lab` för att öppna jupyter lab i ett internet fönster. Standard är att den öppnar jupytern i safari. men man kan kopiera URLen och klistra in den i firefox eller google chrome om man vill. ![](/pictures/InstallJupyterNotebook/Mac_jupyter_start.png) (/pictures/InstallJupyterNotebook/Mac_jupyter_url.png)
28. När du känner dig klar med arbetet så kan du stänga ner jupytern genom att trycka `ctrl+c` och sedan trycka `y` och enter i terminalen.  ![](/pictures/InstallJupyterNotebook/Mac_close.png)

Nu är allt vi behöver installerat för Mac.
