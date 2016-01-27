import aiml
import os
import subprocess
kernel = aiml.Kernel()

if os.path.isfile("rebot_brain.brn"):
    kernel.bootstrap(brainFile = "rebot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml pattern")
    kernel.saveBrain("rebot_brain.brn")
# kernel = aiml.Kernel()
# kernel.learn("std-startup.xml")
# kernel.respond("load aiml pattern")
print("begin game")
a = "http://tsn.baidu.com/text2audio?tex=hello, you can talk to me! just tell me&lan=zh&per=0&pit=5&spd=2&cuid=7519663&ctp=1&tok=24.91b892cbba2c73d07f9fba69182b7960.2592000.1456136364.282335-7519663&qq-pf-to=pcqq.c2c"     
subprocess.call(["mpg123",a])
rebot = "rebot say: hello, you can talk to me! Just tell me "
print (rebot)
while True:
    message = raw_input("I say: ")
    if message == "quit":
        exit()
    elif message == "save":
        kernel.saveBrain("rebot_brain.brn")
    elif message == "ch":
        print ("rebot say: Cherry! You find me!How did you know my creator??")
    else:
        bot_response = kernel.respond(message)
        say =  'http://tsn.baidu.com/text2audio?tex='+bot_response+'&lan=zh&per=0&pit=5&spd=2&cuid=7519663&ctp=1&tok=24.91b892cbba2c73d07f9fba69182b7960.2592000.1456136364.282335-7519663&qq-pf-to=pcqq.c2c'     
        print ("robot say: %s" % bot_response)
        b= subprocess.call(["mpg123",say,">1.txt"],shell=True,stdout=1)
