import sys
from tkinter import *

class MyButtonExit(Button):
    def __init__(self, parent=None, **configs):
        Button.__init__(self, parent, **configs)
        self.config(text='Exit!', command=self.__call__)
        self.config(bg='red', fg='yellow', padx=10, pady=2, cursor='hand2')
        self.pack()

    def __call__(self, *args, **kwargs):
        #sys.exit()
        self.quit()