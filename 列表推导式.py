# 学习并使用列表推导式
if __name__ == '__main__':
    # 普通列表推导式
    list1 = [i for i in range(10)]
    print(list1)
    list2 = [i for i in range(0, 10, 2)]
    print(list2)
    print('*' * 20)
    # 带有if的列表推导式
    list3 = [i for i in range(10) if i % 2 == 1]
    print(list3)
    print('*' * 20)
    # 多个for循环实现列表推导式
    list4 = [(i, j) for i in range(10) for j in range(10)]
    print(list4)
    list5 = [(i * j) for i in range(10) for j in range(10)]
    print(list5)
    list6 = [(i * j) for i in range(10) for j in range(10) if i % 2 == 0 if j % 2 == 1]
    print(set(list6))
