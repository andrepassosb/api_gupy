import urllib.request
from bs4 import BeautifulSoup
import json

url = "https://www.gupy.io/login/"
f = urllib.request.urlopen(url)
html = f.read()
arquivo = open("login.html", "wb")
arquivo.write(html)

html_string = html
soup = BeautifulSoup(html_string,features="html.parser")

api_gupy = {}

for tag in soup.find_all('tr'):
    empresa = (tag.td.string)
    for link in tag.find_all('a'):
        links = (link.get('href'))
        api_gupy[empresa]= {'Page':links}
        break

for k, v in api_gupy.items():
    try:
        url = api_gupy[k]['Page']
        print(url)
        f = urllib.request.urlopen(url)
        html = f.read()
        html_string = html
        soup = BeautifulSoup(html_string,features="html.parser")
        vagas = {}
        x = []
        for tag in soup.find_all('tr'):
            for h4 in tag.find_all('h4'):
                vaga = h4.span.string
            for strong in tag.find_all('strong'):
                local = strong.string
                remove = ["\n","/","\n","\n","  ","and"]
                for i in range(0,len(remove)):
                    local = local.replace(remove[i],"")
                vagas = {vaga : local}
                x.append(vagas)
                api_gupy[k]['Vaga'] = x
                x.append(vagas)
    except Exception:
        pass

with open('api_gupy.json', 'w') as f:
   json.dump(api_gupy, f)    
