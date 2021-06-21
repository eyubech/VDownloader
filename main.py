#libraries
import tkinter as tk
import pytube
from tkinter import messagebox

root = tk.Tk()
root.title('VDownloader')
root.geometry('500x150')

lien_var = tk.StringVar()
#fonction
def url():
    # to get url from Entry
    lien = lien_var.get()
    youtube = pytube.YouTube(lien)
    video = youtube.streams.first()

    #video locatio
    video.download('/home/ayoub/')
    lien_var.set("")
    tk.messagebox.showinfo(title='Download', message='Done')

title = tk.Label(root, text='youtube downloader',font=('Helvatical',30,'bold')).pack()

entry = tk.Entry(root, width='50', textvariable=lien_var).pack()

btt = tk.Button(root,text='Download',command=url).pack()


root.mainloop()