import speechd
import time

response = speechd.input("Say something, please.")
speechd.say("You said " + response)

def callback(phrase, listener):
    if phrase == "goodbye":
        listener.stoplistening()
    speechd.say(phrase)
    print (phrase)

listener = speechd.listenforanything(callback)
while listener.islistening():
    time.sleep(.5)
