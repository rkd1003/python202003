function func(){
    var season = prompt("좋아하는 계절?","봄");
    var message = "";
    var img ="";
    
    switch(season){  // switch(숫자)
        case "봄":
            message="봄을 좋아하시네요";
            img = "01.jpg";
            break;
        case "여름":
            message="여름을 좋아하시네요";
            img = "02.jpg";
            break;
        case "가을":
            message="가을을 좋아하시네요";
            img = "03.jpg";
            break;
        case "겨울":
            message="겨울을 좋아하시네요";
            img = "04.jpg";
            break;
        default:
            alert("번호를 잘못 입력했습니다.(1~4번을 눌러주세요)");
    }
    
    document.getElementById('message').innerHTML=message;
    document.getElementById('img').src = "/static/img/" + img
}