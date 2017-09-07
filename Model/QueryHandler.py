#!/usr/bin/env python3.6
from Model.Conversation import *
from Model.Time import *

def decipherQuery(input):
    if "time" in input:
        getTime()
    elif "date" in input:
        getDate()
    elif "conversation" in input:
        print("conversation")
    elif ("play" in input) and ("song" in input):
        print("spotify")
    elif "joke" in input:
        getJoke()
    else:
        Speech.speak("I'm sorry, can you repeat?")




