#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re

username = 'natas23'
password = 'qjA8cOoKFTzJhtV0Fzvt92fgvxVnVRBj'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()

# response = session.get(url, auth=(username, password))
response = session.post(url, data = { "passwd" : "11iloveyou" },auth=(username, password))

content = response.text
print(content)