#리스트 컴프리핸션과 맵(map)

# List Comprehension
[list(a) for a in zip(*mylist)]

# Map
list(map(list, zip(*mylist)))

map 함수는 iterator를 리턴> 그래서 map 함수를 적용한 후, list로 형 변환을 해주어야 함
해주지 않으면 map at object x234l23l4k23 이런형태로 출력됨

list comprehension을 사용하면 따로 형 변환해줄 필요가 없다.
