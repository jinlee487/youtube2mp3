
#https://python-guide-kr.readthedocs.io/ko/latest/dev/virtualenvs.html
#https://www.geeksforgeeks.org/youtube-mediaaudio-download-using-python-pafy/
import pafy
import os

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

run()



