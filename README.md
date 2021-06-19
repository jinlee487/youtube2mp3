

# youtube2mp3
custom Youtube video to mp3 converter 3.01
### 👋 Introduction 

Hello World! 

I was working on recording videos and needed audio clips from Youtube.
I could use Youtube to mp3 conversion service sites... but I am a programmer. 
So I went ahead and created a simple script to download Youtube audios straight from Youtube.
This Python script uses Tkinter for the GUI design and pafy to download youtube streams.

Please message me with any feedback, I am happy talk :)

<img src="https://user-images.githubusercontent.com/46912607/120653042-4c1f9a00-c4bb-11eb-9e2e-79c13aebbc20.PNG" width="300">

### 📑 How to Install and Run

1. Download the youtube2mp3 3.01 zip file from the lastest published releases.
2. After you first download the zip folder, unzip the folder in your location of choice.
3. Then create a quick a shortcut of the youtube2mp3.exe file for access.
4. Make sure to choose a file download destination before you start downloading files.
5. Start downloading
### 📑 Things to Note 

...
### 📑 References
- `downloading virtual env` : [https://python-guide-kr.readthedocs.io/ko/latest/dev/virtualenvs.html](https://python-guide-kr.readthedocs.io/ko/latest/dev/virtualenvs.html)
- `using pafy` : [https://www.geeksforgeeks.org/youtube-mediaaudio-download-using-python-pafy/]( https://www.geeksforgeeks.org/youtube-mediaaudio-download-using-python-pafy/)
- `pythonguides.com` : [https://pythonguides.com/?s=tkinter](https://pythonguides.com/?s=tkinter)
- others: 
- [https://python-guide-kr.readthedocs.io/ko/latest/dev/virtualenvs.html]
- [https://www.geeksforgeeks.org/python-gui-tkinter/]
- [https://www.geeksforgeeks.org/youtube-mediaaudio-download-using-python-pafy/]
- [https://github.com/grassfedfarmboi/tkinter_template]
- [https://github.com/ajinkyapadwad/Sample-GUI-Tkinter]
- [https://github.com/mps-youtube/pafy/issues/41]
- [https://stackoverflow.com/questions/754307/regex-to-replace-characters-that-windows-doesnt-accept-in-a-filename]

### 📑 Release Notes
2.00
- created a GUI 
- downdable youtube audio streams
- only compatable with Windows

3.00    
- switched from pafy to pytube due to a bug with pafy's remux_audio in download parameter options.
- fixed the encoding problem so that iTunes can read the downloaded M4A file correctly.
- fixed file name with regrex
- mp4 and mp3 downloadable
- automatically chooses highest quality files

    Possible future releases ... 
    - better GUI 
    - IOS compatable
    - working progress bar

3.01
- removed pafy due to out of date bugs
- added moviepy to convert mp4 into mp3
- added temp file name function
3.02
- upgraded pytube version [https://stackoverflow.com/questions/67614883/pytube-givng-an-http-error-404-not-found-error-anyone-knows-how-to-fix-this]
### 👋 DISCLAIMER!!!
- This is an open source youtube audio/video downloader made by me, Jinlee487. I will not assume any responsibility of others using this resource in any fashion.


Author: <a href="https://github.com/jinlee487">JWL</a>
