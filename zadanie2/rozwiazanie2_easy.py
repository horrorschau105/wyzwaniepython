#wyzwaniepython ZADANIE 2 (EASY)
#27-07-2016
#autor: @Dewastators
import os.path

def line(key, tup, count, extlen= 5, sizelen= 15, histlen=50):
    size, many = tup
    return "{}{}{}{}".format(key.rjust(extlen),str(size).rjust(sizelen),10*' ',(int(round(histlen*many/count))*"#").rjust(histlen))
def info(way, data): # jestesmy w folderze way
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
