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

## Elements

"""text_var = tkinter.StringVar(value="Insert a YouTube URL :")

title = customtkinter.CTkLabel(app, textvariable=text_var, font=('Roboto', 15), text_color='cyan')
title.pack(padx=10, pady=10)"""

## Menu Bar

# Frame

menuframe = customtkinter.CTkFrame(master=app,
            width=720, height=20,
            corner_radius=1, fg_color='#4a4a4a'
            )
menuframe.pack(expand=True , fill=tkinter.X, anchor='n')

## File option menu

filemenu = customtkinter.CTkOptionMenu(
    menuframe, values=["Open Folder"], width=10, height=20,
    dropdown_fg_color='#1f6aa5', dropdown_hover_color='#1f6aa5',
    corner_radius=6
    )
filemenu.pack(anchor='w')
filemenu.set("File")



# Run App
app.mainloop()