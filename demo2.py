from ftplib import FTP

if __name__ == '__main__':
    ftp = FTP()
    # 连接
    ftp.connect(host="10.118.21.88", port=53521)
    # 登录
    ftp.login(user="ftp1", passwd="Pinghang@ftp0$")
    # 登录成功
    ftp.getwelcome()
    # 切换路径
    ftp.cwd("/yunxi-181/")
    # 显示目录下所有目录信息
    print(ftp.dir())
    # 获取目录下的文件
    # print(ftp.nlst())

    # close 与 quit 的区别
    # 1、close()：关闭当前窗口，如果它是当前打开的最后一个窗口，则退出浏览器
    # 2、quit()：退出此驱动程序，关闭所有相关窗口

    # 关闭ftp
    # ftp.close()

    # 推出ftp
    ftp.quit()
