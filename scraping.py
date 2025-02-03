import requests
from bs4 import BeautifulSoup

#hacemos una peticion a una pag web

url = "https://es.wikipedia.org/wiki/Wikipedia:Portada"
response = requests.get(url)

#Creamos el objeto

soup = BeautifulSoup(response.text,"html.parser")
#extraemos el titulo de la pagina

seccionActualidad = soup.find('div',{'id':'main-cur'})

if seccionActualidad:
   
    listado = seccionActualidad.find('ul')
    
    li_elements = listado.find_all('li')
 
    for li in li_elements:
        a_tag = li.find('a')
        if a_tag:
            print(a_tag.text)  
else:
    print("No se encontró el div con id 'main-cur'.")