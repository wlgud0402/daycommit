years_list =[1980,1981,1982,1983,1984,1985]

print(years_list[3])
print(years_list[-1])

print()
print()

things =["mozzarella", "cinderella","salmonella"]
print(things[1].capitalize()) #첫글짜 대문자로 바꿔서 출력함 but 리스트 값이 내부적으로 변화하진 않는다.

things[1] = things[1].capitalize() #이렇게 할당하면 내부값도 바뀜
print(things)

