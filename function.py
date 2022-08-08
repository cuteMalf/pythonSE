# 函数
if __name__ == '__main__':
    def sum_two_num(a, b):
        """求和函数"""

        def div1(x, y):
            x = x - 1
            y = y - 1
            return x, y

        # t = div1(a, b)
        # return t[0] + t[1]
        a, b = div1(a, b)
        return a + b


    print(sum_two_num(4, 2))
    print('*' * 20)
    # 交换临时变量
    a = 1
    b = 2
    a, b = b, a
    print(f'a={a} b={b}')
