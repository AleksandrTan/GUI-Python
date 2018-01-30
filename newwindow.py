import sys
from tkinter import Button, YES, BOTH, Toplevel
from tkinter.colorchooser import askcolor

class NewWindow(Button):
    def __init__(self, labels=0, parent=None, **configs):
        Button.__init__(self, parent, **configs)
        self.config(text='New Window!', command=self.__call__)
        self.config(bg='green', fg='yellow', padx=10, pady=2, cursor='hand2')
        self.pack(expand=YES, fill=BOTH)
        self.labels = labels

    def __call__(self, *args, **kwargs):
        makemodal = True
        newwindow = Toplevel()
        newwindow.iconbitmap(r'E:\WebProjects\Шаблоны BFG\Templates\site\images\favicon.ico')
        newwindow.protocol('WM_DELETE_WINDOW', lambda: None)
        newwindow.title('MyNewWindow')
        Button(newwindow, text='Choise Color!', bg='green', command=self.show_color).pack()
        Button(newwindow, text='Destroy new window!!!', bg='red', command=newwindow.destroy).pack()
        if makemodal:
            newwindow.focus_set()
            newwindow.grab_set()
            newwindow.wait_window()

    def show_color(self):
        data, hexstr = askcolor()
        print(data)
        self.labels.config(bg=hexstr, fg='yellow')