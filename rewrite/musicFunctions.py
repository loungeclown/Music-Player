#dk why i need to import stuff here as well :p
from tkinter import *
from tkinter import messagebox, filedialog
import tkinter.ttk as ttk

from ttkthemes import ThemedTk
from pygame import mixer


#functions file

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select an audio file",
                                          filetypes = (("Audio Files", "*.mp3*"), ("All files", "*.*")))
    mixer.music.load(filename)

def info():
    messagebox.showinfo("Credit", credit)

def github():
    messagebox.showinfo("Github", github)

def exit():
    quit()

def play():
    mixer.music.play()

def pause():
    mixer.music.pause()

def resume():
    mixer.music.unpause()

def stop():
    mixer.music.stop()

def queue():
    queuefile = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select an audio file",
                                          filetypes = (("Audio Files", "*.mp3*"), ("All files", "*.*")))
    mixer.music.queue(queuefile)
    





#variables
credit = '''Program written by
Aman Bele.
Rewritten by me as well.'''
github = '''https://github.com/loungeclown
gotta change soon :D'''

