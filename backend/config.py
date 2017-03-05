"""

Configs

"""

import datetime
import json
import urllib.request
import sys
import configparser
import argparse
from constants import *


class ApiURL(object):
  def __init__(self, type):

    self.type = type # defines what kind of api url I want to build
    self.meteo_data = ''
    self.sms_data = ''

    if self.type == 'METEO':
      self.urlMeteo()
    elif self.type == 'SMS':
      self.urlSMS()
    else:
      print('type URL not found')

  def urlMeteo(self):
    self.meteo_data = METEO_BASE_URL + METEO_CITY_IDS + '&mode=json&units=' + METEO_UNIT + '&APPID=' + METEO_USER_API
    return(self.meteo_data)

  def urlSMS(self):
    print('empty')