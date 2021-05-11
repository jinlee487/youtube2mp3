
# https://python-guide-kr.readthedocs.io/ko/latest/dev/virtualenvs.html
# https://www.geeksforgeeks.org/python-gui-tkinter/
# https://www.geeksforgeeks.org/youtube-mediaaudio-download-using-python-pafy/
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
# import tkinter as tk
import tkinter.messagebox as tkMessageBox

# globally declare the expression variable
url = ""
# Driver code
if __name__ == "__main__":
    # create a GUI window
    gui = Tk()
 
    menu = Menu(gui)
    gui.config(menu=menu)
    gui.title('youtube2mp3')
    filemenu = Menu(menu)
    menu.add_cascade(label='File', menu=filemenu)
    filemenu.add_command(label='New')
    filemenu.add_command(label='Open...')
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=gui.quit)
    helpmenu = Menu(menu)
    menu.add_cascade(label='Help', menu=helpmenu)
    helpmenu.add_command(label='About')

    # set the background colour of GUI window
    gui.configure(background="#f2f2f2")
 
    # set the title of GUI window
    gui.title("youtube2mp3")
 
    # set the configuration of GUI window
    gui.geometry("500x500")

    # StringVar() is the variable class
    # we create an instance of this class
    url = StringVar()
 
    # create the text entry box for
    # showing the url .
    Label(gui, text='url').grid(row=0,rowspan=2,column=0)
    url_field = Entry(gui, textvariable=url,width=60)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    url_field.grid(row=0,rowspan=2, column=1, columnspan=4)

    v = IntVar()
    r1=Radiobutton(gui, text='Video', variable=v, value=1)
    r2=Radiobutton(gui, text='Audio', variable=v, value=2)
    r1.grid(row=0, column=5)
    r2.grid(row=1, column=5)
    # start the GUI
    gui.mainloop()
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



