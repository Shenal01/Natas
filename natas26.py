#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re
import urllib
from urllib.parse import unquote
import base64

username = 'natas26'
password = '8A506rfIAXbKKk68yJeuTuRq4UfcK70k'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()

response = session.get(url, auth=(username, password))
content = response.text
print(content)
print(session.cookies)

response = session.get(url + '?x1=0&y1=0&x2=500&y2=500', auth=(username, password))
content = response.text
print(content)
print(base64.b64decode(unquote(session.cookies['drawing'])))
# print(urllib.unqoute(session.cookies['drawing']))
