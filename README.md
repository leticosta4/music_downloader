# music_downloader
Um bot que faz o download de músicas (formato mp4) pelo youtube a partir de um arquivo csv

### bibliotecas e módulos utilizados
- [pytube](https://pytube.io/en/latest/)
- [moviepy](https://zulko.github.io/moviepy/)
- [pandas](https://pandas.pydata.org/docs/)
- [selenium-webdriver]( https://www.selenium.dev/documentation/webdriver/)
- [webdriver-manager](https://pypi.org/project/webdriver-manager/)


### criação de um ambiente virtual
 - Dentro da pasta do projeto, rodar no terminal:
    - python3 -m venv "nome do ambiente virtual"

 - Para ativar o ambiente virtual:
   - Linux:      source "nome do ambiente virtual"/bin/activate
   - Windows:    "nome do ambiente virtual"\Scripts\activate.bat


### instalando as bibliotecas
Dentro da pasta do projeto, rodar no terminal:
    - pip install -r requirements.txt

### ALERTA 
Já com o ambiente virtual ativado, ao se instalar o pytube, na versão 15.0.0, a linha 30 do seu arquivo 'cipher.py' (pasta lib) precisa ser alterada
para tal:

      var_regex = re.compile(r"^[\w\$_]+\W")

Essa alteração evitará um erro de identificação do caracter alfanumérico "\w+". E na função do arquivo havia um `'\$O'`, que não seria correspondido.
De acordo com a especificação da [ECMA](https://262.ecma-international.org/5.1/#sec-7.6), identificadores válidos podem incluir os símbolos `'$'` e `'_'`, além de caracteres alfanuméricos.