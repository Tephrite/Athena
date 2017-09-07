#!/usr/bin/env python3.6

from Model.Speech import *
from datetime import datetime


def getTime():
    Speech.speak("The time is "+str(datetime.now().time())[:-10])

def getDate():
    dayOfTheWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th',
            '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st',
            '22nd', '23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31st']
    month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    date = "The date is "+dayOfTheWeek[datetime.now().weekday()]+" the "+day[(datetime.now().day)-1]+" of "+month[(datetime.now().month)-1]
    Speech.speak(date)






