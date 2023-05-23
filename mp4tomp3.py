import moviepy
import moviepy.editor

# file path
video = moviepy.editor.VideoFileClip('2023-05-03_16-26-56.mp4')
# video to audio
audio = video.audio
audio.write_audiofile(video.filename + '.mp3')
