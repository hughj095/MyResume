# This script downloads a YouTube video file and saves the audio to an mp3

from pytube import YouTube
from pydub import AudioSegment

input_video_url = 'https://www.youtube.com/watch?v=SPoIoUgBJdI'
output_audio_filename = 'market_bell.mp3'

def download_youtube_audio(video_url, output_path=output_audio_filename):
    # Download the video
    yt = YouTube(video_url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    downloaded_file = audio_stream.download(filename='audio.mp4')
    
    # Convert to MP3
    audio = AudioSegment.from_file(downloaded_file)
    audio.export(output_path, format="mp3")
    print(f"Audio saved as {output_path}")

# Example usage
download_youtube_audio(input_video_url)

'''
import yt_dlp

def download_youtube_audio(video_url, output_path='output.mp3'):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': output_path,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

# Example usage
download_youtube_audio('https://www.youtube.com/watch?v=YOUR_VIDEO_ID')
'''

