"""
* Crea un programa que se encargue de calcular el aspect ratio de una
* imagen a partir de una url.
* - Url de ejemplo: https://raw.githubusercontent.com/mouredev/
*   mouredev/master/mouredev_github_profile.png
* - Por ratio hacemos referencia por ejemplo a los "16:9" de una
*   imagen de 1920*1080px.
"""

import requests
import cv2
import numpy as np
from fractions import Fraction

# Usar requests
#respuesta = requests.get("https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png")
respuesta = requests.get("https://www.hiberus.com/crecemos-contigo/wp-content/uploads/2021/03/4-3-300x224.jpg")
contenido_imagen = respuesta.content

# Abrir la imagen
imagen = cv2.imdecode(np.frombuffer(contenido_imagen, np.uint8), cv2.IMREAD_COLOR)

ancho, alto, canales = imagen.shape
ratio = str(Fraction(ancho, alto))
ratio = ratio.replace("/", ":")
print(ratio)
