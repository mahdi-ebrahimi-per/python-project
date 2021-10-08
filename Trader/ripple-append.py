from bs4 import BeautifulSoup
import requests
import re
import sqlite3
from datetime import date
r = requests.get('https://finance.yahoo.com/quote/XRP-USD/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAGoC-GNAixXa_GSTwSFWJTLtEV9zylHtJPf63nFGpT7VOAR5oa3st7MQh8bWbt97XQ3Jm48j6V2Trng__5e8XgWMrUIzDjmYN7e0ukBCqFX5giXfZPDAolWtip1Guifkt84yNEB6shridyRoaYG_JKR2j5SzXAphLZGEN_anMhWD')
soup = BeautifulSoup(r.text,'html.parser')
res =str(soup.find('span', attrs={'class':"Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"}))
result = re.search(">(.*)<", res)
result = result.group()
result =float( result[1:-1])
today = date.today()

conn = sqlite3.connect('ripple.db')
c = conn.cursor()
try:
    # Create table
    c.execute('''CREATE TABLE price(date,price)''')
except:
    pass
# Insert a row of data
c.execute("insert into price(date,price) values (?, ?)", (today,result))
# Save (commit) the changes
conn.commit()
# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()