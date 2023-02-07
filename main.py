# A GUI Yotube video downloader made in python.

# imports

import tkinter
import customtkinter
from pytube import YouTube

# UI

# Global Def :

def startDownload():
    try:
        ytLink = YouTube(link.get())
        stream = ytLink.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        stream.download()
    except:
        print("Youtube link is invalid")
    print("Download Completed")

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
download.pack()





# Run App
app.mainloop()