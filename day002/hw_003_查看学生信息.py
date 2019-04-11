# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-11 09:32
# 文件名称: hw_003_查看学生信息.py
# 开发工具: PyCharm

# 需求,按照指定格式,在用户录入个人信息后打印
# 格式
"""
姓名：小明
年龄：18 岁
性别：是男生
身高：1.75 米
体重：75.0 公斤
"""

# 思路:
# 让用户输入指定信息并存储
name = input("姓名:")
age = input("年龄:")
gender = input("性别:")
height = input("身高(m):")
weight = input("体重(kg):")
print('---' * 22)  # 字符串可以做乘法 打印22个'---'
# 格式化输出
info = """
姓名：{}
年龄：{} 岁
性别：{}
身高：{} m
体重：{} kg
""".format(name, age, gender, height, weight)
print(info)
