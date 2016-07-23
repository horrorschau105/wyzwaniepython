#wyzwaniepython ZADANIE 2 (HARD)
#27-07-2016
#autor: @Dewastators
import os.path
import sys
import sqlite3
import hashlib

def info(way, objects, card, checksums, curr_id): # jestesmy w folderze way
    sizeof = 0
    countof = 0
    for f in os.listdir(way):
        path = os.path.join(way, f)
        if os.path.isfile(path): # jest to plik
            size = os.path.getsize(path)
            sizeof+=size
            objects.append([curr_id, path, 'f', size])
            checksums.append([curr_id, hashlib.md5(path).hexdigest()])
            curr_id+=1
            countof+=1
        elif os.path.isdir(path): # jest to folder
            objects, card, checksums, curr_id, size, count =info(path, objects,card, checksums, curr_id)
            sizeof +=size
            countof += count+1 
        else: #jest to cos innego (symlink..)
            size = os.path.getsize(path)
            sizeof+=size
            objects.append([curr_id, path, 'o', size])
            curr_id+=1
            countof+=1
    objects.append([curr_id, way, 'd', sizeof])
    card.append([curr_id, countof])
    return objects, card, checksums, curr_id+1, sizeof, countof

folder_name, database_name = sys.argv[1:3]
objects, card, checksums, count, sizeof, countof = info(folder_name, [],[],[], 0)

for i in objects:
    print i
print ' ' 
for i in card:
    print i
print ' ' 
for i in checksums:
    print i
