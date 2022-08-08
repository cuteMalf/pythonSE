# 集合推导式
if __name__ == '__main__':
    set1 = {i for i in range(10)}
    print(set1)
    print('*' * 2)
    list1 = [1, 2, 2, 1, 4, 1]
    set2 = {i ** 2 for i in list1}
    print(set2)
