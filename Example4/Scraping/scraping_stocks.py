import requests
import re

url = 'https://finance.naver.com/item/main.nhn?code=005930'
rsp = requests.get(url)
html = rsp.text

stock_results = re.findall(r'(<dl class="blind">)([\s\S]+?)(</dl>)', html)
samsung_stock =stock_results[0]
samsung_index = samsung_stock[1]

index_list = re.findall(r'(<dd>)([\s\S]+?)(</dd>)', samsung_index)

for index in index_list:
    print(index[1])