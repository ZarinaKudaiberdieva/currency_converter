import requests
import json
class Currency_convertor:
    
    rates = {} 
    def __init__(self, url):
       data = requests.get(url).json()
       self.rates = data["rates"] 
    
    
    
    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != 'EUR' :
            amount = amount / self.rates[from_currency]
        amount = round(amount * self.rates[to_currency], 2)
        print('{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency))
  

from_country = input("From Country: ")
to_country = input("TO Country: ")
amount = int(input("Amount: "))
url = 'https://api.ratesapi.io/api/latest HTTP/2'
converter = Currency_convertor(url)
 
print(converter.convert(from_country, to_country, amount))