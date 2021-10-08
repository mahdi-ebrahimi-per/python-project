import requests,sqlite3, re
from datetime import date
from bs4 import BeautifulSoup


class Main():
    def __init__(self):
        pass


class Get():#get data from nobitex
    def __init__(self):
        pass

    def nowPrice(self):
        pass

    def Login(self): #باید تنظیم شود 20 روز یکبار کار کند
        userName = ''
        password = ''

        headers = {
            'Content-Type': 'application/json',
        }

        data = '${"username":"%s","password":"%s","remember":"yes"}' %(userName,password)
        #remember : yes ممکنه باگ داشته باشه
        response = requests.post('https://api.nobitex.ir/auth/login/', headers=headers, data=data)
        resJson = response.json()
        if 'key' in resJson:
            self.Token = resJson['key']


    def getLimitations(self):#محدودیت ها
        headers = {
            'Authorization': 'Token %s'%self.Token,
            'content-type': 'application/json',
            }

        response = requests.post('https://api.nobitex.ir/users/limitations', headers=headers)
        resJson = response.json()

    def balance(self,currency): #موجودی
        headers = {
            'Authorization': 'Token %s'% self.Token,
        }

        data = '{"currency":"%s"}'%currency

        response = requests.post('https://api.nobitex.ir/users/wallets/balance', headers=headers, data=data)
        resJson = response.json()
        if resJson['status'] == 'ok':
            self.Balance = resJson['balance']



class Analysis():#Analysis & send order
    def __init__(self):
        pass    


    def stopLoss(self):
        pass



class Order():
    def __init__(self):
        pass

    def new(self,currency,price,amount,src,dst):#معامله جدید
        #currency:btc / price:22$/ amount:5/ srt -> dst  from btc to xrp
        headers = {
            'Authorization': 'Token %s'% self.Token,
            'content-type': 'application/json',
        }

        data = '{"type":"%s","srcCurrency":"%s","dstCurrency":"%s","amount":"%s","price":%s}' %(currency,stc,dst,amount,price)
        #execution : دلیل ارور ممکن است به دلیل نداشتن
        response = requests.post('https://api.nobitex.ir/market/orders/add', hb~
        resJson = response.json() #در دیتا بیس باید ذخیره شود

    def update(self,id):#به روز رسانی معامله
        pass

    def status(self,id):#وضعیت سفارش
        headers = {
            'Authorization': 'Token %s'self.Token,
            'content-type': 'application/json',
        }

        data = '{"id":%s}'%id

        response = requests.post('https://api.nobitex.ir/market/orders/status', headers=headers, data=data)
        resJson = response.json()


    def listOrders(self,src,dst):#فهرست سفارش
        headers = {
            'Authorization': 'Token %s'%self.Token,
            'content-type': 'application/json',
        }

        data = '{"srcCurrency":"%s","dstCurrency":"%s","details":2}'%

        response = requests.post('https://api.nobitex.ir/market/orders/list', headers=headers, data=data)


    def cancel(self,execution,src,dst,hours):#لغو سفارش
        headers = {
            'Authorization': 'Token %s'%self.Token,
            'content-type': 'application/json',
        }

        data = '{"execution":"limit","srcCurrency":"btc","dstCurrency":"rls","hours":2.4}'

        response = requests.post('https://api.nobitex.ir/market/orders/cancel-old', headers=headers, data=data)
        resJson = response.json()
        


######اضافه نشده ها به دلیل ندونستن کاربرد و کارکرد
#لیست سفارشات
#لیست معاملات
#آمار بازار نوبیتکس
#آمار بازار جهانی
#افزودن کارت بانکی
#افزودن حساب بانکی
#لیست تراکنش ها
#لیست واریزها و برداشت‌ها
#تولید آدرس بلاکچین


##########سوال ها
#بهترین قیمت لحظه ای  فروش/خرید -> سفارش مارکت market
#execution limit?



##########امکانات
#بدست آوردن کارمزد و در نظر گرفتن در تحلیل
#شمردن هر معامله
#ثبت شدن هر معامله در دیتا بیس
#عوض کننده ی اتوماتیک یوزر پسm



##########نکات
#ممکنه ریسپانس جیسون نباشه بعدش به باگ میخوریم
#برنامه باید موجودی تمام دارایی ها را با زمان در دیتا بیس مشخص کند
#ممکن است باگ به خاطر '%s' کوتیشن/ %s خالی
#باید چک کند که حتما اردر انجام شده است


##########اسطلاحات
#currency نوع ارز
#
#
#