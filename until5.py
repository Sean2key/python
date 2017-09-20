# 简单的if
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

age =3
if age < 4 :
	print('You are free')
elif age < 18:
	print('You are half money')
else:
	print('You are all money')

# 字典
person = {'name':'xiao li', 'age':16,'sex':'man'}
print(person['name'])

# 添加键值
person['money']=200
person['car']=True
print(person)

# 删除键值
del person['sex']
print(person)

# 遍历字典
for key,value in person.items():
	print(key + ': ' + str(value))

# 遍历所有键
for key in person.keys():
	print(key)

# 遍历所有指
for value in person.values():
	print(value)

# .key() 不仅用于遍历还可以返回列表
if 'sex' not in person.keys():
	print('字典没有 sex 键')