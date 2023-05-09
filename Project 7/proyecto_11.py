import bs4
import requests

# identificar condiciones de extraccion (en este caso la cantidad de estrellas)

'''url_base = 'http://books.toscrape.com/catalogue/page-{}.html'

resultado = requests.get(url_base.format('1'))
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

print(sopa.select('.product_pod'))'''

# Extraer titulo del libro

'''url_base = 'http://books.toscrape.com/catalogue/page-{}.html'

resultado = requests.get(url_base.format('1'))
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

libros = sopa.select('.product_pod')

ejemplo = libros[0].select('a')[1]['title']

print(ejemplo)'''

# Combinar items (crear url sin numero de pagina)

url_base = 'http://books.toscrape.com/catalogue/page-{}.html'

# Lista de titulos con 4 o 5 estrellas

titulos_rating_alto = []

# Iterar paginas

for pagina in range(1, 51):

    # crear sopa en cada pagina
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    # seleccionar datos de los libros
    libros = sopa.select('.product_pod')

    # iterar libros
    for libro in libros:

        # chequear q tengan 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:

            # guardar tituo en variable
            titulo_libro = libro.select('a')[1]['title']

            # agregar libro a la lista
            titulos_rating_alto.append(titulo_libro)

# ver libros de 4 o 5 estrellas en consola
for t in titulos_rating_alto:
    print(t)
