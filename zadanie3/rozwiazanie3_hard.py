#wyzwaniepython ZADANIE 3 (HARD)
#03-08-2016
#autor: @Dewastators
from os.path import join, getsize, getctime, getmtime, isfile, isdir, exists
from os import getcwd, walk, listdir, remove
from shutil import copy2, move, rmtree
import datetime
from time import mktime, gmtime
from Tkinter import *
import rozwiazanie3_hard as my # dx
import tkMessageBox

gv_path = getcwd()

def getinfo(path):
    typ = 'inny'
    size = ''
    count = ''
    way = path
    ct = datetime.datetime.fromtimestamp(mktime(gmtime(getctime(path)))).date()
    mt = datetime.datetime.fromtimestamp(mktime(gmtime(getmtime(path)))).date()
    if isfile(path):
        typ = 'plik'
        size = (str(getsize(path)))+('B')
        return '\n'.join(['typ: '+typ, 'sciezka: '+(way),
                          'rozmiar: '+(size), 
                          'ctime '+('-'.join([str(ct.year), str(ct.month), str(ct.day)])),
                          'mtime '+('-'.join([str(mt.year), str(mt.month), str(mt.day)]))])
    if isdir(path):
        typ = 'katalog'
        size, count = get_size(path)
        return '\n'.join(['typ: '+(typ), 'sciezka: '+(way),
                          'rozmiar: '+(size), 'liczba_plikow: '+(count),
                          'ctime '+('-'.join([str(ct.year), str(ct.month), str(ct.day)])),
                          'mtime '+('-'.join([str(mt.year), str(mt.month), str(mt.day)]))])
    
    return '\n'.join(
        ['typ: '+(typ), 'sciezka: '+(way),'rozmiar: '+(size), 
                          'ctime '+('-'.join([str(ct.year), str(ct.month), str(ct.day)])),
                          'mtime '+('-'.join([str(mt.year), str(mt.month), str(mt.day)]))])
def get_size(start_path):
    total_size = 0
    count = 0
    for dirpath, dirnames, filenames in walk(start_path):
        for f in filenames:
            fp = join(dirpath, f)
            total_size += getsize(fp)
            count +=1
    return (str(total_size))+('B'), str(count)

class SampleApp(Tk):
    global gv_path
    path = gv_path
    def mv(self):
        move(self.entry1.get(), self.entry2.get())
        self.refresh()
    def cp(self):
        copy2(self.entry1.get(), self.entry2.get())
        self.refresh()
    def info(self):
        tkMessageBox.showinfo("Info", getinfo(self.entry1.get()))
    def rm(self):
        if isfile(self.entry1.get()):
            remove(self.entry1.get())
        else:
            rmtree(self.entry1.get())
        self.refresh()
    def cd(self):
        self.path = self.entry1.get()
        self.refresh()
    def touch(self):
        open(join(self.path, self.entry1.get()), 'w+')
        self.refresh()
    def refresh(self):
        global gv_path
        gv_path = self.path
        self.destroy()
        print 123
        self = my.SampleApp(gv_path)
    def __init__(self, curr_path):
        global gv_path
        path = curr_path
        gv_path = path
        Tk.__init__(self)
        self.geometry("368x256+100+100")
        self.here = Label(self, text="You are here: "+path)
        self.here.pack()
        self.here.place(x=0, y=0)
        
        self.button1 = Button(self, text="touch", command= self.touch)
        self.button1.pack()
        self.button1.place(x=0, y=20)
        
        self.button2 = Button(self, text="cd", command= self.cd)
        self.button2.pack()
        self.button2.place(x=42, y=20)
        
        self.button3 = Button(self, text="rm", command=self.rm)
        self.button3.pack()
        self.button3.place(x=66, y=20)
        
        self.button4 = Button(self, text="info", command=self.info)
        self.button4.pack()
        self.button4.place(x=92, y=20)

        self.entry1 = Entry(self)
        self.entry1.insert(5, "arg1")
        self.entry1.pack()
        self.entry1.place(x=125, y=20, height=25)

        self.button5 = Button(self, text="cp", command=self.cp)
        self.button5.pack()
        self.button5.place(x=72, y=46)

        self.button6 = Button(self, text="mv", command=self.mv)
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
    
        
app = SampleApp(gv_path)
app.mainloop()
