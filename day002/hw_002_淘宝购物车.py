# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-11 09:24
# 文件名称: hw_002_淘宝购物车.py
# 开发工具: PyCharm

# 需求,完成购物车结算功能
# 分析:
# 1 获取购物车商品名称及价格 购买数量
good = input("商品名称:")
price = input("商品单价:")
count = input("购买数量:")
# 2 计算总价
need_pay = int(price) * int(count)  # 转换为整型
# 3 让用户确认支付
print("您购买{}共{}.该商品单价为{},总价是{},请您确认无误后付款:"
      .format(good, count, price, need_pay))
is_pay = False
# 4 确认用户已支付,完成结算
is_pay_str = input("请输入ok支付:")
print(is_pay_str)
