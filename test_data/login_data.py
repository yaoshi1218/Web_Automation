# -*- coding: utf-8 -*-
# @Time    : 2019/5/12 18:26
# @File    : login_data.py

# 数据 1. 账号 2. 密码 3、预期 caseid
# 测试用例分组
# 用户分组依据：测试用例方法步骤逻辑是否发生变化。

# 用户成功
user_info_success = [{"id": '1', "username": "18684720553", "pwd": "python", "expected": "小蜜蜂96027921"}]

# 错误数据
user_info_error = [
    {"id": '1', "username": "", "pwd": "", "expected": "请输入手机号"},
    {"id": '2', "username": "12", "pwd": "", "expected": "请输入正确的手机号"},
    {"id": '3', "username": "18654321456", "pwd": "", "expected": "请输入密码"},
]

# 没有权限的数据
user_info_authorize = [
    {"id": '1', "username": "18654321456", "pwd": "12", "expected": "此账号没有经过授权，请联系管理员!"}
]
