#문자열이 시작하는지 끝나는지 리스트 속에 있는지 없는지 체크!
hi = "안녕하세요 여러분 저는 김지형입니다"
print(hi.startswith("안녕"))
print(hi.endswith("입니다"))

answer_list =  [True, False, True, True]

def solution(list):
    if False in answer_list:
        return "거짓입니다"

print(solution(answer_list))
