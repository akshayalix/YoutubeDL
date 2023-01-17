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

menuframe = customtkinter.CTkFrame(app,
            width=720, height=20,
            corner_radius=1, fg_color='#4a4a4a'
            )
menuframe.pack(expand=True , fill=tkinter.X, anchor='n')

## Menu Buttons

btnfolder = customtkinter.CTkButton(app,
            width=40, height=20, border_width=0,
            corner_radius=8, text="Open Folder"
            )
btnfolder.place(rely=0.5, anchor='nw')

btnabout = customtkinter.CTkButton(app,
            width=40, height=20, border_width=0,
            corner_radius=8, text="About"
            )
btnabout.place(rely=0.5, anchor='e')





# Run App
app.mainloop()