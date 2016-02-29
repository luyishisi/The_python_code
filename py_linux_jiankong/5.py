#!/usr/bin/env Python 
# coding:utf-8
import os, sys, time 

while True: 
    time.sleep(4) 
    try: 
        ret = os.popen('ps -C apache2 -o pid,cmd').readlines() 
        if len(ret) < 2: 
            print "apache 进程异常退出， 4 秒后重新启动" 
        time.sleep(3) 
        os.system("service apache2 restart") 
        print("service apache2 restart")
        ret2 = os.popen('ps -C apache2 -o pid,cmd').readlines()  
        print(ret2)
    except: 
        print "Error", sys.exc_info()[1]

