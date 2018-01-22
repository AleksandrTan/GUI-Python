import sys
from tkinter import Button, YES, BOTH, Toplevel

class NewWindow(Button):
    def __init__(self, parent=None, **configs):
        Button.__init__(self, parent, **configs)
        self.config(text='New Window!', command=self.__call__)
        self.config(bg='green', fg='yellow', padx=10, pady=2, cursor='hand2')
        self.pack(expand=YES, fill=BOTH)

    def __call__(self, *args, **kwargs):
        newwindow = Toplevel()
        newwindow.iconbitmap(r'E:\WebProjects\Шаблоны BFG\Templates\site\images\favicon.ico')
        newwindow.protocol('WM_DELETE_WINDOW', lambda: None)
        newwindow.title('MyNewWindow')
        Button(newwindow, text='Destroy new window!!!', command=newwindow.destroy).pack()