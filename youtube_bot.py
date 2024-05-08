#import os
from pytube import YouTube
from pytube.exceptions import VideoUnavailable
import moviepy.editor as mpe
from scripts.data_extracting import data_extracting

video_output_path = 'data/videos/'
audio_output_path = 'data/audios/'

#Criando um objeto do youtube com link e acessando o seu audio
def video_extracting(url, path):
    yt_video = YouTube(str(url))
    title = yt_video.title
    song_audio = yt_video.streams.get_highest_resolution() #acessando stream específica de audio 

    print(f"video title: {title}")
    print(f"streams de audio mp4: {song_audio}")
    
    #fazendo o download da stream escolhida
    song_audio.download(path) 
    print("the song was downloaded successfully!") 
    return title  
   
def coverting_to_audio_files(name, input_path, output_path):
    video = mpe.VideoFileClip(f"{input_path}{name}.mp4")#, fps_source=30)
    video.audio.write_audiofile(f"{output_path}{name}.mp3")
            


series = data_extracting()
for song_url in series:
     audio_title = video_extracting(song_url, video_output_path)
     coverting_to_audio_files(audio_title, video_output_path, audio_output_path)


"""
streams information:
- itag: identificador de tag, referente a qualidade e tipo de stream
- mime_type: tipo de midia
- abr: taxa de bits média aproximada => quanto maior, melhor a qualidade da stream
- acodec: codificador de audio usado
- progressive: progressive é quando inclui audio e video na mesma stream (bool)
"""
    
"""
Exemplos de outras musicas para adicionar no csv:
Shut up my moms calling, Hotel Ugly
Numb,Men I Trust
Sweet,Lana Del Rey
"""

   
            
