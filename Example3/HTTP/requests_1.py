import requests

rsp = requests.get('https://naver.com')

print(rsp.status_code)
print(rsp.encoding)

url = 'https://search.naver.com/search.naver'
payload = {'query': 'iot'}
rsp = requests.get(url, params=payload)
print(rsp.url)
print(rsp.headers)
print(rsp.text)