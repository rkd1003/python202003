#csv->db
import sqlite3,csv

input_file='sqlitetest/input.csv'
conn=sqlite3.connect('sqlitetest/sup.db')
cur=conn.cursor()
sql='''
    create table if not exists sup
    (
        sup_name varchar(20),
        invoice_number varchar(20),
        part_number varchar(20),
        cost float,
        date date    
    )'''

cur.execute(sql)
conn.commit()
conn.close()