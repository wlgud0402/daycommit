#이쁘게 조건줘서 출력할수 있는 pprint
from pprint import pprint

info = {
    "name":"지형",
    "age":25,
    "address":"남양주시"
}

print(info)
pprint(info, width=10, indent=10)