# A GUI Yotube video downloader made in python.

# imports

import tkinter
import customtkinter
from pytube import YouTube

# UI

## System Settings

customtkinter.set_appearance_mode('system')
customtkinter.set_default_color_theme('blue')

## App Frame

app = customtkinter.CTk()
app.geometry('720x480')
app.title('Yotube Video Downloader')

# Run App
app.mainloop()