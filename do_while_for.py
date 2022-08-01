from random import randint

if __name__ == '__main__':
    print("学习循环")
    # 使用while 和 for 循环
# i = 1
# while i < 100:
#     print(i)
#     i += 1

# 猜数字游戏
# a = randint(1, 10)
# print(a)
# for n in range(3):
#     print(n)
#     x = int(input("请输入一个数字："))
#     if x > a:
#         print("too big")
#     elif x < a:
#         print("too small")
#     else:
#         print("恭喜！")
#         break
#     print("机会已用完")
# 打印正等腰三角形

#    *
#   ***
#  *****
# *******
# a = 6
# i = 1
# while i < a:
#     k = 1
#     while k <= a - i:
#         print(' ', end='')
#         k += 1
#     j = 1
#     while j <= 2 * i - 1:
#         print("*", end='')
#         j += 1
#     print("\n")
#     i += 1
# *********
#  *******
#   *****
#    ***
#     *
# 打印倒等腰三角形
# a = 6
# i = 1
# while i < a:
#
#     j = 0
#     while j < i - 1:
#         print(' ', end='')
#         j += 1
#
#     k = 1
#     while k < 2*a-2*i:
#         print('*', end='')
#         k += 1
#     i += 1
#     print('\n')
# 报数游戏 7 和 7 的倍数
index = 0
for i in range(1, 51):
    if i % 7 == 0 or i % 10 == 7:
        continue
    else:
        index += 1
    print(index)
