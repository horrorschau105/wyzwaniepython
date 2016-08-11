#wyzwaniepython ZADANIE 4 (EASY)
#16-08-2016
#autor: @Dewastators
import Queue
import threading

# called by each thread
def read(q, _):
    txt = raw_input()
    new = "t"
    while not new=="":
        new = raw_input()
        txt+=("\n"+new)
    print txt[:-1]
    q.put(txt[:-1])
def parse(txt, _):
    print "454"
                                     
  
if __name__ == "__main__":
    print "Podwojny enter konczy wprowadzanie tekstu do przerobienia"
    
    q = Queue.Queue()
    taketxt = threading.Thread(target=read, args = (q, 0))
    taketxt.daemon = True
    taketxt.start()
    parseit = threading.Thread(target=parse, args = (q.get(), 0))
    parseit.daemon = True
    parseit.start()
    
    
