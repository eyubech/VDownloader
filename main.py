import tkinter as tk
import pytube
from tkinter import messagebox, filedialog

root = tk.Tk()
root.title('YTDownloader')
root.geometry('450x250')
root.resizable(False, False)
root.config(background='brown1')
title = tk.Label(root, text='YouTube Downloader',font=('Helvatical',25,'bold'),background=('brown1')).pack()


download_Path = tk.StringVar()
def Browse():
    download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH")
    download_Path.set(download_Directory)


lien_var = tk.StringVar()
def url():
    lien = lien_var.get()
    youtube = pytube.YouTube(lien)
    video = youtube.streams.first()

    folder = download_Path.get()
    video.download(folder)
    lien_var.set("")
    tk.messagebox.showinfo(title='Download', message='Done')

get_info = tk.Label(root, text="Enter Download Path : ").pack()

download_path = tk.Entry(root, width='50', textvariable=download_Path).pack()

choose_folder = tk.Button(root, text="Browse", command=Browse).pack()

tk.Label(root, ).pack()

link_here = tk.Label(root, text="Enter YT Link : ").pack()

entry = tk.Entry(root, width='50', textvariable=lien_var).pack()

btt = tk.Button(root,text='Download',command=url).pack()



root.mainloop()
