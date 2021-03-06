# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-12 09:44
# 文件名称: hw_006_敏感词过滤程序.py
# 开发工具: PyCharm

# 需求:我们做开发的时候常常需要录入数据,但是很多数据中往往包含我们
# 并不想要展示的内容,也就是敏感词汇,现在需要做一个程序,过滤掉敏感词

"""
分析:
1 首先需要有一个敏感词汇的列表
2 然后对比录入的数据,如果录入的数据中包含敏感词汇,就处理掉
"""
# 1 定义敏感词列表
l = ['敏感词1', '敏感词2']

# 2 录入数据 需要循环录入
# 2.1 需要定义一个空列表来存储用户录入
contents = []
while True:
    # 方便测试 录入的时候记得包含 敏感词1  敏感词2
    s = input("请输入内容:\n")
    # 进行敏感词处理
    # s.replace('敏感词1', '*')
    # s.replace('敏感词2', '*')
    for i in l:
        # print(i)
        # 注意了 字符串是不可修改类型,替换后必须接收
        # 替换不会修改原内容,而是返回替换后的值
        s = s.replace(i, '*')
    print(s)
    exit()
    contents.append(s)
    print('数据录入成功,是否继续?y/n\n')
    if input() == 'n':
        break
# 打印数据内容测试
for i in contents:
    print(i)
