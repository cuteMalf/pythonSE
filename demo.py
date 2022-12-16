# 1.导包
import pymysql

if __name__ == '__main__':
    # 2.创建连接对象
    conn = pymysql.connect(host="localhost",
                           port=3306,
                           user="root",
                           password="admin",
                           database="test",
                           charset="utf8mb4")

    # 3.获取游标，用于执行SQL语句
    cursor = conn.cursor()
    sql = "select * from yx_dic limit 100;"

    # 4.执行sql语句
    cursor.execute(sql)
    # 获取单行结果集,返回的是一个元组
    # row = cursor.fetchone()
    # 获取所有结果集
    allRows = cursor.fetchall()
    for row in allRows:
        print(row)
    # 5.关闭游标
    cursor.close()
    # 6.关闭连接
    conn.close()
