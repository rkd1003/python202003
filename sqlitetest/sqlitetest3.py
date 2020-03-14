import sqlite3

conn = sqlite3.connect('sqlitetest/example.db')
c = conn.cursor()

c.execute('select * from stocks')
print(c.fetchall()) #.fetch~ 불러오다

symbol = input('심볼을 입력하세요 : ')
sql="select * from stocks where symbol='%s'"%symbol
sql="select * from stocks where symbol=?"
# ?은 sqlite에서 제공하는함수라
# 다른데도 공통으로 쓰게하려면 위에 %s %symbol로 써야함

c.execute(sql,[symbol])
# c.execute(sql,(symbol,))
# 두번째값은 튜플로 만들어 싸줘야함
# symbol을 소괄호로 묶어 !튜플! 로 만들어줘야함
# 튜플은 끝에 , 넣어야함

print(c.fetchall())
conn.close()