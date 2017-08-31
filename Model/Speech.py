#!/usr/bin/env python3.6

import speech_recognition as sr
from gtts import gTTS
from pygame import mixer

r = sr.Recognizer()
m = sr.Microphone()


class Speech:

    def __init__(self):
        r = sr.Recognizer()
        m = sr.Microphone()

    def getSpeech():

        try:
            with m as source:
                r.energy_threshold=68
                print("Set minimum energy threshold to {}".format(r.energy_threshold))
                audio = r.listen(source, phrase_time_limit=3)
                try:
                    # recognize speech using Google Speech Recognition
                    value = r.recognize_google(audio)
                    # we need some special handling here to correctly print unicode characters to standard output
                    if str is bytes:  # this version of Python uses bytes for strings (Python 2)
                        print(value.encode)
                        return value.encode("utf-8")
                    else:  # this version of Python uses unicode for strings (Python 3+)
                        print(value)
                        return value

                except sr.UnknownValueError:
                   print("Oops! Didn't catch that")
                except sr.RequestError as e:
                    print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
        except KeyboardInterrupt:
             pass

    def speak(textString):
        tts = gTTS(text=textString, lang='en')
        tts.save("audio.mp3")
        mixer.init()
        mixer.music.load('D:/Programming/Python Projects/Athena/audio.mp3')
        mixer.music.play()

