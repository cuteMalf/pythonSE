# 学习并使用字典,对比java中的map
if __name__ == '__main__':
    body = {'name': 'ken thompson', 'sex': 'male', 'age': '26', 'hobby': 'female'}
    body['girlfriend'] = 'liutt'
    print(body)
    body['girlfriend'] = 'girls'
    print(body)
    print(body['girlfriend'])
    del body['girlfriend']
    print(body.get('girlfriend', 'tiktok_grils'))
    print('*' * 20)
    print(body)
    print(body.keys())
    print(body.values())
    print(body.items())
    print('*' * 20)
    body1 = body.items()
    print(type(body1))
    print('*' * 20)
    # 遍历键值对
    for k, v in body1:
        print(f'{k}={v}')

    body.clear()
    print(body)
# 序列 （列表 字典 集合）