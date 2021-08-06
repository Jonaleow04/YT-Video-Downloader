import tkinter as tk
from pytube import YouTube

url = ''

def redo():
    finish.destroy()
    again.destroy()
    enter_url.delete(0, 'end')

def download_video():
    url = enter_url.get()
    yt = YouTube(url).streams.get_highest_resolution()
    yt.download()
    finish.grid(row = 1, column = 0)
    again.grid(row = 1, column = 1)


window = tk.Tk()
window.title('YT Video Downloader')

finish = tk.Label(text = 'Done!')
again = tk.Button(text = 'Click to download new video', command=redo)
button = tk.Button(text = 'Download', command = download_video)
label = tk.Label(text = "Enter video's URL")
enter_url = tk.Entry()

label.grid(row = 0, column = 1, sticky = 'w') 
enter_url.grid(row = 0, column = 0, sticky = 'e')

label.grid(row = 0, column = 0, padx = 10)
enter_url.grid(row = 0, column = 1, padx = 10)
button.grid(row = 0, column = 2, padx = 10)

window.mainloop()