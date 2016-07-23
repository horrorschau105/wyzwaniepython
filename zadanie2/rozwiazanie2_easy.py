#wyzwaniepython ZADANIE 2 (EASY)
#27-07-2016
#autor: @Dewastators
import os.path
import sys

def line(key, tup, count, extlen= 5, sizelen= 15, histlen=50):
    size, many = tup
    return "{}{}{}{}\n".format(key.rjust(extlen),(str(size)+'B').rjust(sizelen),10*' ',(int(round(histlen*many/count))*"#").rjust(histlen))
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
way = sys.argv[1]
print way
output = info(way, output)
count = 0
for key in output:
    count+=output[key][1]
with open('dane.txt', 'w') as f:
    for key in output:
        f.write(line(key, output[key],count))
