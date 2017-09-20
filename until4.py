# 操作列表

names = ['xiao li', 'zhang san', 'wang fei', 'zhou hui', 'bo lan']

for name in names:
	print(name)

# 生成数字
for i in range(1,5):				# 生成数字：从1到5（不包含5）
	print(i)

for i in range(3,10):				# 生成数字：从3到10（不包含10）
	print(i)

# 创建数字列表
nums = list(range(0,10))			# 生成数字：从0到10（不包含10） 到 列表中
print(nums)

# range 步长
nums = list(range(1,10,2))			# 生成数字：从0到10（不包含10） 到 列表中，间隔2
print(nums)

# 数字列表 最小值
mins = min(nums)
print(mins)

# 数字列表 最大值
maxs= max(nums)
print(maxs)

# 数字列表 合
sums = sum(nums)
print(sums)

# 列表解析
squares = [value**2 for value in range(1,10)]
print(squares)
		# 循环语句放前面，循环条件放后面

# 切片
print(names)
print(names[0:3])		# 输出下标0~3
print(names[1:4])
print(names[2:])
print(names[:3])
print(names[-2:])

# 遍历切片
for name in names[:3]:
	print(name.title())

# 复制列表
cars = ['dawo', 'toyota', 'benchi', 'Audi', 'Qiya']
newcars = cars[:]
cars.append('qq')
newcars.append('fengtian')
print(newcars)
print(cars)

# 元祖 不能改变值的列表
dimensions = (200, 50)
print(dimensions)
print(dimensions[0])
print(dimensions[1])

# 遍历元祖
for i in dimensions:
	print(i)
