from tkinter import *
from tkinter.messagebox import *

class DialogWindow(Button):
    def __init__(self, parent=None, **configs):
        Button.__init__(self, parent)
        self.config(text='Dialog Window!', command=self.__call__)
        self.config(bg='green', fg='yellow', padx=10, pady=2, cursor='hand2')
        self.pack(expand=YES, fill=BOTH)

    def __call__(self, *args, **kwargs):
        if askyesno('Warning!!!', 'Do yuo really want to quit!'):
            showwarning('Yes', 'Quit not yet implemented')
        else:
            showinfo('No', 'Quit has been canceled')