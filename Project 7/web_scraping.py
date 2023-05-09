import bs4
import requests

# Extraer parrafo de un sitio web ↓

'''resultado = requests.get('https://escueladirecta.com/bloq/260007/encapsulamiento')

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

parrafo_especial = sopa.select('p')

print(sopa.select('title'))'''

# Extraer elementos de una clase ↓

'''resultado = requests.get('https://escueladirecta.com/bloq/260007/encapsulamiento')

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

columna_lateral = sopa.select('.content p')
for p in columna_lateral:
    print(p.getText)'''

# Extraer Imagenes

resultado = requests.get('https://escueladirecta.com/courses')

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

imagenes = sopa.select('.course-box-image')
for i in imagenes:
    print(i)

# Si queremos descargar la imagen en la compu ↓

descargar_imagen = sopa.select('.course-box-image')[0]['src']

print(descargar_imagen)
# nos da el url:  https://process.fs.teachablecdn.com/ADNupMnWyR7kCWRvm76Laz/resize=width:705/https://file-uploads.teachablecdn.com/136becbcea3e4d51abede23bf9794cf1/bcae2c4d38ac4953bd27a3d3be140893

imagen_1 = requests.get(descargar_imagen)

f = open('mi_imagen.jpg', 'wb') # creamos el archivo mi_imagen y lo almacenamos en la variable f
f.write(imagen_1.content) # Lo llamamos con .content (lo que hace content es traer el codigo binario
f.close() # cerramos siempre.



