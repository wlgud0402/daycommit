#for 문과 while문의 차이

days = ['Mon','Tue','Wen','Thr','Fri','Sat','Sun'] #총 7개의 요소가 들어있다.


while len(days):
    print(days[0])
    days.pop(0)

for day in days:
    print(day)