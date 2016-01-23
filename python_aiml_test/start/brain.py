import aiml
import os

kernel = aiml.Kernel()

if os.path.isfile("rebot_brain.brn"):
    kernel.bootstrap(brainFile = "rebot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml pattern")
    kernel.saveBrain("rebot_brain.brn")
# kernel = aiml.Kernel()
# kernel.learn("std-startup.xml")
# kernel.respond("load aiml pattern")

print "rebot say: hello, you can talk to me! Just tell me ~"
while True:
    message = raw_input("I say: ")
    if message == "quit":
        exit()
    elif message == "save":
        kernel.saveBrain("rebot_brain.brn")
    elif message == "ch":
        print "rebot say: Cherry! You find me!How did you know my creator??"
    else:
        bot_response = kernel.respond(message)
        print "robot say: %s" % bot_response
