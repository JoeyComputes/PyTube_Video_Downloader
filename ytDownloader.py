from pytube import YouTube
import tkinter as tk
from tkinter import messagebox, filedialog, ttk, font
from customtkinter import *
import threading

# Define a function to show the download progress
def progress(stream, chunk, bytes_remaining):
    current = ((stream.filesize - bytes_remaining)/stream.filesize)
    percent = ('{0:.1f}').format(current*100)
    progressbar['value'] = percent
    app.update_idletasks()

# Define a function to download the video
def download_video():
    # Get the YouTube link from the entry field
    link = url_entry.get()
    # Open a file dialog for the user to choose the download directory
    download_folder = filedialog.askdirectory()
    # Create a YouTube object
    yt = YouTube(link, on_progress_callback=progress)
    # Get the stream with the highest resolution
    yd = yt.streams.get_highest_resolution()
    # Download the video
    yd.download(download_folder)
    # Show a success message
    messagebox.showinfo("Success", "Video downloaded successfully")

# Create a Tkinter window
app = CTk()
# Set the size of the window
app.geometry('800x600')
# Set the title of the window
app.title('YouTube Downloader')
set_appearance_mode("dark")

# Create a title label

title_label = tk.Label(master=app, text="YouTube Downloader \n Created by Joey Tosakoon", font=('Helvetica',14,'bold'), bg='black', fg='white')

# Create a label for the entry field
url_label = tk.Label(master=app, text="Enter YouTube link:", font=('Helvetica',14,'bold'), bg='black', fg='white')
# Create an entry field
url_entry = tk.Entry(master=app, font=('Helvetica',12,'normal'), bg='white', fg='black')

# Create a download button that calls the download_video function when clicked
download_button = tk.Button(master=app, text ='Download', command = lambda: threading.Thread(target=download_video).start(), bg='white', fg='black')

# Create a progress bar
progressbar = ttk.Progressbar(master=app, length = 200, mode ='determinate')
progressbartext = tk.Label(master=app, text = '0%', font=('Helvetica',14,'bold'), bg='black', fg='white')

# Place the label, entry field, button, and progress bar on the window
url_label.grid(row=0, column=0, sticky='nsew') # sticky='nsew' means the label will take up all the available space in the row and column
url_entry.grid(row=0, column=1, sticky='nsew')
title_label.grid(row=2, column=1, sticky='nsew')
download_button.grid(row=1, column=1, sticky='nsew')
progressbar.grid(row=1, column=0, sticky='nsew')
progressbartext.grid(row=2, column=0, sticky='nsew')


# Make the rows and columns scale with the window
app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)
app.grid_rowconfigure(2, weight=1)
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)

# Start the Tkinter event loop
app.mainloop()

