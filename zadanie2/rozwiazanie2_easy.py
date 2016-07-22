#wyzwaniepython ZADANIE 2 (EASY)
#27-07-2016
#autor: @Dewastators
import time
import os.path
import shutil

def line(key, tup, count, extlen= 5, sizelen= 15, histlen=30):
    size, many = tup
    return key.rjust(extlen)+str(size).rjust(sizelen)+(int(round(histlen*many/count))*"#").rjust(histlen)
def info(way, data): # jestesmy w folderze way
    # jezeli cos jest plikiem, to dorzucamy do slownika rozmiar
    # jesli nie to tylko wchodzimy glebiej
    for f in os.listdir(way):
        path = way+"/"+f
        if os.path.isfile(path): # jest to plik
            ext = path.split('.')[-1]
            if ext in data:
                data[ext][0]+=os.path.getsize(path)
                data[ext][1]+=1
            else:
                data[ext]=[os.path.getsize(path),1]
        else: # jest to folder
            data = info(path,data)
    return data
output = {}
way = "F"
output = info(way, output)
count = 0
for key in output:
    count+=output[key][1]
for key in output:
    print line(key, output[key],count)
