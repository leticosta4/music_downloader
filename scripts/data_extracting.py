import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
#adaptar aqui p o navegador que for ser usado talvez dps
from webdriver_manager.firefox import GeckoDriverManager #firefox


#preparando o driver
def driver_setup():
    options = webdriver.FirefoxOptions()
    # options = Options()
    options.add_argument("-headless") #dispensando interface grafica
    d = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),options=options) 
    d.implicitly_wait(3) #tempo de espera antes dos elementos aparecerem
    return d

#tratando a query da musica parao url
def removing_whitespaces(str):
    str = str.replace(" ", "")
    return str

#extraindo a query do arquivo csv para url
def data_extracting():
    url_list = []
    music_data = pd.read_csv('data/input/songs.csv')
    music_data["Song"] = music_data["Song"].apply(removing_whitespaces)
    music_data["Singer"] = music_data["Singer"].apply(removing_whitespaces)

    for song, singer in zip(music_data["Song"], music_data["Singer"]):
        url_list.append(video_searching(song, singer))
    
    links = pd.Series(url_list)
    return links

#fazendo a busca do link do primeiro video no youtube
def video_searching(song, singer):
    driver = driver_setup()

    query = f"{song}+{singer}"
    search_url = f"https://www.youtube.com/results?search_query={query}"

    driver.get(search_url) 

    #achar o primeiro video da pagina
    ytd_thumbnail = driver.find_element(By.CSS_SELECTOR, "#contents ytd-video-renderer a[href]")
    watch_url = ytd_thumbnail.get_attribute("href")

    #conferindo dados
    print(f"link atual do driver: {driver.current_url}") 
    print(f"link final para o video pelo acesso ao elemento html: {watch_url}")
    return watch_url