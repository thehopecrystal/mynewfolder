from tkinter import *
# from pytube import YouTube

# WIDGETS
def widgets():
    # App Title
    headLabel = Label(root, text='YouTube Video Downloader',
                      padx=15, pady=15, font='SegoeUI 14',
                      bg='palegreen1', fg='red')
    
    headLabel.grid(row=1, column=1, padx=5, pady=10, columnspan=3)

    # Label and Entry for YouTube Link
    linkLabel = Label(root, text='YouTube Link',
                      bg='salmon', padx=5, pady=5)
    linkLabel.grid(row=2, column=0, pady=5, padx=5)

    root.linkText = Entry(root, width=35,
                          textvariable=videoLink,
                          font='Arial 14')
    root.linkText.grid(row=2, column=1, padx=5, pady=5, columnspan=2)

    # Label, Entry and Button for the Destination Folder
    destinationLabel = Label(root, text='Destination', bg='salmon',
                             padx=9, pady=5)
    destinationLabel.grid(row=3, column=0, pady=5, padx=5)

    root.destinationText = Entry(root, width=25,
                                 textvariable=downloadPath, font='Arial 14')
    root.destinationText.grid(row=3, column=1, padx=5, pady=5)

    browseBtn = Button(root, text='Browse', width=10,
                       bg='bisque', relief=GROOVE)
    browseBtn.grid(row=3, column=2, padx=1, pady=1)

    # Download Button
    downloadBtn = Button(root, text='Download Video',
                         width=20, bg='thistle',
                         padx=15, pady=10,
                         relief=GROOVE, font='Georgia 14')
    
    downloadBtn.grid(row=4, column=1, pady=20, padx=20)


root = Tk()
root.geometry('1000x500')
root.title('My Awesome YouTube Downloader')
root.config(bg='PaleGreen')

videoLink = StringVar()
downloadPath = StringVar()
widgets()

root.mainloop()