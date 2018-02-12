import time
import webbrowser
from os import path
import random

#Assignment: write a program that open a link with a browser every 2 hours
#Purpose: have a reminder to take a break
#Improvements:
#1 - Turn the program into a reusable parametrized function
#2 - Let the user choose the break interval and repetitions
#3 - Randomize the link choosing from a list of URLs on a file

#This function return a list of urls
def get_urls():
    #set filename for urls list
    urls_file = 'urls.txt'
    #assume that the file has to be inside the same dir of the script
    current_dir = path.dirname(path.realpath(__file__))
    #try open the file
    try:
        with open(path.join(current_dir,urls_file)) as fr:
            #Get the list of urls
            urls = [line.strip() for line in fr]
        return urls
    #on any exception return a predefined urls list
    except:
        return list(["https://www.youtube.com/watch?v=Up1MzGUhQG0"])

#This function open a browser every x minutes for y times
#x = minutes
#y = times
def break_time(minutes, times):
    i = 0
    #get the list of urls
    urls = get_urls()
    #loop 
    while (i < times):
        #wait the specified time
        time.sleep(minutes*60)
        #get a random index in the valid range
        url_ind = random.randint(0,len(urls)-1)
        #open the url
        webbrowser.open(urls[url_ind])
        i = i + 1

minutes = input("How often do you want to take a break? In minutes: ")
times = input("How many breaks do you want to take? ")
break_time(minutes,times)
