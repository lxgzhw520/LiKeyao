# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-11 09:51
# 文件名称: hw_007_实战案例_猜拳小游戏.py
# 开发工具: PyCharm

# 新知识:随机数 模块

# 导入模块
import random

# 使用模块方法生成随机数
random_num = random.randint(1, 3)
# 打印测试 自己多运行即便,看是否随机
print(random_num)
# 需求 玩家输入 石头1 剪刀2 或布3 电脑随机出拳,判断输赢
# 分析
# 罗列出电脑赢的情况,咱不考虑平局,只要电脑没赢,就算玩家赢
"""
石头 1  赢  剪刀2
剪刀 2  赢  布  3
布   3  赢  石头 1
"""
# 先写出电脑赢的情况
# 新知识 逻辑运算符  and 表示并的关系  or 表示且的关系 not 表示非的关系

# 先定义两个变量,分别代表电脑出拳和玩家出拳
# 新知识 None 代表什么都没有,是一个特殊的值
computer = None
player = None

# 录入用户的值
player = input("请出拳(1石头 2剪刀 3布):")
computer = str(random_num)  # 新知识 str(数字) 能够将数字转换为字符串

# 电脑赢  新知识 \加在一段代码末尾表示换行 后面不能加任何内容哪怕注释
if (computer == '1' and player == '2') \
        or (computer == '2' and player == '3') \
        or (computer == '3' and player == '1'):
    print('电脑赢了')
else:
    print("玩家赢了")
