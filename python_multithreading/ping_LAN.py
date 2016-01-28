#!/usr/bin python

from threading import Thread
import subprocess
from Queue import Queue
import datetime

num_threads = 100
ips = ['192.168.0.1','192.168.255.255']
for i in range(25):
    for j in range(255):
        l = '192.168.'+str(i)+'.'+str(j)
        ips.append(l)
        #print (ips)
#print(ips)
q = Queue()
def pingme(i,queue):
    while True:
        ip = queue.get()
        #print('thread %s pinging %s' %(i,ip))
        begin = datetime.datetime.now()
        ret = subprocess.call('ping -c 1 %s' % ip,shell=True,stdout=open('/dev/null','w'),stderr = subprocess.STDOUT)
        #ret.wait()
        end = datetime.datetime.now()
        diff = end-begin

        #if diff.seconds < 10:
         #   print ('%s time %s' %(ip,diff.seconds))

        if ret == 0:
            print ('%s is alive!' %ip)
        elif ret == 1:
            pass
            #print ('%s is down...' %ip)
        queue.task_done()

for i in range(num_threads):
    t=Thread(target=pingme,args=(i,q))
    t.setDaemon(True)
    t.start()
    #print (i)

for ip in ips:
    q.put(ip)
    #print (ip)

print ('main thread waiting....')
q.join()
print ('done')
            
