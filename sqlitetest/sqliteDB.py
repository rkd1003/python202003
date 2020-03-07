import sqlite3

def db_conn():
    return sqlite3.connect('sqlitetest/book.db')
    
def create_table():
    conn=db_conn()
    cur=conn.cursor()
    sql='''
        create table if not exists books(
            title text,
            pub_date text,
            pub text,
            pages integer,
            recommend integer
        )
    '''
    cur.execute(sql)
    conn.commit()
    conn.close()
    print("테이블 생성")
    
def insert_data():
    conn=db_conn()
    cur=conn.cursor()
    title=input('책제목: ')
    pub_date=input('출판일: ')
    pub=input('출판사: ')
    pages=int(input('총페이지: '))
    recommend=input('비고: ')
    data=[title,pub_date,pub,pages,recommend]
    sql='insert into books values(?,?,?,?,?)'
    cur.execute(sql,data)
    conn.commit()
    conn.close()

def select_data():
    conn=db_conn()
    cur=conn.cursor()
    title=input('책제목을 입력하세요: ')
    title='%'+title+'%'
    sql="select * from books where title like ?"
    cur.execute(sql,(title,))
    print(cur.fetchall())
    conn.close()

def update_data():
    pass

def delete_data():
    pass

