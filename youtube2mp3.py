
# https://python-guide-kr.readthedocs.io/ko/latest/dev/virtualenvs.html
# https://www.geeksforgeeks.org/python-gui-tkinter/
# https://www.geeksforgeeks.org/youtube-mediaaudio-download-using-python-pafy/
# https://github.com/grassfedfarmboi/tkinter_template
# https://github.com/ajinkyapadwad/Sample-GUI-Tkinter
# M4A files are encoded with the lossy Advanced Audio Coding (AAC) codec,
# which is able to provide the same bitrates as MP3s, yet achieve tighter compression.
# This results in smaller file sizes, all while delivering higher audio quality.
# YouTube supports the following video formats for upload: 
# 3GPP, AVI, FLV, MOV, MPEG4, MPEGPS, WebM and WMV. 
# MPEG4 commonly uses the . mp4 file extension. 
# YouTube also recommends specific encoding settings for optimal conversion.
import pafy
import os


from tkinter import *
from tkinter import Tk, ttk
import tkinter as tk
import PIL 
# from PIL import ImageTk,Image


class Example(Frame):

    def __init__(self, parent):
        # bg = Image.open("bg.jpg")
        # background_image=ImageTk.PhotoImage(bg)
        # background_label = Label(parent, image=background_image)
        # background_label.place(x=0, y=0, relwidth=1, relheight=1)
        

        Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title("User Setup")
        self.style = ttk.Style()
        self.style.theme_use("default")
        self.centreWindow()
        self.pack(fill=BOTH, expand=1)
        
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Exit", command=self.quit)
        # menubar.add_cascade(label="File", menu=fileMenu)

        firstNameLabel = Label(self, text="Username")
        firstNameLabel.grid(row=0, column=0, sticky=W+E)
        lastNameLabel = Label(self, text="Password")
        lastNameLabel.grid(row=1, column=0, sticky=W+E)
        countryLabel = Label(self, text="Country")
        countryLabel.grid(row=2, column=0, sticky=W+E)
        addressLabel = Label(self, text="Address")
        addressLabel.grid(row=3, column=0, pady=10, sticky=W+E+N)
        
        firstNameText = Entry(self, width=20)
        firstNameText.grid(row=0, column=1, padx=5, pady=5, ipady=2, sticky=W+E)
        lastNameText = Entry(self, width=20)
        lastNameText.grid(row=1, column=1, padx=5, pady=5, ipady=2, sticky=W+E)
        
        self.countryVar = StringVar()
        self.countryCombo = ttk.Combobox(self, textvariable=self.countryVar)
        self.countryCombo['values'] = ('United States', 'United Kingdom', 'France')
        self.countryCombo.current(1)
        self.countryCombo.bind("<<ComboboxSelected>>", self.newCountry)
        self.countryCombo.grid(row=2, column=1, padx=5, pady=5, ipady=2, sticky=W)
        
        addressText = Text(self, padx=5, pady=5, width=20, height=6)
        addressText.grid(row=3, column=1, padx=5, pady=5, sticky=W)
        
        
        self.titleVar = StringVar()
        self.titleVar.set("[User Status]")
        Label(self, textvariable=self.titleVar).grid(
            row=4, column=1, sticky=W+E
        )   # a reference to the label is not retained
        
        title = ['Admin', 'End-user', 'Programmer']
        titleList = Listbox(self, height=5)
        for t in title:
            titleList.insert(END, t)
        titleList.grid(row=3, column=2, columnspan=2, pady=5, sticky=N+E+S+W)
        titleList.bind("<<ListboxSelect>>", self.newTitle)
        
        okBtn = Button(self, text="OK", width=10, command=self.onConfirm)
        okBtn.grid(row=4, column=2, padx=5, pady=3, sticky=W+E)
        closeBtn = Button(self, text="Close", width=10, command=self.onExit)
        closeBtn.grid(row=4, column=3, padx=5, pady=3, sticky=W+E)
    
    def centreWindow(self):
        w = 450
        h = 295
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def onExit(self):
        self.quit()
    
    def newCountry(self, event):
        print(self.countryVar.get())
    
    def fullChecked(self):
        if self.fullTimeVar.get() == 1:
            self.parent.title("Simple Window (full-time)")
        else:
            self.parent.title("Simple Window")
    
    def newTitle(self, val):
        sender = val.widget
        idx = sender.curselection()
        value = sender.get(idx)
        self.titleVar.set(value)
    
    def onConfirm(self):
        box.showinfo("Information", "Thank you!")

def main():
    root = Tk()

    root.resizable(width=TRUE, height=TRUE)
    # resizable

    app = Example(root)

    # img = ImageTk.PhotoImage(Image.open("logo.jpg"))
    # panel = Label(root, image = img)
    # panel.pack(side = "bottom", fill = "both", expand = "no")

    root.mainloop()

if __name__ == '__main__':
    main()













import tkinter
# Lots of tutorials have from tkinter import *, but that is pretty much always a bad idea
from tkinter import ttk
import abc

class Menubar(ttk.Frame):
    """Builds a menu bar for the top of the main window"""
    def __init__(self, parent, *args, **kwargs):
        ''' Constructor'''
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.init_menubar()

    def on_exit(self):
        '''Exits program'''
        quit()

    def display_help(self):
        '''Displays help document'''
        pass

    def display_about(self):
        '''Displays info about program'''
        pass

    def init_menubar(self):
        self.menubar = tkinter.Menu(self.root)
        self.menu_file = tkinter.Menu(self.menubar) # Creates a "File" menu
        self.menu_file.add_command(label='Exit', command=self.on_exit) # Adds an option to the menu
        self.menubar.add_cascade(menu=self.menu_file, label='File') # Adds File menu to the bar. Can also be used to create submenus.

        self.menu_help = tkinter.Menu(self.menubar) #Creates a "Help" menu
        self.menu_help.add_command(label='Help', command=self.display_help)
        self.menu_help.add_command(label='About', command=self.display_about)
        self.menubar.add_cascade(menu=self.menu_help, label='Help')

        self.root.config(menu=self.menubar)

class Window(ttk.Frame):
    """Abstract base class for a popup window"""
    __metaclass__ = abc.ABCMeta
    def __init__(self, parent):
        ''' Constructor '''
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        self.parent.resizable(width=False, height=False) # Disallows window resizing
        self.validate_notempty = (self.register(self.notEmpty), '%P') # Creates Tcl wrapper for python function. %P = new contents of field after the edit.
        self.init_gui()

    @abc.abstractmethod # Must be overwriten by subclasses
    def init_gui(self):
        '''Initiates GUI of any popup window'''
        pass

    @abc.abstractmethod
    def do_something(self):
        '''Does something that all popup windows need to do'''
        pass

    def notEmpty(self, P):
        '''Validates Entry fields to ensure they aren't empty'''
        if P.strip():
            valid = True
        else:
            print("Error: Field must not be empty.") # Prints to console
            valid = False
        return valid

    def close_win(self):
        '''Closes window'''
        self.parent.destroy()

class SomethingWindow(Window):
    """ New popup window """

    def init_gui(self):
        self.parent.title("New Window")
        self.parent.columnconfigure(0, weight=1)
        self.parent.rowconfigure(3, weight=1)

        # Create Widgets

        self.label_title = ttk.Label(self.parent, text="This sure is a new window!")
        self.contentframe = ttk.Frame(self.parent, relief="sunken")

        self.label_test = ttk.Label(self.contentframe, text='Enter some text:')
        self.input_test = ttk.Entry(self.contentframe, width=30, validate='focusout', validatecommand=(self.validate_notempty))

        self.btn_do = ttk.Button(self.parent, text='Action', command=self.do_something)
        self.btn_cancel = ttk.Button(self.parent, text='Cancel', command=self.close_win)

        # Layout
        self.label_title.grid(row=0, column=0, columnspan=2, sticky='nsew')
        self.contentframe.grid(row=1, column=0, columnspan=2, sticky='nsew')

        self.label_test.grid(row=0, column=0)
        self.input_test.grid(row=0, column=1, sticky='w')

        self.btn_do.grid(row=2, column=0, sticky='e')
        self.btn_cancel.grid(row=2, column=1, sticky='e')

        # Padding
        for child in self.parent.winfo_children():
            child.grid_configure(padx=10, pady=5)
        for child in self.contentframe.winfo_children():
            child.grid_configure(padx=5, pady=2)

    def do_something(self):
        '''Does something'''
        text = self.input_test.get().strip()
        if text:
            # Do things with text
            self.close_win()
        else:
            print("Error: But for real though, field must not be empty.")

class GUI(ttk.Frame):
    """Main GUI class"""
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.init_gui()

    def openwindow(self):
        self.new_win = tkinter.Toplevel(self.root) # Set parent
        SomethingWindow(self.new_win)

    def init_gui(self):
        self.root.title('Test GUI')
        self.root.geometry("600x400")
        self.grid(column=0, row=0, sticky='nsew')
        self.grid_columnconfigure(0, weight=1) # Allows column to stretch upon resizing
        self.grid_rowconfigure(0, weight=1) # Same with row
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.option_add('*tearOff', 'FALSE') # Disables ability to tear menu bar into own window
        
        # Menu Bar
        self.menubar = Menubar(self.root)
        
        # Create Widgets
        self.btn = ttk.Button(self, text='Open Window', command=self.openwindow)

        # Layout using grid
        self.btn.grid(row=0, column=0, sticky='ew')

        # Padding
        for child in self.winfo_children():
            child.grid_configure(padx=10, pady=5)

if __name__ == '__main__':
    root = tkinter.Tk()
    GUI(root)
    root.mainloop()





















# from tkinter import *
# # import tkinter as tk
# import tkinter.messagebox as tkMessageBox

# # globally declare the expression variable
# url = ""
# # Driver code
# if __name__ == "__main__":
#     # create a GUI window
#     gui = Tk()
 
#     menu = Menu(gui)
#     gui.config(menu=menu)
#     gui.title('youtube2mp3')
#     filemenu = Menu(menu)
#     menu.add_cascade(label='File', menu=filemenu)
#     filemenu.add_command(label='New')
#     filemenu.add_command(label='Open...')
#     filemenu.add_separator()
#     filemenu.add_command(label='Exit', command=gui.quit)
#     helpmenu = Menu(menu)
#     menu.add_cascade(label='Help', menu=helpmenu)
#     helpmenu.add_command(label='About')

#     # set the background colour of GUI window
#     gui.configure(background="#f2f2f2")
 
#     # set the title of GUI window
#     gui.title("youtube2mp3")
 
#     # set the configuration of GUI window
#     gui.geometry("500x500")

#     # StringVar() is the variable class
#     # we create an instance of this class
#     url = StringVar()
 
#     # create the text entry box for
#     # showing the url .
#     Label(gui, text='url').grid(row=0,rowspan=2,column=0)
#     url_field = Entry(gui, textvariable=url,width=60)

#     # grid method is used for placing
#     # the widgets at respective positions
#     # in table like structure .
#     url_field.grid(row=0,rowspan=2, column=1, columnspan=4)

#     v = IntVar()
#     r1=Radiobutton(gui, text='Video', variable=v, value=1)
#     r2=Radiobutton(gui, text='Audio', variable=v, value=2)
#     r1.grid(row=0, column=5)
#     r2.grid(row=1, column=5)
#     # start the GUI
#     gui.mainloop()
# def proces():
#     try:
#         number1=Entry.get(E1)
#         number2=Entry.get(E2)
#         operator=Entry.get(E3)
#         number1=int(number1)
#         number2=int(number2)
#         if operator =="+":
#             answer=number1+number2
#         if operator =="-":
#             answer=number1-number2
#         if operator=="*":
#             answer=number1*number2
#         if operator=="/":
#             answer=number1/number2
#         Entry.insert(E4,0,answer)
#         print(answer)
#     except ValueError:
#         tkMessageBox.showwarning("Warning","Please enter the value in integer")
#     except :
#         tkMessageBox.showwarning("Warning","Pleae try again with different input")

# root = Tk()
# menu = Menu(root)
# root.config(menu=menu)
# root.title('youtube2mp3')
# filemenu = Menu(menu)
# menu.add_cascade(label='File', menu=filemenu)
# filemenu.add_command(label='New')
# filemenu.add_command(label='Open...')
# filemenu.add_separator()
# filemenu.add_command(label='Exit', command=root.quit)
# helpmenu = Menu(menu)
# menu.add_cascade(label='Help', menu=helpmenu)
# helpmenu.add_command(label='About')
# v = IntVar()
# Radiobutton(root, text='GfG', variable=v, value=1).pack(anchor=W)
# Radiobutton(root, text='MIT', variable=v, value=2).pack(anchor=W)
# scrollbar = Scrollbar(root)
# scrollbar.pack( side = RIGHT, fill = Y )
# mylist = Listbox(root, yscrollcommand = scrollbar.set )
# for line in range(100):
#    mylist.insert(END, 'This is line number' + str(line))
# mylist.pack( side = LEFT, fill = BOTH )
# scrollbar.config( command = mylist.yview )

# master = Tk()
# w = Canvas(master, width=500, height=500)
# w.pack()
# Label(w, text='url').grid(row=0)
# e1 = Entry(w)
# e2 = Entry(w)
# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)
# mainloop()

# top = Tk()
# L1 = Label(top, text="My calculator",).grid(row=0,column=1)
# L2 = Label(top, text="Number 1",).grid(row=1,column=0)
# L3 = Label(top, text="Number 2",).grid(row=2,column=0)
# L4 = Label(top, text="Operator",).grid(row=3,column=0)
# L4 = Label(top, text="Answer",).grid(row=4,column=0)
# E1 = Entry(top, bd =5)
# E1.grid(row=1,column=1)
# E2 = Entry(top, bd =5)
# E2.grid(row=2,column=1)
# E3 = Entry(top, bd =5)
# E3.grid(row=3,column=1)
# E4 = Entry(top, bd =5)
# E4.grid(row=4,column=1)
# B=Button(top, text ="Submit",command = proces).grid(row=5,column=1,)


def run():
    url = input("\ninput youtube video link below.\n")
    print("\nrequested url:"  +url)
    video= pafy.new(url)
    print("title: " + video.title)
    # print(video.rating)
    # print(video.viewcount)
    print("account: ", video.author)
    print("length: ", video.length)
    # print(video.duration, video.likes, video.dislikes, video.description)
    audiostreams = video.audiostreams
    count = 0
    for i in audiostreams: 
        print('index: %s, bitrate: %s, ext: %s, size:%0.2fMb' % (count,i.bitrate, i.extension, i.get_filesize()/1024/1024))
        count+=1
    index = int(input("\nchoose the file you want to download\n"))
    print("you chose index: %s\n bitrate: %s, ext: %s, size:%0.2fMb" % (index, audiostreams[index].bitrate, audiostreams[index].extension, audiostreams[index].get_filesize()/1024/1024))
    choice = input("\n작업을 계속 진행하고 싶으시면 Y 아니면 y 를 입력해주세요.\n\n").strip()
    if choice == "Y" or choice == "y":
        try:
            audiostreams[index].download()
            # bestaudio = video.getbestaudio()
            # bestaudio.download()
            cwd = os.getcwd()
            print("\n다음 경로로 \n\n"+cwd+"\n\n  "+video.title+"\n\n  파일을 성공적으로 저장하였습니다.\n")
            print("\nOperation successful.....Terminating the program.\n")
        except Exception as e:
            print("\n\nAn exception occurred!\n")
            print(e)
            print("\n\t.........Terminating the program.\n\n\n")
    else:
        print("\n.....Terminating the program.\n")
    quit()

# run()



