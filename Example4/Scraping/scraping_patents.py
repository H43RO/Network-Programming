from urllib import request
import re

url = 'https://bulkdata.uspto.gov/data/patent/officialgazette/2019/'
rsp = request.urlopen(url)
html = rsp.read().decode()

file_list = re.findall(r'(e-)(.+)(zip")', html)
file_url = ''

for name in file_list:
    file_url = (url + ''.join(name))[:-1]
    print(file_url)

request.urlretrieve(file_url, 'test.zip')
