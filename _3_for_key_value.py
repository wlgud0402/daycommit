drinks={
    '마티니':{'보드카','버몬트'},
    '블랙러시안':{'보드카','칼루아'},
    '화이트러시안':{'크림','칼루아','보드카'},
    '맨해튼':{'루','버몬트','비터스'},
    '스크류':{'오렌지쥬스','보드카'}
}

for name,contents in drinks.items():
    if '보드카' in contents:
        print(name)

print()
print()

for name,cnetnes in drinks.items():
    if '보드카' in contents and not('버몬트' in contents or '크림' in contents):
        print(name)

print()
print()

for name,contents in drinks.items():
    if contents & {'보드카','오렌지쥬스'}:
        print(name)

print()
print()

for name,contents in drinks.items():
    if '보드카' in contents and not contents & {'버몬트','크림'}:
        print(name)