import time as t
# names = ['Tom','Jerry']
# names.append("Yami")
# names.remove(names[0])
# for name in names:
#     print(name)

# names = ['Tom','Jerry']
# names.insert(1,"Yami")
# for name in names:
#     print(name)

# too_expensive = 'ducati'

# print(too_expensive.title())

# numbers = range(1,10)
# squares = []
# for number in numbers:
#     sque = number ** 2
#     squares.append(sque)
#
# print(squares)

# 列表解析，在中括号中包裹需要插入的数值加上for循环的表达式
# numbers = range(1,10)
# squares = [value ** 2 for value in numbers]
# print(squares)

# 数到20
# squares = [num for num in range(1,21)]
# print(squares)

# 一百万
# squares = [num for num in range(1,1000001)]

# for square in squares:
#     print(square)
#     t.sleep(0.1)

# 一百万求和
# squares = [num for num in range(1,1000001)]

# print(min(squares))
# print(max(squares))
#求和
# start_time = t.time()
# print(sum(squares))
# end_time = t.time()

# print(end_time - start_time)

# 奇数，通过给函数 range()指定第三个参数来创建一个列表，其中包含
# 1～20 的奇数，再使用一个 for 循环将这些数打印出来。
# nums = list(range(1,21,2))
# for num in nums:
#     print(num)

# 3的倍数,3每次跳3步都是3的倍数
# nums = list(range(3,31,3))
# for num in nums:
#     print(num)

# 立方 创建一个列表，其中包含前 10 个整数（1～10）的立方，再使用一个 for循环将这些立方数打印出来。
nums = []
for value in range(1,11):
    num = value ** 3
    nums.append(num)

for num in nums:
    print(num)

# 立方解析 使用列表解析生成一个列表，其中包含前 10 个整数的立方。
nums = [value **3 for value in range(1,11)]
print(nums)
