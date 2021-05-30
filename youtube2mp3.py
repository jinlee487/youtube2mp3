import pafy
import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import filedialog
import json
import webbrowser

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
        self.videoOrAudio = 2
        self.title('youtube2mp3')
        self.geometry('575x650')
        frame = Frame(self,bd=2, relief=SOLID, padx=10, pady=10)

        Label(frame, text="URL", font=('Times', 14)).grid(row=0, column=0, sticky=W, pady=10)
        Label(frame, text="Task", font=('Times', 14)).grid(row=1, column=0, sticky=W, pady=10)
        Label(frame, text="Info", font=('Times', 14)).grid(row=2, column=0, sticky=W, pady=10)
        Label(frame, text="Files", font=('Times', 14)).grid(row=3, column=0, sticky=W, pady=10)
        Label(frame, text="Path", font=('Times', 14)).grid(row=4, column=0, sticky=W, pady=10)
        Label(frame, text="Progress", font=('Times', 14)).grid(row=5, column=0, sticky=W, pady=10)
        self.reg_url = Entry(frame, font=('Times', 14), width=40)
        video_rb = Radiobutton(frame, font=('Times', 14), text="video", variable=self.videoOrAudio, value=1, state=DISABLED)
        audio_rb = Radiobutton(frame, font=('Times', 14), text="audio", variable=self.videoOrAudio, value=2) 
        reg_search = Button(frame, width=10, text='Search', font=('Times', 14), command=self.searchURL)

        self.downloadPath = Entry(frame, font=('Times', 14), width=28,state=DISABLED)
        path_btn = Button(frame, width=4, text='new', font=('Times', 14), command=self.changeDownloadPath)

        self.pb1 = ttk.Progressbar(frame, orient=HORIZONTAL, length=120, mode='indeterminate')

        download_btn = Button(frame, width=10, text='Download', font=('Times', 14), command=self.downloadStream)
        cancel_btn = Button(frame, width=10, text='Cancel', font=('Times', 14), command=self.destroy)

        self.EventText = scrolledtext.ScrolledText(frame,font=('Times', 14), height=5, width=38)
        self.tv = ttk.Treeview(frame, columns=(1, 2, 3), show='headings', height=8)
        self.tv['columns']=('index','extension', 'bitrate', 'filesize')
        self.tv.column('#0', width=0, stretch=NO)
        self.tv.column('index', anchor=CENTER, width=50)
        self.tv.column('extension', anchor=CENTER, width=105)
        self.tv.column('bitrate', anchor=CENTER, width=105)
        self.tv.column('filesize', anchor=CENTER, width=105)
        self.tv.heading('#0', text='', anchor=CENTER)
        self.tv.heading('index', text="index")
        self.tv.heading('extension', text="extension")
        self.tv.heading('bitrate', text="bitrate")
        self.tv.heading('filesize', text="filesize(Mb)")
        self.downloadText = scrolledtext.ScrolledText(frame,font=('Times', 14), height=3, width=38)

        self.reg_url.grid(row=0, column=1, columnspan=10, pady=2, padx=2)
        video_rb.grid(row=1, column=1, pady=2, padx=2)
        audio_rb.grid(row=1, column=2, pady=2, padx=2)
        reg_search.grid(row=1, column=3, pady=2, padx=2)
        self.EventText.grid(row=2, column=1, columnspan=10, pady=3, padx=2)
        self.tv.grid(row=3, column=1, columnspan=10, pady=2, padx=2)

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
        url = self.reg_url.get()
        self.EventText.delete(1.0, END)
        self.downloadText.delete(1.0, END)
        self.EventText.insert("end","URL: " + str(url) +"\n")
        for item in self.tv.get_children():
            self.tv.delete(item)
        try:
            file = pafy.new(url)
            self.title = str(file.title).replace("[#%&*:<>?/{|}]", "_")
            self.EventText.insert("end","TITLE: " + str(file.title) + "\n")
            self.EventText.insert("end","AUTHOR: " + str(file.author) + "\n")
            self.EventText.insert("end","RATING: " +  str(file.rating) + "\n")
            self.EventText.insert("end","VIEWCOUNT: " +  str(file.viewcount) + "\n")
            self.EventText.insert("end","DURATION: " +  str(file.duration) + "\n")
            self.EventText.insert("end","LIKES: " +  str(file.likes) + "\n")
            self.EventText.insert("end","DISLIKES: " +  str(file.dislikes) + "\n")

            if(self.videoOrAudio == 1):
                streams = file.streams
            elif(self.videoOrAudio == 2):
                streams = file.audiostreams
            else:
                messagebox.showwarning("Warning","Pleae try again with different URL")
                return

            idx = 0
            for s in streams:
                self.tv.insert(parent='', index=idx, iid=idx, values=(idx,s.extension,s.bitrate,round(s.get_filesize()/1024/1024, 2)))
                idx += 1
            self.currentStream = streams
        except Exception as e:
            messagebox.showwarning("Warning", str(e) + "\nPleae try again with different URL")
        return

    def downloadStream(self):
        def mycb(total, recvd, ratio, rate, eta):
            self.downloadText.insert(1.0,str(recvd) + "\t" + str(ratio) +"\t" + str(eta) + "\n")
        try: 
            path = self.downloadPath.get()
            selected = self.tv.focus()
            temp = self.tv.item(selected, 'values')
            index = int(temp[0])
            self.downloadText.delete(1.0, END)
            self.downloadText.insert("end","")
            self.fulltitle = self.title +"."+ temp[1]
            if(self.check()==False):
                return
        except Exception as e:
            messagebox.showwarning("Warning", str(e) + "\nPlease select the file you would like to download")
            return
        try:
            self.currentStream[index].download(callback=mycb,filepath=path,remux_audio=True)
            self.downloadText.insert(1.0,"Succefully saved file at location \n" + path + "\n")
        except Exception as e:
            messagebox.showwarning("Warning", str(e) + "\nPleae try again with different URL")
            return

    def check(self):
        path = self.downloadPath.get()
        if (os.path.isfile(os.path.join(path.strip(),self.fulltitle.strip()))==True):
            messagebox.showwarning("Warning", "File with identical name found in location: \n" + path+"\\"+self.fulltitle + "\n Please remove identical file")
            return False
        elif path.strip() == "":
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




