#install module/package
#pip install moviepy

#import all module/package
from moviepy.editor import *

#loading Video
clip = VideoFileClip('YouTube Channel Introduction Video.mp4')

#getting only 5 first seconds from video
clip = clip.subclip(0,5)

#saving video clip as gif
clip.write_gif('GifCreater.gif')
