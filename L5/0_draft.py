import re
line = 'abc83 cde7 1 b 24'
otvet = re.findall(r'\d+',line )
num = int((' , '.join(otvet)))
print(num)

