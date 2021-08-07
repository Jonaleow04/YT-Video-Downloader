import tkinter as tk
from tkinter import messagebox, filedialog
from pytube import YouTube

def redo():
    again.grid_remove()
    input_url.delete(0, 'end')
    download_button.grid()

def download_video():
    url = input_url.get()
    download_folder = download_path.get()
    yt = YouTube(url).streams.get_highest_resolution()
    yt.download(download_folder)
    download_button.grid_remove()
    again.grid()
    messagebox.showinfo("Notice", "Download is Complete")

def browse():
    download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH")
    download_path.set(download_Directory)

window = tk.Tk()
window.title('YT Video Downloader')

download_path = tk.StringVar()

input_label = tk.Label(text = "URL: ")
input_label.grid(row = 0, column = 0, sticky = 'w', padx = 10) 

download_button = tk.Button(text = 'Download', command = download_video,)
download_button.grid(row = 3, column = 1, padx = 10)

input_url = tk.Entry(width = 55)
input_url.grid(row = 0, column = 1, sticky = 'e', padx = 10)

destination_label = tk.Label(text = 'Destination: ')
destination_label.grid(row = 1, column = 0, sticky = 'w', padx = 10)

input_destination = tk.Entry(width = 45, textvariable = download_path)
input_destination.grid(row = 1, column = 1, sticky = 'w', padx = 10)

destination_button = tk.Button(text = 'Browse', command = browse)
destination_button.grid(row = 1, column = 1, sticky = 'e', padx = 10)

again = tk.Button(text = 'Click to download new video', command=redo)
again.grid(row = 3, column = 1)
again.grid_remove()

window.mainloop()