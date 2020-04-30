from plot_funcs import *
from InformationLog import *
from data_funcs import *

STANDARD_COL = '#5ba3cf' # nu ljusblå
HIGHLIGT_COL = '#e45756' # nu röd
COL1 = '#54a246' # nu grön
COL2 = '#4c78a8' # nu mörkblå

def axis_ticks(keyword):
    if keyword == "N15505":
        return 50
    return 20

class diagram_1(plot):

    def __init__(self):
        super().__init__()

    def update(self, kommun, year, keyword_desc, sekom):
        self.clear()

        keyword = desc_to_key[keyword_desc]

        if kommun == "Ej vald":
            kommun = None

        infoLog = InformationLog()

        m = get_data(keyword,year,infoLog,gender = "M")
        f = get_data(keyword,year,infoLog,gender = "K")
        mun = get_all_municipalties()

        mun, m, f = normalize_data(mun,m,f)

        if sekom == "Ja" and kommun:
            mun, m, f = filter_on_SEKOM(kommun,mun,m,f)
            infoLog.addInfo(sekomCol = sekom_data[kommun], expectedTot = no_per_sekom(kommun))

        if kommun and kommun in mun:
            mun, m, f = move_to_last(kommun,mun,m,f)

        col = create_list_of_colors(mun,infoLog,STANDARD_COL,HIGHLIGT_COL,kommun)

        infoLog.addInfo(actualQty = len(mun))

        smallest = min(f + m)
        biggest = max(f + m)
        tick = axis_ticks(keyword)

        self.plot_line(0,0,320,320)
        self.add_scatter(m,f, mun, col, "Pojkar", "Flickor")
        self.format_layout()
        self.add_title(keyword_desc, "Pojkar", "Flickor")
        self.format_x_axis(tick, [smallest-5,biggest+5])
        self.format_y_axis(tick, [smallest-5,biggest+5])
        self.format_size(900,600)
        infoLog.informUser('missingData','succeededYears','sekomCol','actualQty','expectedTot','missingMunis',kommun = kommun)
        self.show(CONFIG=self.edit_toolbar('Diagram_1','svg'))


class diagram_2(plot):

    def __init__(self):
        super().__init__()

    def update(self, kommun,year ,keyword_desc, sekom):
        self.clear()

        keyword = desc_to_key[keyword_desc]

        if kommun == "Ej vald":
            kommun = None

        infoLog = InformationLog()

        var = get_data(keyword,year,infoLog)
        ed = get_data("N15820",year,infoLog)
        mun = get_all_municipalties()

        mun, ed, var = normalize_data(mun,ed,var)

        if sekom == "Ja" and kommun:
            mun, ed, var = filter_on_SEKOM(kommun,mun,ed,var)
            infoLog.addInfo(sekomCol = sekom_data[kommun], expectedTot = no_per_sekom(kommun)) 

        if kommun and kommun in mun:
            mun, ed, var = move_to_last(kommun,mun,ed,var)

        col = create_list_of_colors(mun,infoLog,STANDARD_COL,HIGHLIGT_COL,kommun)

        infoLog.addInfo(actualQty = len(mun))

        smallest = min(var)
        biggest = max(var)
        tick = axis_ticks(keyword)

        self.add_scatter(ed, var, mun, col, "Föräldrars utbildningsnivå (%)", keyword_desc)
        self.format_layout(show_y_grid=True)
        self.add_title(keyword_desc, "Föräldrars utbildningsnivå", keyword_desc)
        self.format_x_axis(20 ,[0,100])
        self.format_y_axis(tick, [smallest-5,biggest+5])
        self.format_size(900,600)
        infoLog.informUser('missingData','succeededYears','sekomCol','actualQty','expectedTot','missingMunis',kommun = kommun)
        self.show(CONFIG=self.edit_toolbar('Diagram_2','svg'))

class diagram_3(plot):

    def __init__(self):
        super().__init__()

    def update(self, kommun,year, subject):
        self.clear()
        if kommun == "Ej vald":
            self._fig.update_layout(title='<b>Välj en kommun för att visa data.</b>')
            self.format_layout()
            self.format_size(1000,600)
            self.show(CONFIG=self.edit_toolbar('Diagram_3','svg'))

            return

        if subject == "Engelska":
            pos_keyword = "N15574"
            neg_keyword = "N15573"

        elif subject == "Matematik":
            pos_keyword = "N15572"
            neg_keyword = "N15571"

        elif subject == "Svenska":
            pos_keyword = "N15570"
            neg_keyword = "N15569"

        infoLog = InformationLog()

        data_over = get_comparison_list(pos_keyword, year, kommun, infoLog)
        data_under = get_comparison_list(neg_keyword, year, kommun, infoLog)

        self.add_bar([kommun, "Sekom", "Rike"],
                        [x if x else 0 for x in data_over],
                        [COL1]*3,
                        text="Högre betyg: ")

        self.add_bar([kommun, "Sekom", "Rike"],
                [-x if x else 0 for x in data_under],
                [COL2]*3,
                text="Lägre betyg: ")

        self.add_title("Andel som fick högre respektive lägre slutbetyg än vad de skrev på nationella prov i " + subject)
        self.format_layout()
        self.show_zero_line()
        self.format_size(1000,600)
        infoLog.informUser('missingData','succeededYears','showSekomAvg')
        self.show(CONFIG=self.edit_toolbar('Diagram_3','svg'))

class diagram_4(plot):

    def __init__(self):
        super().__init__()


    def update(self, kommun, year, subject, overUnder):
        self.clear()

        if overUnder == "Betyg över NP-resultat":
            over = True
        else:
            over = False

        if kommun == "Ej vald":
            kommun = None

        if subject == "Engelska":
            keyword = "N15574" if over else "N15573"

        elif subject == "Matematik":
            keyword = "N15572" if over else "N15571"

        elif subject == "Svenska":
            keyword = "N15570" if over else "N15569"


        infoLog = InformationLog()

        data = get_data(keyword,year,infoLog)
        mun = get_all_municipalties()

        mun, data = normalize_data(mun, data)

        data,mun = sort_by_fst_lst([data, mun], reverse=False)

        rike_avg = get_single_data(keyword, year, infoLog)

        if rike_avg is None:
            rike_avg = get_single_data(keyword, infoLog._alertLog["succeededYears"][keyword], infoLog)

        color = create_list_of_colors(mun,infoLog,COL2,HIGHLIGT_COL,kommun)
        infoLog.addInfo(actualQty = len(mun))

        self.format_layout(show_y_grid=True)
        self.add_Rike_def(rike_avg)
        self.add_bar(mun,data, color, False)
        self.plot_line(0,rike_avg, len(mun), rike_avg,line_type="dot")
        title_snippet = "högre" if over else "lägre"
        self.add_title("Andel som fick " + title_snippet + " slutbetyg än vad de skrev på nationella prov i " + subject)
        self.format_size(1200,600)
        infoLog.informUser('missingData','succeededYears','actualQty','expectedTot','missingMunis',kommun = kommun)
        self.show(CONFIG=self.edit_toolbar('Diagram_4','svg',width=1400))


class diagram_5(plot):

    def __init__(self):
        super().__init__()

    def update(self,kommun,year,keyword_desc):
        self.clear()

        if kommun == "Ej vald":
            self._fig.update_layout(title='<b>Välj en kommun för att visa data.</b>')
            self.format_layout()
            self.format_size(1000,600)
            self.show(CONFIG=self.edit_toolbar('Diagram_5','svg'))

            return

        infoLog = InformationLog()

        keyword = desc_to_key[keyword_desc]

        data = get_comparison_list(keyword, year, kommun, infoLog)

        self.add_bar([kommun, "Sekom", "Rike"],
                    [x if x else 0 for x in data],
                    [COL1]*3)
        self.format_layout()
        self.add_title(keyword_desc)
        self.format_size(1000,600)
        infoLog.informUser('missingData','succeededYears','showSekomAvg')
        self.show(CONFIG=self.edit_toolbar('Diagram_5','svg'))
