import os

def prepare_directories():
    diretorios_A_criar = ['data/output/', 'data/output/videos', 'data/output/audios']
    for path in diretorios_A_criar:
        try:
            os.makedirs(path)
            print(f"O diretório {path} foi criado com sucesso.")
        except FileExistsError:
            print(f"O diretório {path} já existe!")
        except Exception as err:
            print(f"Erro ao criar o diretório {path}: {err}")

def deletar_videos(diretorio):
    if not os.path.exists(diretorio):
        print(f"O diretório {diretorio} não existe.")
        return

    for video in os.listdir(diretorio):
        if video.endswith(".mp4"):
            video_path = os.path.join(diretorio, video) #cria o caminho completo do arquivo
            os.remove(video_path)
            print(f"O vídeo {video} removido com sucesso.")