#import os
from pytube import YouTube
from pytube.exceptions import VideoUnavailable
import moviepy.editor as mpe
from scripts.files_config import prepare_directories, deletar_videos
from scripts.data_extracting import data_extracting

def video_extracting(url, path):
    yt_video = YouTube(str(url))
    title = yt_video.title
    song_audio = yt_video.streams.get_highest_resolution() 

    print(f"video title: {title}")
    print(f"streams de audio mp4: {song_audio}")
    
    #fazendo o download da stream escolhida
    song_audio.download(path) 
    print("the song was downloaded successfully!") 
    return title  
   
def coverting_to_audio_files(name, input_path, output_path):
    video = mpe.VideoFileClip(f"{input_path}{name}.mp4")#, fps_source=30)
    video.audio.write_audiofile(f"{output_path}{name}.mp3")
            

"""
streams information:
- itag: identificador de tag, referente a qualidade e tipo de stream
- mime_type: tipo de midia
- abr: taxa de bits média aproximada => quanto maior, melhor a qualidade da stream
- acodec: codificador de audio usado
- progressive: progressive é quando inclui audio e video na mesma stream (bool)
"""