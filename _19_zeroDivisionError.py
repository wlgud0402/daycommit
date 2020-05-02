#zero division 에러 처리방법
#어떠한 수를 0 으로 나눗셈을 할때 발생하는 오류이다
#이를 만나면 실행이 거기서 중지 되버리기 때문에 try except구문으로 오류를 지정해 주어야 한다.

lst = [1,3,5,0,2]
 
for i in lst:
    try:
        print(10 / i)
    except ZeroDivisionError:
        print("ZeroDivision")
