import requests
from bs4 import BeautifulSoup

pagina_tienda = "https://www.gollo.com"
try:
    html = requests.get(pagina_tienda)

    if html.status_code != 200:
        print("Este sitio permite que la araña vea pero no la deja entrar :'( ")
    else:    
        soup = BeautifulSoup(html.text, "html.parser")

        nombre_tienda = soup.title
        enlaces = soup.find_all("a")
        imagenes = soup.find_all("img")

        if len(enlaces) == 0 or len(imagenes) == 0:
            print("Ver pero no tocar :'C")
        else:
            #Cambiar esto por guardar a disco
            for enlace in enlaces:
                print(enlace.text)

        print("------------------------------------------------------\n\n")
        print(f"Hay un total de {len(enlaces)} enlaces en la página de {nombre_tienda.text}!!)")
        print(f"Y usan un total de {len(imagenes)} imagenes en su sitio...!!\n\n")
except:
    print("A este sitio no le gustan las arañas")
    print("No se recibió respuesta por parte del sitio")
finally:
    print("Operación terminada")
