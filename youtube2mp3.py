import pafy
import os
from tkinter import Menu
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import Tk
from tkinter import Frame
from tkinter import Label
from tkinter import IntVar
from tkinter import SOLID
from tkinter import Entry
from tkinter import Radiobutton
from tkinter import Button
from tkinter import DISABLED
from tkinter import HORIZONTAL
from tkinter import END
from tkinter import W
import json
import webbrowser
from pytube import YouTube 
import re
from mutagen.mp3 import MP3
class MenuBar(Menu):
    def __init__(self, ws):
        Menu.__init__(self, ws)

        file = Menu(self, tearoff=False)
        file.add_command(label="Open Config",command=self.openConfig)    
        file.add_separator()
        file.add_command(label="Exit", underline=1, command=self.quit)
        self.add_cascade(label="File",underline=0, menu=file)

        help = Menu(self, tearoff=0)  
        help.add_command(label="About", command=self.about)  
        help.add_command(label="Release Notes", command=self.release)  
        help.add_command(label="Instructions", command=self.instruction)  

        self.add_cascade(label="Help", menu=help)  

    def openConfig(self):
        curr_directory = os.getcwd()
        try:
            os.system("notepad config.json")
        except Exception as e:
            messagebox.showerror('Error', str(e)+'\nCannot locate config.json at ' + curr_directory)

    def exit(self):
        self.exit
    def release(self):
        webbrowser.open('https://github.com/jinlee487/youtube2mp3')
    def instruction(self):
        curr_directory = os.getcwd()
        try:
            os.system("notepad instruction.txt")
        except Exception as e:
            messagebox.showerror('Error', str(e)+'\nCannot locate instruction.txt at ' + curr_directory)
    def about(self):
        messagebox.showinfo('About', 'This is an open source youtube audio/video downloader made by me, Jinlee487.' 
                    +' I will not assume any responsibility of others using this resource in any fashion.')

class GUI(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.style = ttk.Style()
        self.style.theme_use("winnative")
        self.videoOrAudio = IntVar()
        self.title('youtube2mp3')
        self.geometry('575x500')
        frame = Frame(self,bd=2, relief=SOLID, padx=10, pady=10)

        Label(frame, text="URL", font=('Times', 14)).grid(row=0, column=0, sticky=W, pady=10)
        Label(frame, text="Task", font=('Times', 14)).grid(row=1, column=0, sticky=W, pady=10)
        Label(frame, text="Info", font=('Times', 14)).grid(row=2, column=0, sticky=W, pady=10)
        Label(frame, text="Path", font=('Times', 14)).grid(row=4, column=0, sticky=W, pady=10)
        Label(frame, text="Progress", font=('Times', 14)).grid(row=5, column=0, sticky=W, pady=10)
        self.reg_url = Entry(frame, font=('Times', 14), width=40)
        video_rb = Radiobutton(frame, font=('Times', 14), text="video", variable=self.videoOrAudio, value=1)
        audio_rb = Radiobutton(frame, font=('Times', 14), text="audio", variable=self.videoOrAudio, value=2)
        self.videoOrAudio.set(2)
        reg_search = Button(frame, width=10, text='Search', font=('Times', 14), command=self.searchURL)

        self.downloadPath = Entry(frame, font=('Times', 14), width=28,state=DISABLED)
        path_btn = Button(frame, width=4, text='new', font=('Times', 14), command=self.changeDownloadPath)

        self.pb1 = ttk.Progressbar(frame, orient=HORIZONTAL, length=120, mode='indeterminate')

        download_btn = Button(frame, width=10, text='Download', font=('Times', 14), command=self.downloadStream)
        cancel_btn = Button(frame, width=10, text='Cancel', font=('Times', 14), command=self.destroy)

        self.EventText = scrolledtext.ScrolledText(frame,font=('Times', 14), height=5, width=38)
        self.downloadText = scrolledtext.ScrolledText(frame,font=('Times', 14), height=3, width=38)

        self.reg_url.grid(row=0, column=1, columnspan=10, pady=2, padx=2)
        video_rb.grid(row=1, column=1, pady=2, padx=2)
        audio_rb.grid(row=1, column=2, pady=2, padx=2)
        reg_search.grid(row=1, column=3, pady=2, padx=2)
        self.EventText.grid(row=2, column=1, columnspan=10, pady=3, padx=2)

        self.downloadPath.grid(row=4, column=1, columnspan=3, pady=2, padx=2)
        path_btn.grid(row=4, column=4)

        self.downloadText.grid(row=5, column=1, columnspan=10, pady=3, padx=2)

        self.pb1.grid(row=7, column=1, columnspan=2, pady=3, padx=2)
        download_btn.grid(row=7, column=4, pady=2, padx=2)
        cancel_btn.grid(row=7, column=3, pady=2, padx=2)
        frame.place(x=50, y=50)

        menubar = MenuBar(self)  
        self.config(menu=menubar)
        self.readConfig()

    def start_pb(self):
        # not used
        self.pb1.start(100)   
        
    def end_pb(self):
        # not used
        self.pb1.stop()

    def searchURL(self):
        self.currentUrl = self.reg_url.get()
        self.EventText.delete(1.0, END)
        self.downloadText.delete(1.0, END)
        self.EventText.insert("end","URL: " + str(self.currentUrl) +"\n")
        self.currentStream = ""
        try:
            file = pafy.new(self.currentUrl)
            self.title = re.sub("[#%&*:<>?/{|}]", "_", str(file.title))
            self.EventText.insert("end","TITLE: " + str(file.title) + "\n")
            self.EventText.insert("end","AUTHOR: " + str(file.author) + "\n")
            self.EventText.insert("end","RATING: " +  str(file.rating) + "\n")
            self.EventText.insert("end","VIEWCOUNT: " +  str(file.viewcount) + "\n")
            self.EventText.insert("end","DURATION: " +  str(file.duration) + "\n")
            self.EventText.insert("end","LIKES: " +  str(file.likes) + "\n")
            self.EventText.insert("end","DISLIKES: " +  str(file.dislikes) + "\n")
        except Exception as e:
            messagebox.showwarning("Warning", str(e) + "\nPleae try again with different URL")
        return

    def downloadStream(self):
        ext = ".mp3"
        try:
            file = YouTube(self.currentUrl) 
            if(self.videoOrAudio.get() == 1):
                ext = ".mp4"
                streams = file.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            elif(self.videoOrAudio.get() == 2):
                ext = ".mp3"
                streams = file.streams.filter(only_audio=True).first()
            self.currentStream = streams
        except Exception as e:
            messagebox.showwarning("Warning", str(e) + "\nPlease try again with different URL")
            return
        try: 
            destination = os.path.normpath(self.downloadPath.get())
            self.downloadText.delete(1.0, END)
            self.downloadText.insert("end","")
            self.fulltitle = self.title + ext
            if(self.check()==False):
                return
        except Exception as e:
            messagebox.showwarning("Warning", str(e) + "\nPlease select the file you would like to download")
            return
        try:
            out_file = self.currentStream.download(output_path=destination)
            new_file = os.path.join(destination.strip(),self.fulltitle.strip())
            os.rename(out_file, new_file)
            self.downloadText.insert(1.0,"Succefully saved file at location \n" + destination + "\n")
        except Exception as e:
            messagebox.showwarning("Warning", str(e) + "\nPleae try again with different URL")
            return
        try:
            print(new_file)
            if (os.path.isfile(new_file)==True):
                print(True)
            else:
                print(False)

            mp3 = MP3(new_file)
            mp3.pprint()
            mp3.delete()
            mp3.save()
        except Exception as e:
            messagebox.showwarning("Warning", str(e) + "\nFile downloaded, but failed to remove metadata")
            return
    def check(self):
        destination = self.downloadPath.get()
        if (os.path.isfile(os.path.join(destination.strip(),self.fulltitle.strip()))==True):
            messagebox.showwarning("Warning", "File with identical name found in location: \n" + destination+"\\"+self.fulltitle + "\n Please remove identical file")
            return False
        elif destination.strip() == "":
            messagebox.showwarning("Warning", "Download file path is empty")
            return False  

    def readConfig(self):
        curr_directory = os.getcwd()
        try:
            f = open('config.json')
            data = json.load(f)
            if 'directory' not in data:
                raise ValueError()
            path = data['directory']
            self.downloadPath.configure(state='normal')
            self.downloadPath.delete("0", "end")
            self.downloadPath.insert("end",path)
            self.downloadPath.configure(state=DISABLED)
        except ValueError as e:
            messagebox.showerror('Error', str(e)+'\nCannot find directory key in config.json. Check if config.json has been modified.')
        except Exception as e: 
            messagebox.showerror('Error', str(e)+'\nCannot locate config.json at ' + curr_directory)

    def changeDownloadPath(self):
        dir_name = filedialog.askdirectory()  
        if(dir_name == ""):
            return
        with open("config.json", "r") as jsonFile:
            data = json.load(jsonFile)

        data["directory"] = dir_name

        with open("config.json", "w") as jsonFile:
            json.dump(data, jsonFile)

        self.readConfig()

if __name__ == "__main__":
    
    ws=GUI()
    ws.mainloop()




