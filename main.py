from scripts.files_config import prepare_directories, deletar_videos
from scripts.data_extracting import data_extracting
from scripts.youtube_bot import video_extracting, coverting_to_audio_files

video_output_path = 'data/output/videos/'
audio_output_path = 'data/output/audios/'

prepare_directories()
series = data_extracting()
for song_url in series:
     audio_title = video_extracting(song_url, video_output_path)
     coverting_to_audio_files(audio_title, video_output_path, audio_output_path)

print("audio baixado com sucesso")
deletar_videos(video_output_path)

"""
Exemplos de outras musicas para adicionar no csv:
describe what she was like, 2Klercs
sweet, cigarettes after sex   
(esses de cima sao mais curtos)
Shut up my moms calling, Hotel Ugly
Numb,Men I Trust
Sweet,Lana Del Rey
"""