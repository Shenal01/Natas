#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re
import urllib.parse
import base64

username = 'natas11'
password = '1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
cookies = { "data" : "MGw7JCQ5OC04PT8jOSpqdmk3LT9pYmouLC0nICQ8anZpbS4qLSguKmkz" }
response = session.get(url, auth=(username, password), cookies = cookies )

content = response.text
print(content)
