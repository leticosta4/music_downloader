import os
from pytube import YouTube
from pytube.exceptions import VideoUnavailable
from scripts.data_extracting import data_extracting

#Criando um objeto do youtube com link e acessando o seu audio
series = data_extracting()
for song_url in series:
    yt_video = YouTube(str(song_url))
    title = yt_video.title
    song_audio = yt_video.streams.get_audio_only('mp4') #acessando stream específica de audio 

    print(f"video title: {title}")
    print(f"streams de audio mp4: {song_audio}")
 
    #fazendo o download da stream escolhida
    song_audio.download('data/downloaded/') #tentar mexer aqui só depois pq ta ficando como umapasta nova
    print("the song was downloaded successfully!")   
   

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

Numb,Men I Trust
Sweet,Lana Del Rey
Bohemian Rhapsody,Queen
"""

   
            
