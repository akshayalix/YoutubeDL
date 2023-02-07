# A GUI Yotube video downloader made in python.

# imports

import tkinter
import customtkinter
from pytube import YouTube

# UI

# Global Def :

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title, text_color="white")

        video.download()
    except:
        finishLabel.configure(text="Invalid Link", text_color="red")
    finishLabel.configure(text="Download Completed")

## System Settings

customtkinter.set_appearance_mode('system')
customtkinter.set_default_color_theme('blue')

## App Frame

app = customtkinter.CTk()
app.geometry('720x480')
app.title('Yotube Video Downloader')

## Elements

text_var = tkinter.StringVar(value="Insert a YouTube URL :")

title = customtkinter.CTkLabel(app, textvariable=text_var, font=('Roboto', 15), text_color='cyan')
title.pack(padx=10, pady=10)

## Link input

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, font=('Roboto', 15), width=350, height=40, textvariable=url_var)
link.pack()

## Download Button

download = customtkinter.CTkButton(app, text='Download', command=startDownload)
download.pack(padx=10, pady=10)

# Finished Downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()



# Run App
app.mainloop()