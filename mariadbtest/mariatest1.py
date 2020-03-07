import pymysql

conn=pymysql.connect(host='localhost',
                        user='root'
                        password='qwer1234'
                        db='test'
                        cursorclass=pymysql.cursors.DictCursor)

c=conn.cursor()