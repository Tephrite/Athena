#!/usr/bin/env python3.6

import speech_recognition as sr

r = sr.Recognizer()
m = sr.Microphone()


class Speech:

    def __init__(self):
        r = sr.Recognizer()
        m = sr.Microphone()

    def getSpeech(self, view):
        try:
            with m as source:
                view.canvas.itemconfig(view.tText, text="A moment of silence, please...")
                r.energy_threshold=68
                print("Set minimum energy threshold to {}".format(r.energy_threshold))
                view.canvas.itemconfig(view.tText, text="Say something!")
                audio = r.listen(source)
                view.canvas.itemconfig(view.tText, text="Got it! Now to recognize it...")
                try:
                    # recognize speech using Google Speech Recognition
                    value = r.recognize_google(audio)

                    # we need some special handling here to correctly print unicode characters to standard output
                    if str is bytes:  # this version of Python uses bytes for strings (Python 2)
                        view.canvas.itemconfig(view.tText, text=u" "+(value).encode("utf-8"))
                    else:  # this version of Python uses unicode for strings (Python 3+)
                        view.canvas.itemconfig(view.tText, text=" "+(value))
                except sr.UnknownValueError:
                    view.canvas.itemconfig(view.tText, text="Oops! Didn't catch that")
                except sr.RequestError as e:
                    view.canvas.itemconfig(view.tText, text="Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
        except KeyboardInterrupt:
             pass

