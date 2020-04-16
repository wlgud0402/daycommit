#FOR문 돌려서 index 찾기

students =[
    {
        "id":5,
        "name":"김지형"
    },
    {
        "id":50,
        "name":"김기현"
    },
    {
        "id":88,
        "name":"이동은"
    }
]
# 1.파이썬 배열 반복문
idx =0  #직접 인덱스를 만들고 처리해야한다.
student_id = 50
for student in students:
    if student["id"] == student_id:
        print(idx)
    idx +=1

# 2.range를 이용하기
for i in range(0, len(students)):
    if students[i]["id"] == student_id:
        print(i)

# 3.이넘레이트(enumerate) 사용 >>인덱스와 값 모두 뺄 수 있다.
for i, student in enumerate(students):
    if student["id"] == student_id:
        print(i, student)

