from tkinter import *

class LabelClass(Label):
    def __init__(self, parent=None, **configs):
        Label.__init__(self, parent, **configs)
        self.config(bg='black', fg='yellow')
        #self.config(height=3, width=120)
        self.pack(expand=YES, fill=BOTH)