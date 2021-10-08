import requests
import sqlite3
from datetime import date
today = date.today()
r = requests.get('https://api.livecoin.net/exchange/ticker?currencyPair=BTC/USD')
res = r.json()
result = res['last']
print(result)
conn = sqlite3.connect('./bitcoin.db')
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