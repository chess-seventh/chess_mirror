"""

File with all the API classes needed and imports.

All classes will return the rwa data

"""
from config import ApiURL

import datetime
import json
import urllib.request
import sys
import configparser
import argparse


class Meteo(object):
  def __init__(self):
    self.myurl = None
    self.data = None
    self.api_dict = dict()

    self.get_urls()
    self.data_fetch()
    self.data_organizer()
    self.display()

  def get_urls(self):
    a = ApiURL('METEO')
    self.myurl = a.urlMeteo()


  def data_fetch(self):
    with urllib.request.urlopen(self.myurl) as url:
      output = url.read().decode('utf-8')
      raw_api_dict = json.loads(output)
    self.api_dict = raw_api_dict


  def data_organizer(self):
    main = self.api_dict.get('main')
    sys = self.api_dict.get('sys')
    data = dict(
      city=self.api_dict.get('name'),
      country=sys.get('country'),
      temp=main.get('temp'),
      temp_max=main.get('temp_max'),
      temp_min=main.get('temp_min'),
      humidity=main.get('humidity'),
      pressure=main.get('pressure'),
      sky=self.api_dict['weather'][0]['main'],
      wind=self.api_dict.get('wind').get('speed'),
      wind_deg=self.api_dict.get('deg'),
      cloudiness=self.api_dict.get('clouds').get('all')
    )
    self.data = data


  def display(self):
    m_symbol = '\xb0' + 'C'
    print('---------------------------------------')
    print('Current weather in: {}, {}:'.format(self.data['city'], self.data['country']))
    print('---------------------------------------')
    print('')
    print(self.data['temp'], m_symbol, self.data['sky'])
    print('Max: {}, Min: {}'.format(self.data['temp_max'], self.data['temp_min']))
    print('')
    print('Wind Speed: {}'.format(self.data['wind']))
    print('Humidity: {}'.format(self.data['humidity']))
    print('')
    print('---------------------------------------')
    print('---------------------------------------')

