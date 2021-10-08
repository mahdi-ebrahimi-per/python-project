import requests, datetime, json

nowDate = str(datetime.date.today())

url = 'https://api.coindesk.com/v1/bpi/historical/close.json?start=2013-09-01&end=%s' %nowDate

response = requests.get(url)
res = response.json()

x= list(res['bpi'].items())

def dateFromPrice(price):
        for i in range(len(x)):
            if float(price) == x[i][1]:
                print(x[i][0])

# dateFromPrice('1124.7631')


def sameLine(num1, num2): #if num1 be in num2 zone return True
    num2_Zone = num2 * (0.43/100)
    num2_min = num2 - num2_Zone
    num2_max = num2 + num2_Zone
    if num1 < num2_max and num1 > num2_min:
        return True
    else:
        return False


print(sameLine(37689,37588))

data = []



# 37689     37718     