import requests 

# headers = {
#     'Authorization': 'Token %s'%self.Token,
#     'content-type': 'application/json',
# }

# data = '{"execution":"limit","srcCurrency":"btc","dstCurrency":"rls","hours":2.4}'

# response = requests.post('https://api.nobitex.ir/market/orders/cancel-old', headers=headers, data=data)
# resJson = response.json()
        

headers ={
    'Content-Type': 'application/json',
    'Captcha':'305411'
}

data= '{"username":"mahdiebi.exe@gmail.com","password":"$11235694990010@MahdiEbi#1384"}'

res = requests.post('https://api.nobitex.ir/auth/login/', headers= headers, data=data)
print(res)
print(res.text)