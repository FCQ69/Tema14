import requests
from bs4 import BeautifulSoup

#hacemos una peticion a una pag web

url = "https://es.wikipedia.org/wiki/Wikipedia:Portada"
response = requests.get(url)

#Creamos el objeto

soup = BeautifulSoup(response.text,"html.parser")
#extraemos el titulo de la pagina

titulo = soup.title.text
print(f"El titulo es {titulo}")
