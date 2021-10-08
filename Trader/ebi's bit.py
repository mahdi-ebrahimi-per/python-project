import requests





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

database = "C:\\Users\\asus\\Desktop\\bitcoin.db"

# create a database connection
conn = create_connection(database)
sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                name text NOT NULL,
                                price integer,
                                date text NOT NULL
                            );"""
create_table(conn, sql_create_tasks_table)
    # create a new project
print('connecting...')
pre_data=requests.get('https://api.coindesk.com/v1/bpi/historical/close.json?start=2013-12-25&end=2020-12-25').json()
mid_data=pre_data['bpi']
for day in mid_data:
    price=mid_data[day]
    project = ('Bitcoin', price, day)
    project_id = create_project(conn, project)

