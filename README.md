# Mega_Exchange Class
A Python class for web scraping data from a website and storing it in a JSON file. The class uses the requests, BeautifulSoup, and fake_headers libraries to send GET requests, parse HTML, and generate user agent headers, respectively. The class also includes a method for comparing the current data with the previous data and highlighting any changes.

## Attributes
URL (str): The URL of the website to be scraped.
name (str): The name of the website.
get_elements (function): A function that returns the scraped data in dictionary format.
## Methods
get(): Sends a GET request to the website and returns a BeautifulSoup object.
write_json(): Writes the scraped data to a JSON file.
data_update(): Compares the current scraped data with the previous data and writes any changes to the JSON file.
Example Usage


import json
import datetime
from Mega_Exchange import Mega_Exchange

def get_elements():
    # define the elements to be scraped
    data = {
        'element1': {
            'purchase': 10,
            'selling': 20
        },
        'element2': {
            'purchase': 30,
            'selling': 40
        }
    }
    return data

url = 'https://example.com'
name = 'example'
exchange = Mega_Exchange(url, name, get_elements)

# scrape data and write to JSON file
exchange.write_json()

# compare current data with previous data and highlight any changes
exchange.data_update()




# Класс Mega_Exchange
Класс на языке Python для парсинга данных с веб-сайта и сохранения их в файле JSON. Класс использует библиотеки requests, BeautifulSoup и fake_headers для отправки GET-запросов, парсинга HTML и генерации заголовков пользовательского агента, соответственно. Класс также включает метод для сравнения текущих данных с предыдущими данными и выделения любых изменений.

## Атрибуты
URL (str): URL-адрес веб-сайта, который будет анализироваться.
name (str): Название веб-сайта.
get_elements (функция): Функция, которая возвращает данные в словарном формате.
## Методы
get(): Отправляет GET-запрос на веб-сайт и возвращает объект BeautifulSoup.
write_json(): Записывает собранные данные в файл JSON.
data_update(): Сравнивает текущие собранные данные с предыдущими данными и записывает любые изменения в файл JSON.
## Пример использования

import json
import datetime
from Mega_Exchange import Mega_Exchange

def get_elements():
    # определение элементов для парсинга
    data = {
        'element1': {
            'purchase': 10,
            'selling': 20
        },
        'element2': {
            'purchase': 30,
            'selling': 40
        }
    }
    return data

url = 'https://example.com'
name = 'example'
exchange = Mega_Exchange(url, name, get_elements)

# очистите данные и запишите в файл JSON
exchange.write_json()

# сравните текущие данные с предыдущими и выделите любые изменения
exchange.data_update()