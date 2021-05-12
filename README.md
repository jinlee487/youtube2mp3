

# youtube2mp3
custom Youtube video to mp3 converter
### 👋 Introduction 

Hello World! 

I was working on recording videos and needed audio clips from Youtube.
I could use Youtube to mp3 conversion service sites... but I am a programmer. 
So I went ahead and created a simple script to download Youtube audios straight from Youtube.

### 📑 How to Install and Run

The installation requirements for this python script is 
- python 3
- pafy
- youtube-dl

Once you have python 3 downloaded, follow the instructions below.

1. Clone the repo in your desired location.
2. Run the Powershell commands in the run.txt in order.
3. Download the video.

### Things to Note 
- The videos will be downloaded to your repo location only. pafy only allows downloads in your current path where the script is being run from.
- If you are using virtual env, remember to activate and deactivate the env.
### References
- `downloading virtual env` : [https://python-guide-kr.readthedocs.io/ko/latest/dev/virtualenvs.html](https://python-guide-kr.readthedocs.io/ko/latest/dev/virtualenvs.html)
- `using pafy` : [https://www.geeksforgeeks.org/youtube-mediaaudio-download-using-python-pafy/]( https://www.geeksforgeeks.org/youtube-mediaaudio-download-using-python-pafy/)


Author: <a href="https://github.com/jinlee487">JWL</a>

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