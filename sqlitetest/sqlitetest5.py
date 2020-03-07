#csv->db
import sqlite3,csv

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
sql='delete from sup'
cur.execute(sql)
input_file='sqlitetest/input.csv'
open_file=open(input_file,'r')
file_reader = csv.reader(open_file,delimiter=',')
print(next(file_reader))
data=[]
for row in file_reader:
    data.append(row)
sql='insert into sup values(?,?,?,?,?)'
cur.executemany(sql,data)
conn.commit()
conn.close()