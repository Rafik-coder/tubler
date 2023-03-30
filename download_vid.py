from pytube import YouTube

from humanize import naturalsize

# import pafy

# Create a Pafy object for the YouTube video URL
# url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

def get_video(url):
    video_url = str(url)

    yt = YouTube(video_url)

    all_audio_stream = yt.streams.filter(only_audio=True)

    video_streams = yt.streams.all()

    streams = []
    for stream in video_streams:
        streams.append(stream)

    audio_streams = []
    for stream in all_audio_stream:
        audio_streams.append(stream)

    video_data = [{
            "stream": stream.resolution,
            "size": naturalsize(stream.filesize),
            "tag": stream.itag
        }
        for stream in streams
    ]

    audio_data = [
        {
            "stream": stream.resolution,
            "size": naturalsize(stream.filesize),
            "tag": stream.itag
        }
        for stream in audio_streams
    ]


    # size = naturalsize(video.filesize)

    cur_video = {
        "video_title": yt.title,
        "vid_image": yt.thumbnail_url,
        "vid_url": yt.channel_url,
        "video_data": video_data,
        "audio_data": audio_data
    }

    return cur_video


def download(url, tag):
    
    # URL of the video to be downloaded
    video_url = str(url)

    # tag = str(tag)

    # Create a YouTube object
    yt = YouTube(video_url)

    # Get the highest resolution video
    video = yt.streams.get_by_itag(tag)
    # yt.channel_url

    # Download the video
    downloaded = video.download(output_path="/home/xcoder/Downloads")

    return downloaded


