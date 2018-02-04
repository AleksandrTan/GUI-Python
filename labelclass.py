from tkinter import *

class LabelClass(Label):
    def __init__(self, parent=None, **configs):
        Label.__init__(self, parent, **configs)
        self.config(bg='black', fg='yellow')
        #self.config(height=3, width=120)
        self.pack(expand=YES, fill=BOTH)
        self.bind('<Button-1>', self.oneLeftClick)
        self.bind('<KeyPress>', self.onKeyPress)
        self.focus()

    def oneLeftClick(self, event):
        self.config(text='')
        self.config(bg='blue', fg='green')

    def onKeyPress(self, event):
        data = event.char
        text = self['text']
        self.config(text=text+data)
        # print(self['text'])