# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-12 06:24
# 文件名称: hw_005_终止循环.py
# 开发工具: PyCharm

# 需要,循环打印1-100之间的数,当打印到55的时候跳过循环
# 新知识:跳过循环的关键字continue
# 分析:和之前的一样,多了个continue而已

index = 0
while index < 100:
    index += 1
    if index == 55:
        print('--' * 22)
        continue
    else:
        print(index)
