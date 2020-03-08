import pymysql

conn = pymysql.connect(host='maria',
                        user='root',
                        password='qwer1234',
                        db='test',
                        charset='utf8')

c=conn.cursor()
symbol=input('심볼을 입력하세요')
sql="select * from stocks where symbol=%s"
# sql="select * from stocks where symbol='%s'"%symbol 이거도 적용안됨
# sql="select * from stocks where symbol=?"  <- 여기서는 적용안됨
c.execute(sql,symbol)
print(c.fetchall())
conn.close()

