import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
import json
import time
import datetime


class Mega_Exchange:
    """
    A class to scrape data from a website using the requests, BeautifulSoup and fake_headers libraries.
    The scraped data is stored in a JSON file and compared with previous data to highlight any changes.

    Attributes:
    -----------
    URL : str
        The URL of the website to be scraped.
    name : str
        The name of the website.
    get_elements : function
        A function that returns the scraped data in dictionary format.

    Methods:
    --------
    get()
        Sends a GET request to the website and returns a BeautifulSoup object.
    write_json()
        Writes the scraped data to a JSON file.
    data_update()
        Compares the current scraped data with the previous data and writes any changes to the JSON file.
    """

    def __init__(self, URL, name, get_elements):
        self.headers = Headers(browser='Chrome', os='win').generate()
        self.name = name
        self.get_elements = get_elements
        self.url = URL
        self.data = {}

    def get(self):
        """
        Sends a GET request to the website and returns a BeautifulSoup object.
        """
        URL = self.url
        headers = self.headers
        page = requests.get(self.url, headers=headers, timeout=30)
        soup = BeautifulSoup(page.text, 'lxml')
        return soup

    def write_json(self):
        """
        Writes the scraped data to a JSON file.
        """
        with open(f'news_dict_{self.name}.json', 'w', encoding='utf8') as file:
            json.dump(self.get_elements(), file, indent=4, ensure_ascii=False)
        return f'news_dict_{self.name}.json'

    def data_update(self):
        """
        Compares the current scraped data with the previous data and writes any changes to the JSON file.
        """
        with open(f'news_dict_{self.name}.json', encoding='utf8') as file:
            old_dict = json.load(file)
        soup = self.get()
        new_dict = self.get_elements()
        time_doc = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M")
        result = {}
        for key in old_dict:
            if old_dict[key]['purchase'] != new_dict[key]['purchase'] or old_dict[key]['selling'] != new_dict[key][
                'selling']:
                result[key] = (old_dict[key], new_dict[key])
                print(f'Changes occurred at {time_doc}: \n{key}\n'
                      f'Purchase price was {old_dict[key]["purchase"]}, now {new_dict[key]["purchase"]}\n'
                      f'Selling price was {old_dict[key]["selling"]}, now {new_dict[key]["selling"]}')
                self.write_json()
            else:
                print(f'Nothing has changed for {key} as of {time_doc}')
        return result
