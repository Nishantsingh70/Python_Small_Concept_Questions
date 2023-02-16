#install module/package
#pip install pytube
#pip install pytube3

#import module/package
from pytube import YouTube

url = 'https://www.youtube.com/watch?v=05uF8t73f5s'
my_video = YouTube(url)

print("******************** Video Title ******************************")
print(my_video.title)

print("******************** Thumbnail Image ***************************")
print(my_video.thumbnail_url)

print("******************** Download Video ****************************")
#set stream resolution

my_video = my_video.streams.get_highest_resolution()

#or my_video = my_video.streams.first() => to print first resolution which is bydefault the highest resolution.
#for stream in my_video.streams:
#  print(stream)
my_video.download()