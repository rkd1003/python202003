import pymysql

def conndb():
    conn = pymysql.connect(host='maria',
                            user='root',
                            password='qwer1234',
                            db='test',
                            cursorclass=pymysql.cursors.DictCursor)
    return conn

def createTable():
    conn=conndb()
    c=conn.cursor()
    sql='drop table if exists product'
    c.execute(sql)
    sql='''
    create table if not exists product(
        product_id int,
        product_name varchar(50),
        price int default 0,
        description text,
        picture_url varchar(500),
        CONSTRAINT PRIMARY KEY (product_id))
    '''
    # c.execute(sql)

    # sql='''insert into product values(1,'사과',10000,'청도 끝사과 당도가 매우 높음','apple.jpg')'''
    # c.execute(sql)

    # sql='''
    # create table cart(
    #     cart_id number primary key,
    #     userid varchar2(50) not null,
    #     product_id references product(product_id),
    #     amount number default 0
    # )'''
    c.execute(sql)
    conn.commit()
    conn.close()

def insertdata():
    conn=conndb()
    c=conn.cursor()
    data=[]
    product_id=input('제품번호: ')
    product_name=input('제품이름: ')
    price=int(input('제품가격: '))
    description=input('제품비고: ')
    picture_url=input('제품사진: ')
    data=[product_id,product_name,price,description,picture_url]
    sql='insert into product values(%s,%s,%s,%s,%s)'
    c.execute(sql)
    conn.commit()
    conn.close()

def listdata():
    pass

def searchdata():
    conn=conndb()
    c=conn.cursor()
    sql='select * from product'
    c.execute(sql)
    
    for row in c:
    pass    

def updatedata():
    # conn=conndb()
    pass
def deletedata():
    pass