#importo el modulo y le pedimos que me de la funcion get_population
import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda x: x['Continent'] == 'South America', data))
  
  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'],data))
  charts.generate_pie_chart(countries, percentages)
  
  country = input('Type Country => ')
  country = country.capitalize()
  result = utils.population_by_country(data, country)
  
  if result:
    labels, values = utils.get_population(result)
    charts.generate_bar_chart(country,labels, values)
  else: 
    print('Country not found')
    
#esto significa que si el archivo main es ejecutado desde la terminal, entonces ejecute 
#run() y si esta siendo llamado por otro archivo, entonces no se ejecute
if __name__ == '__main__':
  run()