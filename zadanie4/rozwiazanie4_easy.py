#wyzwaniepython ZADANIE 4 (EASY)
#16-08-2016
#autor: @Dewastators
import urllib                                       
sock = urllib.urlopen("https://pl.wikipedia.org/wiki/Markdown") 
htmlSource = sock.read()                            
sock.close()                                        
print htmlSource  
