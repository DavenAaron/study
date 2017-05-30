
# 是否包含 __contains__
# name = 'wangzenghui'
# print(name.__contains__('zenghui'))
# print('zenghui' in name)

# 是否相等 __eq__
# name = 'wangzenghui'
# print(name.__eq__(name))

# 反射  __getattribute__

# 首字母大写 capitalize()
# name = 'wangzenghui'
# print(name.capitalize())

# 首字母小写  casefold（）
# name = 'Wangzenghui'
#result = name.casefold()
#print(result)

# wangzenghui居中，其他空格填充满20字符
#name = 'wangzenghui'
#result = name.center(20)
#print(result)

# [****Wangzenghui*****]
#result = name.center(20,'*')
#print(result)

# 查找name变量中n符出现的次数
# name = 'wangzenghui'
# print(name.count('n'))

# 查找name变量中字符n，在第2-5个字符间出现的次数
# name = 'wangzenghui'
# result = name.count('n',2,4)
# print(result)

# 指定字符编码
#name = '王增辉'
#result = name.encode('gbk')
#print(result)

# 判断字符是否以指定字符结尾
# name = 'wangzenghui'
# result = name.endswith('hui')
# print(result)

# 判断指定范围内的字符是否以指定字符结尾
# name = 'Wangzenghui'
# result = name.endswith('g',0,4)
# print(result)

# with 文件操作
# with open('nginx.log', 'wt') as f:
#     f.write('hello, world!')

# 将tab 转换成空格
# name = 'a\tboy'
# result = name.expandtabs()
# #print(len(result))
# print(result)

# 查找指定字符的数量
# name = 'wangzenghui'
# result = name.find('n')
# print(result)

# index 找不到就会抛出异常
# name = 'wangzenghui'
# result = name.index('y')
# print(result)

# 字符串拼接
# name = "tomcat {0} with {1}"
# result = name.format('good','haha')
# print(result)

# 判断字母+数字
# name = 'wangzenghui'
# result = name.isalnum()
# print(result)


# li = ['h','o','w','a','r','e','y','o','u']
# result = "".join(li)
# print(result)

# # 去除左边空格
# name = ' wangzenghui'
# print(name)
# result = name.lstrip()
# print(result)

# name = 'wang zenghui'
# print(name)
# result = name.lstrip('w')
# print(result)

# 以指定的字符为分割点
# name = 'wangzenghui'
# result = name.partition('zeng')
# print(result)

# 字符替换
# name = 'wangzenghui'
# result = name.replace('n','H',1)
# print(result)

#指定分割字符，将字符串分裂成多个字符串组成的列表
# name = 'wangzenghui'
# print(name.split('n'))

# name = """
# wang
# zeng
# hui
# """
# #result = name.splitlines()
# result = name.splitlines()
# print(result)

# 检测字符串是否以指定字符串开头
# name = 'wangzenghui'
# result = name.startswith('wang')
# print(result)

# name = '   tomcat'
# result = name.strip()
# print(result)

# 大小写转换
# name = 'Wang Zenghui'
# result = name.swapcase()
# print(result)

# 连接符 join
# lst = ['my', 'name', 'is', 'tomcat']
# print(' '.join(lst))
# print(','.join(lst))

## 每次创建新的对象
# s = ''
# for x in lst:
#     s += ' ' + x
# print(s)

# 字符串的分割
# split，rsplit,splitlines,partition,rpartition

# split 将字符串分割成列表
# s = 'my name is wangzenghui'
# print(s.split())

# 指定默认分割字符为is（从左往右分割）
# s = 'my name is wangzenghui'
# print(s.split('is'))

# 指定分隔符及其分割次数 (分割次数为-1，则分割所有)
# s = 'my name is wangzenghui'
# print(s.split(' ',1))

## --- rsplit   从右往左分割指定次数
# s = 'my name is wangzenghui'
# print(s.rsplit(' ', 1))

