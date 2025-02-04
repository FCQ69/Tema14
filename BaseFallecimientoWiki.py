import requests
from bs4 import BeautifulSoup
import re
import json

# URL de la página de Wikipedia
url = "https://es.wikipedia.org/wiki/Wikipedia:Portada"

# Hacer la petición HTTP
response = requests.get(url)

# Crear el objeto BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Buscar la sección de fallecimientos
fallecimientos_section = soup.find('dt', text="Fallecimientos")

# Lista para almacenar los datos procesados
fallecimientos_data = []

if fallecimientos_section:
   
    listas_fallecimientos = fallecimientos_section.find_all_next('ul')

 
    contador = 0
    limite = 20  

    for lista in listas_fallecimientos:
        for li in lista.find_all('li'):
            if contador >= limite:
                break  

            texto = li.get_text()
            partes = texto.split(": ", 1)  

            if len(partes) == 2:
                fecha = partes[0].strip()
                nombre_y_cargo = partes[1].strip()

                # Extraer el nombre 
                enlace = li.find('a')
                nombre = enlace.get_text() if enlace else "Nombre no encontrado"

                # Cargo 
                cargo = nombre_y_cargo.replace(nombre, "").strip()

                # Extraer la edad
                edad_match = re.search(r"\((\d+)(?:-(\d+))?\)", cargo)
                if edad_match:
                    if edad_match.group(2):  # rango de edad
                        edad = edad_match.group(2) 
                    else:
                        edad = edad_match.group(1)  #edad dis
                else:
                    edad = "Desconocida"

                cargo = re.sub(r"\(\d+(?:-\d+)?\)", "", cargo).strip()

                # JSON
                fallecimientos_data.append({
                    "fecha": fecha,
                    "nombre": nombre,
                    "cargo": cargo,
                    "edad": edad
                })

                contador += 1  

        if contador >= limite:
            break  
else:
    print("No se encontró la sección de fallecimientos.")

# Guardamos en el JSON
nombre_archivo = "fallecimientos.json"
with open(nombre_archivo, "w", encoding="utf-8") as file:
    json.dump(fallecimientos_data, file, ensure_ascii=False, indent=4)

print(f"✅ Datos guardados en {nombre_archivo}")
