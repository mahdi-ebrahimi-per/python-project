import requests
from bs4 import BeautifulSoup
import sqlite3
from sqlite3 import Error



def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_project(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO tasks(name,price,date)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid


def create_task(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    sql = ''' INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid
def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

database = "C:\\Users\\asus\\Desktop\\ripple.db"

# create a database connection
conn = create_connection(database)
sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                name text NOT NULL,
                                price integer,
                                date text NOT NULL
                            );"""
create_table(conn, sql_create_tasks_table)
    # create a new project


website_text=requests.get('https://finance.yahoo.com/quote/XRP-USD/history/?guccounter=1').text
soup=BeautifulSoup(website_text,'html.parser')
tabel=soup.find('table',{'class':'W(100%) M(0)'})
trs=tabel.find_all('tr')
trs=tabel.find_all('tr',{'class':'BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)'})
lis=[]
print(len(trs))
for tr in trs:
    tds=tr.find_all('td')
    a=0
    dic={}
    for td in tds:
        a+=1
        if a==1:
            dic['date']=td.text
        if a==5:
            dic['close']=td.text
    project = ('Ripple', dic['close'], dic['date'])
    project_id = create_project(conn, project)
print(lis)
