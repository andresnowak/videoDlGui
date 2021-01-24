import tkinter as tk
from tkinter import ttk
from videoDl import *
import time


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.text_url = tk.Label(self.master, width=15, text="Enter Url: ")
        self.text_url.grid(row=0, column=0, padx=5, pady=10)
        self.url = tk.Entry(self.master, width=40,
                            borderwidth=5)
        self.url.grid(row=0, column=1, columnspan=3, padx=10, pady=10)

        self.text_name_file = tk.Label(
            self.master, width=25, text="Enter Name of file: ")
        self.text_name_file.grid(row=1, column=0, padx=5, pady=10)
        self.name_file = tk.Entry(
            self.master, width=40, borderwidth=5)
        self.name_file.grid(row=1, column=1, columnspan=3, padx=10, pady=10)

        self.video_dl = tk.Button(
            self.master, width=25, text="Download as video")
        self.video_dl["command"] = self.download_video
        self.video_dl.grid(row=2, column=0, padx=10, pady=10)

        self.music_dl = tk.Button(
            self.master, width=25, text="Download as audio")
        self.music_dl["command"] = self.download_music
        self.music_dl.grid(row=2, column=2, padx=10, pady=10)

    def download_video(self):
        name_file = self.name_file.get()
        url = self.url.get()

        mp4Option(self.name_file.get(), self.url.get())

        self.delete_entries_text(len(name_file), len(url))

    def download_music(self):
        name_file = self.name_file.get()
        url = self.url.get()

        wavOption(name_file, url)

        self.delete_entries_text(len(name_file), len(url))

    def delete_entries_text(self, name_file_len, url_len):
        self.name_file.delete(0, name_file_len)
        self.url.delete(0, url_len)


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.master.title("VideoDl")
    app.master.minsize(300, 400)
    app.mainloop()
