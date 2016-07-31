#wyzwaniepython ZADANIE 3 (EASY)
#03-08-2016
#autor: @Dewastators
import os.path
import os
import sys
import shutil
import datetime
import time
def get_size(start_path):
    total_size = 0
    count = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
            count +=1
    return (str(total_size)).join('B'), str(count)
def info(path):
    typ = 'inny'
    size = ''
    count = ''
    way = str(os.getcwd())
    ct = datetime.datetime.fromtimestamp(time.mktime(time.gmtime(os.path.getctime(path)))).date()
    mt = datetime.datetime.fromtimestamp(time.mktime(time.gmtime(os.path.getmtime(path)))).date()
    if os.path.isfile(path):
        typ = 'plik'
        size = (str(os.path.getsize(path))).join('B')
        return path, '\n'.join(['typ: '+typ, 'sciezka: '+(way),
                          'rozmiar: '+(size), 
                          'ctime '+('-'.join([str(ct.year), str(ct.month), str(ct.day)])),
                          'mtime '+('-'.join([str(mt.year), str(mt.month), str(mt.day)]))])
    if os.path.isdir(path):
        typ = 'katalog'
        size, count = get_size(path)
        return path, '\n'.join(['typ: '+(typ), 'sciezka: '+(way),
                          'rozmiar: '+(size), 'liczba_plikow: '+(count),
                          'ctime '+('-'.join([str(ct.year), str(ct.month), str(ct.day)])),
                          'mtime '+('-'.join([str(mt.year), str(mt.month), str(mt.day)]))])
    
    return path, '\n'.join(['typ: '+(typ), 'sciezka: '+(way),
                          'rozmiar: '+(size), 
                          'ctime '+('-'.join([str(ct.year), str(ct.month), str(ct.day)])),
                          'mtime '+('-'.join([str(mt.year), str(mt.month), str(mt.day)]))])
def parse(cmd, *args, **kwargs):
    path = kwargs['oldpath']
    if cmd == 'pwd':
        return path, os.getcwd()
    if cmd == 'touch':
        open(args[0], 'w+')
        return path, None
    if cmd == 'cd':
        if os.path.exists(path):
            return args[0], None
        else:
            return os.path.join(path, args[0]), None
    if cmd == 'cp':
        shutil.copy2(args[0], args[1])
        return path, None
    if cmd == 'mv':
        shutil.move(args[0], args[1])
        return path, None
    if cmd == 'rm':
        shutil.rmtree(args[0])
        return path, None
    if cmd == 'ls':
        return path, '\n'.join(os.listdir(path))
    if cmd == 'info':
        return path, info(path)
path = 'C:\Piotrek'
while True:
    path, output = parse(raw_input(), oldpath=path)
    if not output == None:
        print output
