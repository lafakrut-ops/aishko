import requests

class CurrencyConverter:
    def __init__(self):
        url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&json"
        response = requests.get(url)
        data = response.json()
        self.rate = data[0]["rate"]

    def convert(self, amount):
        return amount / self.rate


converter = CurrencyConverter()

print("Курс долара:", converter.rate)

money = float(input("Введіть суму в гривнях: "))

result = converter.convert(money)

print("У доларах:", round(result, 2), "USD")
