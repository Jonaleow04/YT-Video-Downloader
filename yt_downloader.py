import tkinter as tk
from tkinter import messagebox, filedialog
from pytube import YouTube

class YTdownloader():

    def __init__(self):
        self.window = tk.Tk()
        self.widgets()

    def widgets(self):
        input_label = tk.Label(text = "URL: ")
        input_label.grid(row = 0, column = 0, sticky = 'w', padx = 10) 

        self.download_button = tk.Button(text = 'Download', command = self.download_video)
        self.download_button.grid(row = 2, column = 1, padx = 10)

        self.input_url = tk.Entry(width = 55)
        self.input_url.grid(row = 0, column = 1, sticky = 'e', padx = 10)

        destination_label = tk.Label(text = 'Destination: ')
        destination_label.grid(row = 1, column = 0, sticky = 'w', padx = 10)

        self.download_path = tk.StringVar()
        input_destination = tk.Entry(width = 45, textvariable = self.download_path)
        input_destination.grid(row = 1, column = 1, sticky = 'w', padx = 10)

        destination_button = tk.Button(text = 'Browse', command = self.browse)
        destination_button.grid(row = 1, column = 1, sticky = 'e', padx = 10)

        self.again = tk.Button(text = 'Click to download new video', command=self.redo)
        self.again.grid(row = 2, column = 1)
        self.again.grid_remove()

    def download_video(self):
        url = self.input_url.get()
        download_folder = self.download_path.get()
        yt = YouTube(url).streams.get_highest_resolution()
        yt.download(download_folder)
        self.download_button.grid_remove()
        self.again.grid()
        messagebox.showinfo("Notice", "Video has been downloaded in PATH:\n" + download_folder)

    def browse(self):
        download_Directory = filedialog.askdirectory()
        self.download_path.set(download_Directory)

    def redo(self):
        self.again.grid_remove()
        self.input_url.delete(0, 'end')
        self.download_button.grid()

def main():
    program = YTdownloader()
    program.window.title('YT Video Downloader')
    program.window.mainloop()

if __name__ == '__main__':
    main()