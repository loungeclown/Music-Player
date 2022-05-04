#Rewrite of the music player v1.0 with root window used
from tkinter import *
from tkinter import messagebox, filedialog
import tkinter.ttk as ttk
from ttkthemes import ThemedTk
from pygame import mixer
import musicFunctions as mF
import sv_ttk

mixer.init()

#variables

root = Tk()

#setting the theme
sv_ttk.set_theme("light")

#image files
playImg = PhotoImage(file = "resources/play.png")
stopImg = PhotoImage(file = "resources/stop.png")
resumeImg = PhotoImage(file = "resources/resume.png")
pauseImg = PhotoImage(file = "resources/pause.png")
openImg = PhotoImage(file = "resources/open.png")
closeImg = PhotoImage(file = "resources/close.png")
infoImg = PhotoImage(file = "resources/info.png")
githubImg = PhotoImage(file = "resources/github.png")
musicImg = PhotoImage(file = "resources/music.png")
loopImg = PhotoImage(file = "resources/loop.png")
queueImg = PhotoImage(file = "resources/queue.png")

#resize(ing) the images
pImg = playImg.subsample(2, 2)
sImg = stopImg.subsample(2, 2)
rImg = resumeImg.subsample(2, 2)
paImg = pauseImg.subsample(2, 2)
oImg = openImg.subsample(2, 2)
cImg = closeImg.subsample(2, 2)
iImg = infoImg.subsample(2, 2)
gImg = githubImg.subsample(2, 2)
lImg = loopImg.subsample(2, 2)
qImg = queueImg.subsample(2, 2)

#menu
menubar = Menu(root)
songmenu = Menu(menubar, tearoff=0)

songmenu.add_command(label="Open", command=mF.browseFiles)
songmenu.add_separator()
songmenu.add_command(label="Exit", command=mF.exit)
menubar.add_cascade(label="File", menu=songmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=mF.info)
helpmenu.add_command(label="Github", command=mF.github)
menubar.add_cascade(label="About", menu = helpmenu)

#UI
playButton = Button(root,
                        text="Play",
                        image = pImg,
                        compound = LEFT,
                        command=mF.play).grid(column=0,
                                               row=0,
                                               ipadx=11,
                                               ipady=5)

stopButton = Button(root,
                        text="Stop",   
                        image = sImg,
                        compound = LEFT,
                        command=mF.stop).grid(column=1,
                                               row=0,
                                               ipadx=5,
                                               ipady=5)

pauseButton = Button(root,
                         text="Pause",
                         image = paImg,
                         compound = LEFT,
                         command=mF.pause).grid(column=2,
                                                 row=0,
                                                 ipadx=5,
                                                 ipady=5)

resumeButton = Button(root,
                          text="Resume",
                          image = rImg,
                          compound = LEFT,
                          command=mF.resume).grid(column=3,
                                                   row=0,
                                                   ipadx=5,
                                                   ipady=5)

queueButton = Button(root,
                     text="Queue",
                     image = qImg,
                     compound = LEFT,
                     command=mF.queue).grid(column=0,
                                            row=1,
                                            ipadx=5,
                                            ipady=5)



root.config(menu=menubar)
root.mainloop()

