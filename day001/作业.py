# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/4/10 17:13
# 文件名称: 作业.py
# 开发工具: PyCharm

# 需求 读取Excel文件 存入数据库

import pandas as pd

# 读取 调用pandas自带功能可以一键读取
data = pd.read_excel('Ejemplo MerchantSettlement-20190408-20190411.xlsx')
print(data)

# 存入数据库
