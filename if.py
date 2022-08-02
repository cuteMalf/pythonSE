# 用来学习使用python的运算和条件结构
if __name__ == '__main__':
    # a = int(input("输入第一个数"))
    # b = int(input("输入第二个数"))
    # c = int(input("输入第三个数"))
    #
    # if a > b and a > c:
    #     print(a)
    # if b > a and b > c:
    #     print(b)
    # if c > a and c > b:
    #     print(c)
    #
    # score = int(input("输入一个成绩："))
    #
    # if score > 90:
    #     print("A")
    # elif 60 <= score < 90:
    #     print("B")
    # else:
    #     print("C")

    state = input("输入红绿灯状态")

    if state == '红灯':
        print("禁止通行")
    elif state == '绿灯':
        print("可以通行")
    else:
        print("等待通行")
