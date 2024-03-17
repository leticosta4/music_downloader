import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

pd.set_option('display.max_colwidth', None) #configurando pandas para exibir conteúdo completo das células

#preparando o driver
def driver_setup():
    options = webdriver.FirefoxOptions()
    options.add_argument("-headless") #dispensando interface grafica
    d = webdriver.Edge(service=FirefoxService(GeckoDriverManager().install()),options=options) 
    d.implicitly_wait(5) #tempo de espera antes dos elementos aparecerem
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
    print(links)

#fazendo a busca do link do primeiro video no youtube
def video_searching(song, singer):
    driver = driver_setup()

    query = f"{song}+{singer}"
    search_url = f"https://www.youtube.com/results?search_query={query}"

    driver.get(search_url) 
    print(driver.current_url) #só garantinfo

    #achar o primeiro video da pagina
    thumbnails = driver.find_element(By.ID, "thumbnail")
    print("passou\n", thumbnails) 

    ytd_thumbnail = thumbnails.find_element(By.CLASS_NAME, "ytd-thumbnail") #modificar -> crashing with code 9
    print("\nsegundo elemento:\n", ytd_thumbnail)
   
    # ytd_thumbnail = driver.find_element(By.CSS_SELECTOR, 'ytd-thumbnail.style-scope ytd-video-renderer')
    # print(f"finding the element: {ytd_thumbnail}\n")
    
    href_code = ytd_thumbnail.get_attribute("href")
    print(f"pedaço: {href_code}\n")
    watch_url = f"https://www.youtube.com{href_code}"
    print(f"LINK FINAL: {watch_url}\n")

    return driver.current_url