import pyaudio
import speech_recognition as sr
import wave
from audio.commands import Commands

import pyttsx3

running = True

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()

    stream = pa.open(
        format = pa.get_format_from_width(wf.getsampwidth()),
        channels = wf.getnchannels(),
        rate =wf.getframerate(),
        output = True
    )

    data_stream = wf.readframes(chunk)

    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)

    stream.close()
    pa.terminate()

r = sr.Recognizer()
cmd = Commands()

def initSpeech():
    print("Listening...")
    play_audio("./audio/eventually-590.wav")
    with sr.Microphone() as source:
        print("Say something...")
        audio = r.listen(source)
    play_audio("./audio/ill-make-it-possible-notification.wav")
    command = ""

    try:
        command =r.recognize_google(audio)
    except:
        print("Couldn't understand you")
    
    print("Your command:")
    print(command)

    cmd.discover(command)

    if command in ["quit", "exit", "bye", "goodbye"]:
        global running
        running = False

while running == True:
    initSpeech()
