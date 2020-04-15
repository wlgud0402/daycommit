#for 문과 if문에서 return의 순서와위치 실수

1.옳은것
 if uuid == None:
    return redirect("/nocookie")

for user in db_users:
    if uuid == user["uuid"]:
        return render_template("write.html")
return "너왜 쿠키 위조해" #return 시키는 위치 주의
#for문의 아래에 있어야 for문이 끝까지 다돌고 없을때 "위조 메시지를 출력한다"

2.틀린것
 if uuid == None:
    return redirect("/nocookie")

for user in db_users:
    if uuid == user["uuid"]:
        return render_template("write.html")
    return "너왜 쿠키 위조해"
#if 문의 아래에 있을시에는 for문이 다 돌기도 전에 만약 100개의 항목을 체크해야하지만
# 첫번째 반복문 실행시부터 if문에 일치하지 않는다면 바로 return을 시켜버림. >> 100개를 다 반복해서 찾아야 하므로for문 아래에 return이 들어가야 한다.