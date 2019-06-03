# -*- coding: utf-8 -*-
# @Time    : 2019/5/18 13:46
# @File    : investment_data.py


# 错误的投标额(弹窗)
error_data = [{"id": '1', "amount": '0', "expected": "请正确填写投标金额"},
              {"id": '2', "amount": '-100', "expected": "请正确填写投标金额"},
              {"id": '3', "amount": '110', "expected": "投标金额必须为100的倍数"},
              {"id": '4', "amount": ' ', "expected": "请正确填写投标金额"},
              {"id": '5', "amount": '900000', "expected": "投标金额大于可用金额"}]

# 不符合规则的投标额
error_rule_data = [{"id": '1', "amount": '1', "expected": "请输入10的整数倍"},
                   {"id": '2', "amount": '-0.1', "expected": "请输入10的整数倍"},
                   {"id": '3', "amount": '-1', "expected": "请输入10的整数倍"},
                   {"id": '4', "amount": '1001', "expected": "请输入10的整数倍"}]
# 正确投资
investment_success_data = [{"id": '1', "amount": '100', "expected": "投标成功！"}]
