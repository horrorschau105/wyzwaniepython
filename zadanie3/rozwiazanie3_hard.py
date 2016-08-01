#wyzwaniepython ZADANIE 3 (HARD)
#03-08-2016
#autor: @Dewastators
import os
from os import listdir
from Tkinter import *

class SampleApp(Tk):
    def __init__(self, curr_path):
        Tk.__init__(self)
        self.geometry("368x256")
        self.here = Label(self, text="You are here: "+curr_path)
        self.here.pack()
        self.here.place(x=0, y=0)
        
        self.button1 = Button(self, text="touch", command=self.on_button)
        self.button1.pack()
        self.button1.place(x=0, y=20)
        
        self.button2 = Button(self, text="cd", command=self.on_button)
        self.button2.pack()
        self.button2.place(x=42, y=20)
        
        self.button3 = Button(self, text="rm", command=self.on_button)
        self.button3.pack()
        self.button3.place(x=66, y=20)
        
        self.button4 = Button(self, text="info", command=self.on_button)
        self.button4.pack()
        self.button4.place(x=92, y=20)

        self.entry1 = Entry(self)
        self.entry1.insert(5, "arg1")
        self.entry1.pack()
        self.entry1.place(x=125, y=20, height=25)

        self.button5 = Button(self, text="cp", command=self.on_button)
        self.button5.pack()
        self.button5.place(x=72, y=46)

        self.button6 = Button(self, text="mv", command=self.on_button)
        self.button6.pack()
        self.button6.place(x=96, y=46)

        self.entry2 = Entry(self)
        self.entry2.insert(5, "arg2")
        self.entry2.pack()
        self.entry2.place(x=125, y=46, height=25)

        self.listbox = Listbox(self)
        for idx, f in enumerate(listdir(curr_path)):
            self.listbox.insert(idx, f)
        self.listbox.pack()
        self.listbox.place(x=0, y=75, height=100, width=250)

        self.scrollbar = Scrollbar()
        self.scrollbar.pack()
        self.scrollbar.place(x=250, y=75, height= 100)
        

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)


    def on_button(self):
        print(self.entry2.get())

app = SampleApp(os.getcwd())
app.mainloop()
