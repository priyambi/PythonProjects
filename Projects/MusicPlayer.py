from tkinter import *
import pygame  # Pygame is a Python module that works with computer graphics and sound libraries
import os  # OS module for fetching the playlist of songs from the specified directory
root = Tk()  # In order to create an empty window


class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("MusicPlayer")
        self.root.geometry("1000x200+200+200")
        pygame.init()
        pygame.mixer.init()
        self.track = StringVar()
        self.status = StringVar()

        trackframe = LabelFrame(self.root, text="Song Track", font=(
            "times new roman", 17, "bold"), bg="blue", fg="white", bd=5, relief=GROOVE)
        trackframe.place(x=0, y=0, width=600, height=100)

        songtrack = Label(trackframe, textvariable=self.track, width=20, font=(
            "times new roman", 27, "bold"), bg="Orange", fg="yellow").grid(row=0, column=0, padx=10, pady=5)

        trackstatus = Label(trackframe, textvariable=self.status, font=(
            "times new roman", 27, "bold"), bg="orange", fg="yellow").grid(row=0, column=1, padx=10, pady=5)

        # Creating Button Frame
        buttonframe = LabelFrame(self.root, text="Control Panel", font=(
            "times new roman", 17, "bold"), bg="grey", fg="white", bd=5, relief=GROOVE)
        buttonframe.place(x=0, y=100, width=600, height=100)

        playbtn = Button(buttonframe, text="PLAYSONG", command=self.playsong, width=10, height=1, font=(
            "times new roman", 17, "bold"), fg="blue", bg="yellow").grid(row=0, column=0, padx=10, pady=5)

        playbtn = Button(buttonframe, text="PAUSE", command=self.pausesong, width=8, height=1, font=(
            "times new roman", 17, "bold"), fg="blue", bg="yellow").grid(row=0, column=1, padx=10, pady=5)

        playbtn = Button(buttonframe, text="UNPAUSE", command=self.unpausesong, width=10, height=1, font=(
            "times new roman", 17, "bold"), fg="blue", bg="yellow").grid(row=0, column=2, padx=10, pady=5)

        playbtn = Button(buttonframe, text="STOPSONG", command=self.stopsong, width=10, height=1, font=(
            "times new roman", 17, "bold"), fg="blue", bg="yellow").grid(row=0, column=3, padx=10, pady=5)

        # Creating Playlist Frame
        songsframe = LabelFrame(self.root, text="Song Playlist", font=(
            "times new roman", 17, "bold"), bg="grey", fg="white", bd=5, relief=GROOVE)
        songsframe.place(x=600, y=0, width=400, height=200)
        # Inserting scrollbar(optional)
        scrol_y = Scrollbar(songsframe, orient=VERTICAL)

        self.playlist = Listbox(songsframe, yscrollcommand=scrol_y.set, selectbackground="yellow", selectmode=SINGLE, font=(
            "times new roman", 17, "bold"), bg="white", fg="blue", bd=5, relief=GROOVE)

        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)
        # Changing Directory for fetching Songs
        os.chdir(r"C:\Users\HP\Downloads\music")

        songtracks = os.listdir()                   # Fetching Songs

        for track in songtracks:
            self.playlist.insert(END, track)

    def playsong(self):
        self.track.set(self.playlist.get(ACTIVE))
        self.status.set("-Playing")
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        pygame.mixer.music.play()

    def stopsong(self):
        self.status.set("-Stopped")
        pygame.mixer.music.stop()

    def pausesong(self):
        self.status.set("-Paused")
        pygame.mixer.music.pause()

    def unpausesong(self):
        self.status.set("-Playing")
        pygame.mixer.music.unpause()
    root.mainloop()


MusicPlayer(root)
