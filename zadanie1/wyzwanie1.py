#wyzwaniepython ZADANIE 1
#17-07-2016
#autor: @Dewastators
import time
import os.path
import hashlib
import shutil

way = "tst"
def getdata(datastruct):
    mon = datastruct.tm_mon
    return datastruct.tm_year, str(mon) if mon >= 10 else ("0"+str(mon))
def gethash(path, block= 4096):
    with open(path, "r") as f:
        hasher = hashlib.sha1()
        buf = f.read(block)
        while len(buf)>0:
            hasher.update(buf)
            buf = f.read(block)
    return hasher.hexdigest()
files = {}
for f in os.listdir(way):
    path = way+"/"+f
    if os.path.isfile(path):
        hashcode = gethash(path)
        if hashcode in files:
            files[hashcode].append([os.path.getmtime(path),f])
        else:
            files[hashcode] = [[os.path.getmtime(path),f]]
for keys in files:
    files[keys] = sorted(files[keys],key = lambda d: -d[0])
if not os.path.exists('tst/duplicates'):
    os.makedirs('tst/duplicates')
for keys in files:
    for i in range(len(files[keys])-1):
        shutil.copy2('tst/'+files[keys][i][1],'tst/duplicates')
fileslist = []
for keys in files:
    fileslist.append(files[keys][-1])
for files in fileslist:
    year, month = getdata(time.gmtime(files[0]))
    way = 'tst/'+str(year)+'/'+month
    if not os.path.exists(way):
        os.makedirs(way)
    shutil.copy2('tst/'+files[1],way)
