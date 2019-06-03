# -*- coding: utf-8 -*-
# @Time    : 2019/5/11 17:23
# @File    : project_path.py
import os
import datetime

# 获取当前时间#
now_time = datetime.datetime.strftime(
    datetime.datetime.now(), '%Y-%m-%d')

project_path = os.path.realpath(__file__)  # 获取当前文件目录
# main目录下 文件夹地址
# 获取main文件夹路径
main_path = os.path.split(os.path.split(project_path)[0])[0]
# 获得conf 文件夹路径
conf_path = os.path.join(main_path, 'conf', 'config.ini')
# 获得log文件夹路径
log_path = os.path.join(main_path, 'log')
# 获img文件夹路径
img_path = os.path.join(main_path, 'img', now_time)


def mkdir(path):
    path = path.strip()
    is_exists = os.path.exists(path)
    # 判断结果
    if not is_exists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        print(path + '创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False


if __name__ == '__main__':
    # print(project_path)
    # print(main_path)
    # print(conf_path)
    # print(log_path)
    mkdir(img_path)
