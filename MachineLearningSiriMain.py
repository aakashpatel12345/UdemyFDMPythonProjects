#import pyglet
import pyaudio
import wave
import speech_recognition as sr
import subprocess
from commands import Commander

running = True
def say(text):
  subprocess.call("say " + text, shell = True)

def playAudio(filename):
  chunk = 1024
  wf = wave.open(filename, "rb")
  pa = pyaudio.PyAudio()

  stream = pa.open(
    format=pa.get_format_from_width(wf.getsampwidth),
    channels=wf.getnchannels(),
    rate=wf.getframerate(),
    output=True
  )

  dataStream = wf.readframes(chunk)

  while dataStream:
    stream.write(dataStream)
    dataStream = wf.readframes(chunk)

  stream.clsoe()
  pa.terminate()

#open_file("./audio/nameofFile.wav") 

r = sr.Recognizer()
cmd = Commander()
def initSpeech();
  print("Listening ...")
  play_audio("./audio/nameofFileStartTone.wav")

  with sr.Microphone() as sources
  print ("Say Something")
  audio = r.listen(source)

  play_audio("./audio/nameOfFileEndTone.wav")

  command = ""

  try:
    command = r.recognize_goodle(audio)
  except:
    print("Could not be understood")
  
  
  print("Your command")
  print(command)
  if command in ["quit", "exit", "bye", "goodbye"]:
    global running # uses the global variable
    running = False
  cmd.discover(command)
  #say("Your said: " + command)

while running == True:
  initSpeech()

#file = pyglet.resource.media("audio/wet.mp3")
#file.play()

#pyglet.app.run()



