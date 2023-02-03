from moviepy.editor import *

clip = (VideoFileClip("/home/disk/qizhongpei/projects/result.mp4"))  # 需要转为GIF的视频文件路径
clip.write_gif("movie.gif",fps=15)
