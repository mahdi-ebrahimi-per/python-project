import requests,sqlite3, re
from datetime import date
# from bs4 import BeautifulSoup

print(globals()['__name__'])

Token = 0
Type = "buy"
execution = "market"
src = "btc"
dst = "rls"
amount = "0.02"
price = "87"

#currency:btc / price:22$/ amount:5/ srt -> dst  from btc to xrp

headers = {
    'Authorization': 'Token %s'%Token,
    'content-type': 'application/json',
}

data = '{"type":"%s", "execution":"%s" ,"srcCurrency":"%s","dstCurrency":"%s","amount":"%s","price":%s}' %(Type,execution,src,dst,amount,price)
#execution : دلیل ارور ممکن است به دلیل نداشتن
response = requests.post('https://api.nobitex.ir/market/orders/add')
resJson = response.json() #در دیتا بیس باید ذخیره شود
