# set 集合 对比java中的set
# 创建集合
if __name__ == '__main__':
    set_temp = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, '@'}
    set_temp1 = set_temp
    # set_temp = set('@')
    # 增加一个数据
    set_temp.add('a')
    # 增加多个数据，需要使用序列【】
    set_temp.update(['a', 'b'])
    set_temp.update('abc')
    set_temp.remove('@')  # 移除集合中的数据，如果存在则移除，如果不存在则报错
    set_temp.discard('@')  # 移除集合中的数据，如果存在则移除，如果不存在，不会报错
    print(set_temp)
    print('-' * 20)
    print(set_temp1)
    print(set_temp1.pop())  # 随机删除一个数据，并返回。（不一定是随机，可能累计出栈，需要验证）
    print(set_temp1)
    print('-' * 20)
    for x in set_temp:
        print(x, end=' ')

