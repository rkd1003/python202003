import sqliteDB

while True:
    print('''
    1. 테이블 생성
    2. 데이타 입력
    3. 데이타 수정
    4. 데이타 삭제
    5. 데이타 리스트
    6. 종료
    ''')
    menu=input()
    if menu=='1':
        sqliteDB.create_table()
    elif menu=='2':
        sqliteDB.insert_data()
    elif menu=='3':
        sqliteDB.update_data()
    elif menu=='4':
        sqliteDB.delete_data()
    elif menu=='5':
        sqliteDB.select_data()
    else:
        print("메뉴를 잘못선택하셨습니다.")