# 学习并使用字符串
# str1 = int(input("请输入任意数字："))
#
# str2 = ''
# for i in range(1, str1 + 1):
#     str2 = str2 + str(i)
# print(str2)
#
# word = int(input("选取幸运数字："))
# print(str2[word-1:word])


# 字符串切片
# str1 = '''codeccan'tdecodebytesnposition '''
# print(str1[1:8])  # 从下表1截取到下标8的字符串，包括1不包括8
# print(str1[1:5:3])  # 从下标1截取到下标5，截取步长为3，每隔3个字符截取一个
# print(str1[:5])  # 从下标为0截取到下标为5的，前闭后开
# print(str1[1:])  # 从下标为1的开始，截取到字符串结束
# print(str1[:])  # 截取整个字符串
# print(str1[::3])  # 截取步长为3 ，每隔3个截取一个
# print(str1[:-1])  # 倒着截取字符串
# print(str1[-4:-1])
# print(str1[::-1])  # 倒叙

# 字符串查找
# name = 'malinfei'
# print(name.find('i', 0, len(name)))
# print(name.find('in'))  # 查找字串在字符串中出现的位置
#
# name1 = '''liutingting'''
#
# print(name1.index('iu'))
# print(name1.index('g', 0, len(name1)))  # 查找子串在字符串中出现的位置
#
# print(name.rfind('f', 0, len(name)))
#
# print(name1.rindex('u', 0, len(name1)))

# 返回字串在字符串中出现的

# name='this is a python project!'
# print(name.count('is'))
# print(name.count('is',0,11))
# print(name.count('@'))

# 字符串修改

# name = 'this is a python project! p'
# print(name.replace('is', '@'))
# print(name.replace('o', 'O', 1))
# print(name.replace('p', 'P', 3))

# 根据字符分割字符串

# name='abcd,feg,hijklm.uvwxyz！dshahf,sdsd'
# print(name.split(','))
# print(name.split(',',2))
# print(name.split('*'))
#
# str1 = 'hello'
# str2 = 'world'
#
# print(str1.join(str2))

# list1 = ['hello', 'world']
# tuple1 = ('hello', 'python')
#
# print(','.join(list1))
# print('-'.join(tuple1))

# name = 'malinfei'
# print(name.capitalize())  # 将字符串的第一个字母转成大写，其余字母不变
#
# myStr = 'i love you ltt and my  , ,family'
# print(myStr.title())
#
# list1 = ['hello', 'world']
# print(list1[1].title())

# str1='hellO world'
# print(str1.lower())
# print(str1.upper())

# str1=' hello world '
# print(str1.lstrip())
# print(str1.rstrip())
# print(str1.strip())

# str1 = 'world'
# print(str1.ljust(10, '.'))
# print(str1.rjust(10, '.'))
# print(str1.center(10, '.'))

# name = 'helloworld1'
# name1 ='hello'
# name2='134'
# name3=' '
# # print(name.startswith('hello'))
# # print(name.endswith('world'))
#
# # 判断字符串是否字母组成
# print(name1.isalpha())  # 判断是否只有字母
# print(name.isalnum())   # 判断是否只有字母和数字
# print(name2.isdigit())  # 判断是否只有数字
# print(name3.isspace())

# 输入一个字符串，打印所有奇数位上的字符(下标是1，3，5，7…位上的字符)
# my_str='abcdefghijklmn'
# print(len(my_str))
# print(my_str[::2])

# 输入用户名，判断用户名是否合法(用户名长度6~10位)
# username=input("请输入用户名：")
# if 6<=len(username)<=10:
#     print("合法")
# else:
#     print("非法")

# 给定一个文件名，判断其尾部是否以".png"结尾

# photo = 'wallhaven-j3dg1m.jpg'
# if photo.startswith('.png'):
#     print(True)
# else:
#     print(False)

# 给定一个字符串，如：
# mystr = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
# 使用所学的知识，从字符串中随机取出4个字符，生成验证码。
from random import randint

mystr = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
l = len(mystr)
x = randint(0, l)
y = randint(0, l)
z = randint(0, l)
u = randint(0, l)
print(mystr[x:x + 1]+mystr[y:y + 1]+mystr[z:z + 1]+mystr[u:u + 1])
