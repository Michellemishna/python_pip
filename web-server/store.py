import requests

def get_categories():
    #usando request podemos acceder a la informacion de la api
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    print(type(r.text))
    
    #usando .json podemos transformar el str en un formato que podamos iterar
    categories = r.json()
    #haciendo la iteracion le pedimos imprimir el atributo name
    for category in categories:
        print(category['name'])