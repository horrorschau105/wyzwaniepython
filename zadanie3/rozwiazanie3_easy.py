#wyzwaniepython ZADANIE 3 (EASY)
#03-08-2016
#autor: @Dewastators
from os.path import join, getsize, getctime, getmtime, isfile, isdir, exists
from os import getcwd, walk, listdir, remove
from shutil import copy2, move, rmtree
import datetime
from time import mktime, gmtime
def get_size(start_path):
    total_size = 0
    count = 0
    for dirpath, dirnames, filenames in walk(start_path):
        for f in filenames:
            fp = join(dirpath, f)
            total_size += getsize(fp)
            count +=1
    return (str(total_size))+('B'), str(count)
def info(path):
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
def parse(cmd, *args, **kwargs):
    if cmd == 'pwd':
        return path, path
    if cmd == 'touch':
        open(join(path, args[0]), 'w+')
        return path, None
    if cmd == 'cd':
        if exists(args[0]):
            return args[0], None
        else:
            return join(path, args[0]), None
    if cmd == 'cp':
        copy2(args[0], args[1])
        return path, None
    if cmd == 'mv':
        move(args[0], args[1])
        return path, None
    if cmd == 'rm':
        if isfile(args[0]):
            remove(args[0])
        else:
            rmtree(args[0])
        return path, None
    if cmd == 'ls':
        return path, '\n'.join(listdir(path))
    if cmd == 'info':
        return path, info(args[0])
path = getcwd()
while True:
    path, output = parse(*raw_input().split(' '), oldpath=path)
    if not output == None:
        print output
