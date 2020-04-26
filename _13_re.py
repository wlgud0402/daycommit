import re

letter = "I wish I were gay"

print(re.findall('wish',letter))

# |또는
print(re.findall('wish|gay',letter))

#앵커 ^(시작), $끝
print(re.findall('^I', letter))

print(re.findall('gay$',letter))