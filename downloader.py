from pytube import YouTube
from tqdm import tqdm

import time
import sys

def compet():

    print("\nDownloading Complete")

# def progress(stream, chunk, bytes_remaining):
   
#     bytes_downloaded = stream.filesize - bytes_remaining
def progress_function(chunk, file_handle, bytes_remaining):    
    filesizee = video[Reso].filesize
    current = ((filesizee - bytes_remaining)/filesizee)
    percent = ('{0:.1f}').format(current*100)
    progress = int(50*current)
    status = '█' * progress + '-' * (50 - progress)
    sys.stdout.write(' ↳ |{bar}| {percent}%\r'.format(bar=status, percent=percent))
    sys.stdout.flush()


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

# for bytes_downloaded in tqdm(range(video[Reso].filesize)):
#     yt.register_on_progress_callback(progress)
yt.register_on_progress_callback(progress_function)


video[Reso].download('D:\Coding\Programming Video\DSA')

video[Reso].on_complete(compet())

