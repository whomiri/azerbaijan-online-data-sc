import requests
from bs4 import BeautifulSoup

def get_exchange_rates():
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    response = requests.get(url)
    data = response.json()

    rates = {
        'USD': data['rates']['AZN'],
        'TRY': data['rates']['TRY'] / data['rates']['AZN'],
        'EUR': data['rates']['EUR'] / data['rates']['AZN'],
        'RUB': data['rates']['RUB'] / data['rates']['AZN'],
        'GBP': data['rates']['GBP'] / data['rates']['AZN'],
        'JPY': data['rates']['JPY'] / data['rates']['AZN'],
        'CNY': data['rates']['CNY'] / data['rates']['AZN'],
        'INR': data['rates']['INR'] / data['rates']['AZN'],
        'AUD': data['rates']['AUD'] / data['rates']['AZN'],
        'CAD': data['rates']['CAD'] / data['rates']['AZN'],
        'CHF': data['rates']['CHF'] / data['rates']['AZN'],
        'SEK': data['rates']['SEK'] / data['rates']['AZN'],
        'NZD': data['rates']['NZD'] / data['rates']['AZN'],
    }

    return rates

def get_oil_price():
    url = 'https://tradingeconomics.com/commodities/crude-oil'  # Oil price source
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the HTML element containing the oil price
    price_element = soup.find('span', class_='text-2xl')  # This class name may vary depending on the element on the web page
    if price_element:
        oil_price = float(price_element.text.replace('$', '').replace(',', '').strip())
    else:
        raise ValueError("Neft qiyməti tapılmadı!")

    return oil_price

if __name__ == '__main__':
    try:
        exchange_rates = get_exchange_rates()
        oil_price = get_oil_price()

        # Print the results
        for currency, rate in exchange_rates.items():
            print(f"1 {currency} = {rate:.2f} AZN")
        print(f"Azərbaycan Neftinin anlıq qiyməti: {oil_price:.2f} USD")
    except ValueError as e:
        # Printing exchange rates when oil price cannot be found
        exchange_rates = get_exchange_rates()  # Get exchange rates again
        for currency, rate in exchange_rates.items():
            print(f"1 {currency} = {rate:.2f} AZN")
        print("Neft qiyməti tapılmadı!")
    except Exception as e:
        print(f"Hata: {e}")
