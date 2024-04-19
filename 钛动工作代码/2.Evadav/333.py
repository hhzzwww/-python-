import requests

login_url = 'https://evadav.com/login'

headers = {

    "Origin": "https://evadav.com",

    "Referer": "https://evadav.com/",

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
response = requests.get(url=login_url, headers=headers)
print(response.text)





