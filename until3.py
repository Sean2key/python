# 列表
print("list:")

names = ['xiao li', 'zhang san', 'wang kai', 'zhou wu']
print(names)

# 访问元素，下标为0
print(names[0])
print(names[3])
print(names[2].title())

# 访问元素，下标为负数就是倒数第几个
print(names[-1])
print(names[-2].title())
print(names[-3].title())

# 修改元素
print(names)
names[0] =  "lao liu"
print(names)

# 添加元素
names.append('xiao li')			# append 添加一个元素到列表末尾
print(names)

# 插入元素
names.insert(2, 'hu han')			# insert 插入一个元素到 2（第三个） 的下标位置
print(names)

# 删除元素
del names[2]						# del 删除一个元素
print(names)

# 删除元素并返回值
p = names.pop()
print(p , names)					# 删除最后一个元素，并返回给p

p = names.pop(2)					# 删除下标为2的元素，并返回给p
print(p , names)	

# 删除指定元素
names.remove('zhang san')		# 删除指定元素一次
print(names)


# 列表排序
cars = ['bwm', 'audo', 'toyota', 'mesaidesi', 'dazhong', 'qq']
cars.sort()						# 从小到大排序
print(cars)
cars.sort(reverse=True)			# 从大到小排序
print(cars)

# 列表临时排序 并不影响原先列表顺序
cars = ['bwm', 'audo', 'toyota', 'mesaidesi', 'dazhong', 'qq']
print(cars)
print(sorted(cars))
print(cars)
print(sorted(cars, reverse = True))
print(cars)

# 列表反转，倒过来并非排序
cars.reverse()
print(cars)

#列表长度
print(len(cars))