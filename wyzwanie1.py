#wyzwaniepython ZADANIE 1
#17-07-2016
#autor: @Dewastators
import time
import os.path
import hashlib
import shutil

way = "tst"
def gethash(path):
    block = 4096
    fille = open(path, "r")
    hasher = hashlib.sha1()
    buf = fille.read(block)
    while len(buf)>0:
        hasher.update(buf)
        buf = fille.read(block)
    fille.close()
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
    #print files[keys][0]

if not os.path.exists('tst/duplicates'):
    os.makedirs('tst/duplicates')
    
for keys in files:
    for i in range(len(files[keys])-1):
        shutil.copy2('tst/'+files[keys][i][1],'tst/duplicates')

# okej, wywaliliśmy duplikaty
# czas na porządki

fileslist = []
for keys in files:
    fileslist.append(files[keys][-1])

for files in fileslist:
    year = time.gmtime(files[0]).tm_year
    monthh = time.gmtime(files[0]).tm_mon
    if "tmpae7b74ie" == files[1]: # <------- niby listopad, ale jednak grudzien
        print time.gmtime(files[0])
    month = ""
    if monthh < 10:
        month = "0"+str(monthh)
    else:
        month = str(monthh)
    way = 'tst/'+str(year)+'/'+month
    if not os.path.exists(way):
        os.makedirs(way)
    shutil.copy2('tst/'+files[1],way)

#koniec
