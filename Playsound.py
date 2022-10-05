from lib2to3 import pygram
from time import sleep
from turtle import delay
from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play
import pygame
from pygame import mixer
opt  = int(input("enter the opt: "))
if(opt == 1):
    mixer.init()
    mixer.music.load('Life-Goes-On_BTS_OpraDre.com_.mp3')
    mixer.music.play()
    print("Life goes on is playing")
    while mixer.music.get_busy():
        pygame.time.delay(100)
elif(opt == 2):
    mixer.init()
    mixer.music.load('bts_spring.mp3')
    mixer.music.play()
    print("Spring day is playing")
    while mixer.music.get_busy():
        pygame.time.delay(100)

