# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-12 06:17
# 文件名称: hw_003_求1到100之间所有数的和.py
# 开发工具: PyCharm

# 需求:求1-100之间所有数的和
# 分析:使用循环
# 步骤:循环变量不断自增,定义另一个变量,每次循环都加上自增后的变量

index = 0
count = 0
while index < 100:
    # index 分别是1-100
    index += 1
    # count分别是1+...+100
    count += index
print(count)
