from diagram_classes import *
from dropdowns import *
import plot_funcs as pf
from API_Anrop import YEARS

class interactive_diagrams:
    
    def __init__(self):
        
        # Skapande av listorna som utgör valen i dropdownmenyerna
        self._munis = ['Ej vald'] + [k for k in pf.mdata.keys()]
        self._sekom = ["Ja","Nej"]
        self._years = YEARS.strip().split(",")
        
        self._1_keywords = ["N15419", "N15505", "N15436"]
        self._1_keydesc = [pf.key_to_desc[k] for k in self._1_keywords]
        self._1_drop_keys = Dropdown(self._1_keydesc, pf.key_to_desc["N15419"], 'Variabel: ')
        self._1_drop_years = Dropdown(self._years, '2018','År: ')
        self._1_drop_munis = Dropdown(self._munis,'Ej vald','Kommun: ')
        self._1_drop_sekom = Dropdown(self._sekom, "Nej", "Sekomfilter: ")
        self._1 = diagram_1()
        
        self._2_keywords = ["N15419", "N15505", "N15436"]
        self._2_keydesc = [pf.key_to_desc[k] for k in self._2_keywords]
        self._2_drop_keys = Dropdown(self._2_keydesc, pf.key_to_desc["N15419"], 'Variabel: ')
        self._2_drop_years = Dropdown(["2016", "2017", "2018", "2019"],'2018','År:')
        self._2_drop_munis = Dropdown(self._munis,'Ej vald','Kommun: ')
        self._2_drop_sekom = Dropdown(self._sekom, "Nej", "Sekomfilter: ")
        self._2 = diagram_2()
    
    def plot1(self):
        """
        Binder Dropdown-menyerna till plotten
        """
        widgets.interact(self._1.update,keyword_desc=self._1_drop_keys.get(),year=self._1_drop_years.get(), 
        kommun=self._1_drop_munis.get(), sekom=self._1_drop_sekom.get())
        
    def plot2(self):
        widgets.interact(self._2.update,keyword_desc=self._2_drop_keys.get(),year=self._2_drop_years.get(), 
        kommun=self._2_drop_munis.get(),sekom=self._2_drop_sekom.get())
        
