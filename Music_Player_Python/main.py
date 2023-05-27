import pygame
from pygame import mixer
from tkinter import *
import os
def playsong():
    currentsong=playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("Playing")
    mixer.music.play()

def pausesong():
    songstatus.set("Paused")
    mixer.music.pause()

def stopsong():
    songstatus.set("Stopped")
    mixer.music.stop()

def resumesong():
    songstatus.set("Resuming")
    mixer.music.unpause()


def songs():
    pass

current_song_index = 0
def nextsong():
    global current_song_index

    if current_song_index < len(songs) - 1:
        current_song_index += 1
    else:
        current_song_index = 0

    song = songs[current_song_index]
    mixer.music.load(song)
    mixer.music.play()

root=Tk()
root.title('MP3 Music Player')

mixer.init()
songstatus=StringVar()
songstatus.set("choosing")



#playlist---------------

playlist=Listbox(root,selectmode=SINGLE,bg='gray20',fg="cornsilk1",font=('arial',10),width=56)
playlist.grid(columnspan=10)

os.chdir(r'MyPlaylist')
songs=os.listdir()
for s in songs:
    playlist.insert(END,s)

playbtn=Button(root,text="Play",command=playsong)
playbtn.config(font=('arialnarrow',15),bg="DodgerBlue2",fg="white",padx=8,pady=2)
playbtn.grid(row=1,column=0)

pausebtn=Button(root,text="Pause",command=pausesong)
pausebtn.config(font=('arial',15),bg="DodgerBlue2",fg="white",padx=8,pady=2)
pausebtn.grid(row=1,column=1)

resumebtn=Button(root,text="Resume",command=resumesong)
resumebtn.config(font=('arial',15),bg="DodgerBlue2",fg="white",padx=8,pady=2)
resumebtn.grid(row=1,column=2)

stopbtn=Button(root,text="Stop",command=stopsong)
stopbtn.config(font=('arial',15),bg="DodgerBlue2",fg="white",padx=8,pady=2)
stopbtn.grid(row=1,column=3)

nextbtn=Button(root,text="Next",command=nextsong)
nextbtn.config(font=('arial',15),bg="DodgerBlue2",fg="white",padx=8,pady=2)
nextbtn.grid(row=1,column=4)



mainloop()