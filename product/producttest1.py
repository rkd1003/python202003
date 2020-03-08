import productF

productF.createTable()
while True:
    print('''
    1. 제품입력
    2. 제품목록
    3. 제품검색
    4. 제품수정
    5. 제품삭제
    6. 종료
    메뉴선택 >> ''')

    menu=input()
    if menu=='1':
        productF.insertdata()
    elif menu=='2':
        productF.listdata()
    elif menu=='3':
        productF.searchdata()
    elif menu=='4':
        productF.updatedata()
    elif menu=='5':
        productF.deletedata()
    elif menu=='6':
        break
    else:
        print('메뉴를 잘못 선택하셨습니다.')