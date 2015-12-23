# Text To Speech using SAPI (Windows) and Python module pyTTS by Peter Parente
# download installer file pyTTS-3.0.win32-py2.4.exe 
# from: http://sourceforge.net/projects/uncassist
# also needs: http://www.cs.unc.edu/Research/assist/packages/SAPI5SpeechInstaller.msi
# and pywin32-204.win32-py2.4.exe at this date the latest version of win32com
# from: http://sourceforge.net/projects/pywin32/
# tested with Python24 on a Windows XP computer  vagaseat  15jun2005
import pyTTS
import time
tts = pyTTS.Create()
# set the speech rate, higher value = faster
# just for fun try values of -10 to 10
tts.Rate = 1
print "Speech rate =", tts.Rate
# set the speech volume percentage (0-100%)
tts.Volume = 90
print "Speech volume =", tts.Volume
# get a list of all the available voices
print "List of voices =", tts.GetVoiceNames()
# explicitly set a voice
tts.SetVoiceByName('MSMary')
print "Voice is set ot MSMary"
print
# announce the date and time, does a good job
timeStr = "The date and time is " + time.asctime()
print timeStr
tts.Speak(timeStr)
print
str1 = """
A young executive was leaving the office at 6 pm when he found 
the CEO standing in front of a shredder with a piece of paper in hand. 
"Listen," said the CEO, "this is important, and my secretary has left. 
Can you make this thing work?"
"Certainly," said the young executive. He turned the machine on, 
inserted the paper, and pressed the start button.
"Excellent, excellent!" said the CEO as his paper disappeared inside 
the machine. "I just need one copy."
"""
print str1
tts.Speak(str1)
tts.Speak('Haah haa haah haa')
print
str2 = """
Finagle's fourth law:
 Once a job is fouled up, anything done to improve it only makes it worse.
"""
print str2
print
print "The spoken text above has been written to a wave file (.wav)"
tts.SpeakToWave('Finagle4.wav', str2)
print "The wave file is loaded back and spoken ..."
tts.SpeakFromWave('Finagle4.wav')
print
print "Substitute a hard to pronounce word like Ctrl key ..."
#create an instance of the pronunciation corrector
p = pyTTS.Pronounce()
# replace words that are hard to pronounce with something that 
# is spelled out or misspelled, but at least sounds like it
p.AddMisspelled('Ctrl', 'Control')
str3 = p.Correct('Please press the Ctrl key!')
tts.Speak(str3)
print
print "2 * 3 = 6"
tts.Speak('2 * 3 = 6')
print
tts.Speak("sounds goofy, let's replace * with times")
print "Substitute * with times"
# ' * ' needs the spaces
p.AddMisspelled(' * ', 'times')
str4 = p.Correct('2 * 3 = 6')
tts.Speak(str4)
print
print "Say that real fast a few times!"
str5 = "The sinking steamer sunk!"
tts.Rate = 3
for k in range(7):
  print str5
  tts.Speak(str5)
  time.sleep(0.3)
tts.Rate = 0
tts.Speak("Wow, not one mispronounced word!")
