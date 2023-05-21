from pytube import YouTube

video_url = "link"

try:
    yt = YouTube(video_url)
    video = yt.streams.get_highest_resolution()
    print("Downloading")
    video.download()
    print("Video downloaded successfully!")
except Exception as e:
    print("Error:", str(e))