from pytube import YouTube
from tqdm import tqdm
import time
from sys import argv

def compet():

    print("\nDownloading Complete")

def progress(stream, chunk, bytes_remaining):
   
    bytes_downloaded = stream.filesize - bytes_remaining
    for bytes_downloaded in tqdm(range(stream.filesize)):
        continue



link = input('Enter the Link \n')
yt = YouTube(link)  
print("Title : ", yt.title)
print("View : ", yt.views)

video = yt.streams.filter(progressive=True , file_extension='mp4')
liste = list(enumerate(video))
for i in liste:
    tryi = str(i[1])[40:50:]
    print(str(i[0]) + " " + tryi)

print("Select the Resolution :")
Reso = int(input('Enter the number of Resolution : '))
size = str(video[Reso].filesize/(1024*1024))
print("\nFilesize : "+ size + "MB")

yt.register_on_progress_callback(progress)

video[Reso].download('D:\yttrial')

video[Reso].on_complete(compet())

