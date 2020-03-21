var user =confirm("계속할까요?");
if(user==true){    //파이썬은 True인데 여기선 true 소문자, 자바나 c++와 비슷함,{ }도 파이썬은 :
    document.write("확인 버튼을 눌렀습니다.");
}else{
    document.write("취소 버튼을 눌렀습니다.");
}

document.write("<br>");

user = prompt("아이디를 넣으세요","admin");
document.write(user)