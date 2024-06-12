import csv

def read_csv(path):
#aqui leemos el archivo csv 
  with open(path, 'r') as csvfile:
#le indicamos que el archivo csv es delimitado por comas
    reader = csv.reader(csvfile, delimiter=',')
#le indicamos como leer los encabezados
    header = next(reader)
#creamos una lista vacia para guardar los datos
    data = []
#le indicamos que lea las filas una a una
    for row in reader:
#creamos tuplas con los encabezados y los datos de cada fila
      iterable = zip(header, row)
#lo convertimos en un diccionario con el encabezado y el valor de cada fila
      country_dict = {key: value for key, value in iterable}
#guardamos cada diccionario en la lista
      data.append(country_dict)
    return data

#aqui leemos el archivo csv
if __name__ == '__main__':
  data = read_csv('./app/data.csv')
#imprimimos los datos, en este caso solo el primero
  print(data[0])