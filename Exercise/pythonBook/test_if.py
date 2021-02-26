a = 'Porsche'
b = 'Porsche'
# 比较是否相等
# if a==b :
#     print(f'a和b相等,都是{a}')
# else :
#     print('a not equal b')

# 输出：
# a和b相等,都是porsche

# 检查是否相等时，python默认是不忽略大小写的，可以使用lower()方法来转换成小写后再进行比较
# a = 'porSche'
# b = 'porsche'

# if a.lower() == b:
#     print(f'a和b相等,都是{a.lower()}')
# else:
#     print('a not equal b')
#
# print('a的值为', a)
# 输出：
# a和b相等,都是porsche
# a的值为 porSche

# 检查是否不相等，使用!=符号,输出：a not equal to b
# a = 'porSche'
# b = 'porsche'
# if a != b :
#     print('a not equal to b')

# 数值比较与多条件比较
a = 18.8
b = 189

if a == b:
    print('a equals b ?', a == b)
elif a > 100:
    print('a>100?', a > 100)
elif a < b:
    print('a<b?', a < b)
elif a >= 100 and a < b:
    print("a>=100 and a<b?", a >= 100 and a < b)
else:
    print('a not equals b ?', a != b)

# 序列的比较还可以使用 in 和 not in