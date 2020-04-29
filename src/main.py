#import time
#starttime=time.time()
from diagram_classes import *
from dropdowns import *
from IPython.display import display
import plot_funcs as pf
from API_Anrop import YEARS


def alter_widget_placement(widget, cols):
    """
    Placerar alla widgets bredvid varandra, på specificerat antal kolumner.
    Plottar grafen under dessa.

    Arguments:
    widget - interactive datastruktur, innehåller den nödvändiga datan för att skapa en plot med interaktiva widgets.
    cols   - Specificerar antalet kolumner som widgetsarna placeras på.
    """

    center = widgets.Layout(align_items = "center")                                 # Centrera plotten och dropdownmenyerna.
    widget.update()                                                                 # Behövs för att visa plotten vid uppstart.
    output = widget.children[-1]                                                    # Hämtar plotten
    sub_boxes = []
    widget_count = len(widget.children)-1
    for i in range(0,widget_count,cols):
        tmp = []
        for j in range(cols):
            if i+j == widget_count:
                break
            tmp.append(widget.children[i+j])
        sub_boxes.append(widgets.HBox(tmp))
    display(widgets.VBox([*sub_boxes,output],layout=center))                        # Centrerar och visar plotten.


class interactive_diagrams:

    def __init__(self):

        # Skapande av listorna som utgör valen i dropdownmenyerna
        self._munis = ['Ej vald'] + [k for k in pf.mdata.keys()]
        self._sekom = ["Nej","Ja"]
        self._years = YEARS.strip().split(",")

        self._1_keywords = ["N15419", "N15505", "N15436"]
        self._1_keydesc = [pf.key_to_desc[k] for k in self._1_keywords]
        self._1_drop_keys = Dropdown(self._1_keydesc, 'Variabel: ')
        self._1_drop_years = Dropdown(self._years, 'År: ')
        self._1_drop_munis = Dropdown(self._munis,'Kommun: ')
        self._1_drop_sekom = Dropdown(self._sekom, "Sekomfilter: ")
        self._1 = diagram_1()

        self._2_keywords = ["N15419", "N15505", "N15436"]
        self._2_keydesc = [pf.key_to_desc[k] for k in self._2_keywords]
        self._2_drop_keys = Dropdown(self._2_keydesc, 'Variabel: ')
        self._2_drop_years = Dropdown(["2016", "2017", "2018", "2019"],'År:')
        self._2_drop_munis = Dropdown(self._munis,'Kommun: ')
        self._2_drop_sekom = Dropdown(self._sekom, "Sekomfilter: ")
        self._2 = diagram_2()

        self._3_drop_years = Dropdown(self._years,'År: ')
        self._3_drop_munis = Dropdown(self._munis,'Kommun: ')
        self._3_drop_subj = Dropdown(["Matematik", "Svenska", "Engelska"],"Ämne: ")
        self._3 = diagram_3()

        self._4_drop_years = Dropdown(self._years, 'År: ')
        self._4_drop_munis = Dropdown(self._munis,'Kommun: ')
        self._4_drop_subj = Dropdown(["Matematik", "Svenska", "Engelska"],"Ämne: ")
        self._4_drop_over_under = Dropdown(["Betyg över NP-resultat", "Betyg under NP-resultat"],"Över/under: ")
        self._4 = diagram_4()

        self._5_keywords = ["N15419", "N15505", "N15436"]
        self._5_keydesc = [pf.key_to_desc[k] for k in self._5_keywords]
        self._5_drop_years = Dropdown(self._years, 'År: ')
        self._5_drop_munis = Dropdown(self._munis,'Kommun: ')
        self._5_drop_keyword = Dropdown(self._5_keydesc,"Nyckeltal: ")
        self._5 = diagram_5()

    def plot1(self):
        """
        Binder Dropdown-menyerna till plottar, och visar dem.
        """
        alter_widget_placement(widgets.interactive(self._1.update,keyword_desc=self._1_drop_keys.get(),year=self._1_drop_years.get(),
        kommun=self._1_drop_munis.get(), sekom=self._1_drop_sekom.get()),cols=2)

    def plot2(self):
        alter_widget_placement(widgets.interactive(self._2.update,keyword_desc=self._2_drop_keys.get(),year=self._2_drop_years.get(),
        kommun=self._2_drop_munis.get(),sekom=self._2_drop_sekom.get()),cols=2)

    def plot3(self):
        alter_widget_placement(widgets.interactive(self._3.update,year=self._3_drop_years.get(),
        kommun=self._3_drop_munis.get(),subject=self._3_drop_subj.get()),cols=3)

    def plot4(self):
        alter_widget_placement(widgets.interactive(self._4.update,year=self._4_drop_years.get(),
        kommun=self._4_drop_munis.get(),subject=self._4_drop_subj.get(),overUnder=self._4_drop_over_under.get()),cols=2)

    def plot5(self):
        alter_widget_placement(widgets.interactive(self._5.update,year=self._5_drop_years.get(),
        kommun=self._5_drop_munis.get(),keyword_desc=self._5_drop_keyword.get()),cols=3)




def Update_timer():
    while True:
        diagram = interactive_diagrams()
        diagram.plot1()
        time.sleep(900.0 - ((time.time() - starttime) % 900.0))


#Update_timer()
