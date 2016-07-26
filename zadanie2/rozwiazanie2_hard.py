#wyzwaniepython ZADANIE 2 (HARD)
#27-07-2016
#autor: @Dewastators
import os.path
import sys
import sqlite3
import hashlib

def info(way, objects, card, checksums, curr_id): 
    sizeof = 0
    countof = 0
    for f in os.listdir(way):
        path = os.path.join(way, f)
        if os.path.isfile(path):
            size = os.path.getsize(path)
            sizeof+=size
            objects.append((curr_id, path, 'f', size))
            checksums.append((curr_id, hashlib.md5(path).hexdigest()))
            curr_id+=1
            countof+=1
        elif os.path.isdir(path): 
            objects, card, checksums, curr_id, size, count =info(path, objects,card, checksums, curr_id)
            sizeof +=size
            countof += count+1 
        else: 
            size = os.path.getsize(path)
            sizeof+=size
            objects.append((curr_id, path, 'o', size))
            curr_id+=1
            countof+=1
    objects.append((curr_id, way, 'd', sizeof))
    card.append((curr_id, countof))
    return objects, card, checksums, curr_id+1, sizeof, countof

folder_name, database_name = sys.argv[1:3]
objects, card, checksums, count, sizeof, countof = info(folder_name, [],[],[], 0)
conn = sqlite3.connect(database_name)
c = conn.cursor()
c.executescript("""
    DROP TABLE IF EXISTS objects;
    DROP TABLE IF EXISTS cardinality;
    DROP TABLE IF EXISTS checksums;
    CREATE TABLE objects(Id INT, Path TEXT, Type CHAR, Size INT);
    CREATE TABLE cardinality(Id INT, Nbr_of_elements INT);
    CREATE TABLE checksums(Id INT, Checksum TEXT);
""")
c.executemany('INSERT INTO objects VALUES (?,?,?,?)', objects)
c.executemany('INSERT INTO cardinality VALUES (?,?)', card)
c.executemany('INSERT INTO checksums VALUES (?,?)', checksums)
conn.commit()
conn.close()
