# 字典推导式
# 快速合并列表为字典或提取字典中的目标数据
if __name__ == '__main__':
    dict1 = {i: i ** 2 for i in range(5)}
    print(dict1)
    print('*' * 20)
    # 将两个列表合并成一个字典
    list1 = ['name', 'sex', 'age']
    list2 = ['malinfei', 'male', '18']
    dict2 = {list1[i]: list2[i] for i in range(len(list2))}
    print(dict2)
    print('*' * 20)
    # 需求：提取上述电脑数量大于等于200的字典数据
    counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}
    dict3 = {k: v for k, v in counts.items() if v >= 200}
    print(dict3)
