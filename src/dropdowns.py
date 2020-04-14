import ipywidgets as widgets

class Dropdown:
    
    def __init__(self, ops,start,desc):
        self._drop = widgets.Dropdown(
                            options=ops,
                            value=start,
                            description=desc,
                            disabled=False)
    
    def get(self):
        return self._drop
