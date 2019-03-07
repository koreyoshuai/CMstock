#coding=utf-8

import os
from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction


PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__), p))

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['version'] = '6.0'
desired_caps['deviceName'] = 'meizu-m5_note-621QEBPQ2F42W'
desired_caps['appPackage'] = 'com.fcaimao.stock'
desired_caps['appActivity'] = '.ui.activity.SplashActivity'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 获取屏幕大小(1080,1920)
def getSize():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)
# 屏幕向上滑动
def swipeUp(t):
    l = getSize()
    x1 = int(l[0] * 0.5)  # x坐标
    y1 = int(l[1] * 0.75)  # 起始y坐标
    y2 = int(l[1] * 0.25)  # 终点y坐标
    driver.swipe(x1, y1, x1, y2, t)
# 屏幕向下滑动
def swipeDown(t):
    l = getSize()
    x1 = int(l[0] * 0.5)  # x坐标
    y1 = int(l[1] * 0.25)  # 起始y坐标
    y2 = int(l[1] * 0.75)  # 终点y坐标
    driver.swipe(x1, y1, x1, y2, t)
# 屏幕向左滑动
def swipLeft(t):
    l = getSize()
    x1 = int(l[0] * 0.75)
    y1 = int(l[1] * 0.5)
    x2 = int(l[0] * 0.05)
    driver.swipe(x1, y1,x2, y1, t)
# 屏幕向右滑动
def swipRight(t):
    l = getSize()
    x1 = int(l[0] * 0.05)
    y1 = int(l[1] * 0.5)
    x2 = int(l[0] * 0.75)
    driver.swipe(x1, y1, x2, y1, t)
# 彩猫登录及南交所登录
sleep(8)
driver.find_element_by_name("交易").click()
sleep(5)
# 判断是否登录彩猫账号
try:
    caimao_account = driver.find_element_by_id("com.fcaimao.stock:id/account").is_enabled()
except BaseException as e:
    print(e)
else:
    try:
        assert (caimao_account == True), "无法执行，可能由于彩猫账号已经登录"
    except AssertionError as msg:
        pass
    else:
        driver.find_element_by_id("com.fcaimao.stock:id/account").send_keys("18368481916")
        driver.find_element_by_id("com.fcaimao.stock:id/password").send_keys("123456a")
        driver.find_element_by_id("com.fcaimao.stock:id/login").click()
    sleep(5)
# 判断是手势密码登录还是账号密码登录
try:
    el = driver.find_element_by_id("com.fcaimao.stock:id/messageTv").get_attribute("text")
    assert(el == "请输入手势密码")
except BaseException as e:
    sleep(3)
    driver.find_element_by_id("com.fcaimao.stock:id/password").send_keys("123456a")
    driver.find_element_by_id("com.fcaimao.stock:id/login").click()
    print("已输入南交所登录密码")
else:
    # 手势密码L型
    unlock = TouchAction(driver).press(x=250, y=700).wait(ms=100).move_to(x=0, y=300).wait(ms=100).move_to(
    x=0, y=300).wait(ms=100).move_to(x=300, y=0).wait(ms=100).move_to(x=300, y=0).wait(ms=100).release()
    unlock.perform()
    print("已输入手势密码")
sleep(3)
# 是否成功进入南交所
try:
    driver.find_element_by_name("卖出").click()
except BaseException as e:
    print("南交所登录失败")
else:
    print("已成功进入交易")
sleep(5)
print("------交易模块登录测试结束------")
sleep(3)

# 交易
sleep(5)
driver.find_element_by_name("持仓").click()
sleep(3)
# 可用资金
kyzj=driver.find_element_by_id("com.fcaimao.stock:id/available_fund").get_attribute("text")
print("当前账户可用资金为："+kyzj)
sleep(3)

# 卖出页面
print("---卖出页面----")
driver.find_element_by_name("卖出").click()
sleep(3)
driver.find_element_by_id("com.fcaimao.stock:id/productName").click()
driver.find_element_by_name("[南]氧化铕").click()
sleep(3)

# 最大可卖出数量
max=driver.find_element_by_id("com.fcaimao.stock:id/maxAmountCanDeal").get_attribute("text")
print("当前氧化铕最大可卖量："+max)
sleep(3)
driver.find_element_by_id("com.fcaimao.stock:id/tradeType").click()
driver.find_element_by_name("市价快速卖出").click()
sleep(3)

# 判断参考市价显示是否正确
currentPrice=driver.find_element_by_id("com.fcaimao.stock:id/currentPrice").get_attribute("text")
refPrice=driver.find_element_by_id("com.fcaimao.stock:id/refPrice").get_attribute("text")
try:
    assert (currentPrice==refPrice),"参考市价显示错误：与实时行情不一致"
except AssertionError as msg:
    pass
else:
    print("参考市价显示正确")
sleep(5)
driver.find_element_by_id("com.fcaimao.stock:id/tradeType").click()
driver.find_element_by_name("限价卖出").click()
sleep(5)

driver.find_element_by_name("卖5").click()
sleep(3)
driver.find_element_by_id("com.fcaimao.stock:id/add").click()
driver.find_element_by_name("1/3").click()
driver.find_element_by_name("卖出").click()
sleep(3)
try:
    # 委托价格
    trade_price = driver.find_element_by_id("com.fcaimao.stock:id/trade_price").get_attribute("text")
    # 委托数量
    trade_amout = driver.find_element_by_id("com.fcaimao.stock:id/trade_amout").get_attribute("text")
    driver.find_element_by_name("确认卖出").click()
    sleep(5)
except BaseException as e:
    print("卖出失败")
else:
    #条件单显示的委托数量
    entrustAmount=driver.find_element_by_id("com.fcaimao.stock:id/entrustAmount").get_attribute("text")
    #条件单显示的委托价
    order_wtj=driver.find_element_by_id("com.fcaimao.stock:id/order_wtj").get_attribute("text")
    sleep(3)

    try:
        assert(entrustAmount[:1]==trade_amout),"条件单委托数量与输入不一致"

    except BaseException as e:
        print(e)
    else:
        print("条件单委托数量显示正确")
    sleep(3)
    try:
        assert(order_wtj==trade_price),"条件单委托价格与输入不一致"
    except BaseException as e:
        print(e)
    else:
        print("条件单委托价格显示正确")
    sleep(3)
    driver.find_element_by_name("撤销").click()
    sleep(5)
    status1=driver.find_element_by_id("com.fcaimao.stock:id/status").get_attribute("text")
    try:
        assert(status1=="撤销"),"撤销条件单失败"
    except AssertionError as msg:
        pass
    else:
        print("撤销条件单成功")
sleep(3)

# 买入页面
print("---买入页面----")
driver.find_element_by_name("买入").click()
sleep(3)
driver.find_element_by_id("com.fcaimao.stock:id/tradeType").click()
sleep(3)
driver.find_element_by_name("限价买入").click()
sleep(3)
driver.find_element_by_name("买1").click()
sleep(3)
driver.find_element_by_id("com.fcaimao.stock:id/sub").click()
sleep(3)
driver.find_element_by_name("买入").click()
sleep(3)
try:
    # 委托价格
    trade_price1 = driver.find_element_by_id("com.fcaimao.stock:id/trade_price").get_attribute("text")
    # 委托数量
    trade_amout1 = driver.find_element_by_id("com.fcaimao.stock:id/trade_amout").get_attribute("text")
    # 预扣保证金
    bail_money = driver.find_element_by_id("com.fcaimao.stock:id/bail_money").get_attribute("text")
    driver.find_element_by_name("确认买入").click()
    sleep(5)
except BaseException as e:
    print("买入失败")
else:
    # 委托单显示的委托数量
    entrustAmount1=driver.find_element_by_id("com.fcaimao.stock:id/entrustAmount").get_attribute("text")
    # 委托单显示的委托价
    order_wtj1=driver.find_element_by_id("com.fcaimao.stock:id/order_wtj").get_attribute("text")
    # 委托时间
    time1=driver.find_element_by_id("com.fcaimao.stock:id/order_time").get_attribute("text")
    print("委托时间为"+time1)
    # 委托单显示预扣保证金
    order_ykbzj=driver.find_element_by_id("com.fcaimao.stock:id/order_ykbzj").get_attribute("text")
    sleep(3)

    try:
        assert (bail_money == order_ykbzj), "预扣保证金与显示的不一致"
    except AssertionError as e:
        print(e)
    else:
        print("预扣保证金显示正确")
    sleep(3)

    try:
        assert (entrustAmount1[:1] == trade_amout1), "委托单委托数量与输入不一致"
    except AssertionError as e:
        print(e)
    else:
        print("委托单委托数量显示正确")
    sleep(3)

    try:
        assert (order_wtj1 == trade_price1), "委托单委托价格与输入不一致"
    except BaseException as e:
        print(e)
    else:
        print("委托单委托价格显示正确")
    sleep(3)
    driver.find_element_by_name("撤销").click()
    sleep(5)
    status1=driver.find_element_by_id("com.fcaimao.stock:id/status").get_attribute("text")

    try:
        assert(status1=="撤销"),"撤销条件单失败"
    except AssertionError as msg:
        pass
    else:
        print("撤销条件单成功")
sleep(3)

# 持仓页面
driver.find_element_by_name("持仓").click()
#风险率
try:
    fxl=driver.find_element_by_id("com.fcaimao.stock:id/tv_risk_rate").get_attribute("text")
except BaseException as e:
    print("该账户此时风险率未超出80%")
else:
    print("此账号"+fxl)
sleep(3)
print("---止盈止损页面----")
try:
    driver.find_element_by_name("止盈止损").click()
    sleep(5)
except BaseException as e:
    print("当前无持仓")
else:
    driver.find_element_by_name("1/2").click()
    sleep(3)
    driver.find_element_by_id("com.fcaimao.stock:id/add").click()
    driver.find_element_by_id("com.fcaimao.stock:id/sub").click()
    driver.find_element_by_id("com.fcaimao.stock:id/cb_zs").click()
    sleep(3)
    driver.find_element_by_name("提醒我").click()
    sleep(3)
    #止盈触发价
    zyjg=driver.find_element_by_id("com.fcaimao.stock:id/tv_value_zyjg").get_attribute("text")
    #较当前涨
    zy_desc=driver.find_element_by_id("com.fcaimao.stock:id/tv_value_zyjg_desc").get_attribute("text")
    driver.find_element_by_name("达到以上条件时提醒我").click()
    print("当止盈触发到达"+zyjg+"较当前涨"+zy_desc+"时提醒我")
    sleep(5)
    driver.find_element_by_id("com.fcaimao.stock:id/cb_zs").click()
    driver.find_element_by_id("com.fcaimao.stock:id/sub").click()
    driver.find_element_by_id("com.fcaimao.stock:id/sub").click()
    driver.find_element_by_name("确定设置").click()
    sleep(3)
    #止盈止损确认框数量
    count=driver.find_element_by_id("com.fcaimao.stock:id/tv_value_count").get_attribute("text")
    #止损触发价
    zsjg=driver.find_element_by_id("com.fcaimao.stock:id/tv_value_zsjg").get_attribute("text")
    zs_desc=driver.find_element_by_id("com.fcaimao.stock:id/tv_value_zsjg_desc").get_attribute("text")
    sleep(3)
    driver.find_element_by_name("提交").click()
    sleep(5)
    #订单委托数量
    wtl=driver.find_element_by_id("com.fcaimao.stock:id/tv_value_wtl").get_attribute("text")
    #订单止盈价
    ddzyjg=driver.find_element_by_id("com.fcaimao.stock:id/tv_value_zyj").get_attribute("text")
    #订单止损价
    ddzsjg=driver.find_element_by_id("com.fcaimao.stock:id/tv_value_zsj").get_attribute("text")
    #订单状态
    wtzt=driver.find_element_by_id("com.fcaimao.stock:id/tv_value_wtzt").get_attribute("text")
    sleep(3)
    #订单委托时间
    wtsj=driver.find_element_by_id("com.fcaimao.stock:id/tv_value_wtsj").get_attribute("text")
    print("此止盈止损订单委托时间："+wtsj+"订单状态："+wtzt)
    sleep(5)
    try:
        assert (zyjg == ddzyjg), "止盈价格与显示的不一致"
    except AssertionError as e:
        print(e)
    else:
        print("止盈价格显示正确")
    sleep(3)
    try:
        assert (zsjg == ddzsjg), "止损价格与显示的不一致"
    except AssertionError as e:
        print(e)
    else:
        print("止损价格显示正确")
    sleep(3)
    try:
        assert (wtl[:1] ==count ), "止盈止损委托数量与输入不一致"
    except AssertionError as e:
        print(e)
    else:
        print("止盈止损委托数量显示正确")
    sleep(3)
    driver.find_element_by_name("撤单").click()
    sleep(5)
    driver.find_element_by_name("提交").click()
    sleep(5)
    try:
        driver.find_element_by_name("查看").click()
    except BaseException as e:
        print("撤单失败")
    else:
        sleep(3)
        cdsj=driver.find_element_by_id("com.fcaimao.stock:id/tv_value_cdsj").get_attribute("text")
        sleep(3)
        print("撤单时间:"+cdsj)
        sleep(3)
        driver.find_element_by_name("确定").click()
        driver.back()
        sleep(3)

# 查看历史成交和委托单
print("---历史成交和委托单---")
driver.find_element_by_id("com.fcaimao.stock:id/btn_orders_deal").click()
sleep(3)
try:
    pz=driver.find_element_by_id("com.fcaimao.stock:id/tv_ware").get_attribute("text")
except BaseException as e:
    print("暂无历史成交单记录")
else:
    cjjg=driver.find_element_by_id("com.fcaimao.stock:id/tv_num").get_attribute("text")
    sj=driver.find_element_by_id("com.fcaimao.stock:id/tv_time").get_attribute("text")
    cjsl=driver.find_element_by_id("com.fcaimao.stock:id/tv_cost_num").get_attribute("text")
    print("最近一条成交记录："+pz+"在"+sj+"以"+cjjg+"成交了"+cjsl+"手")
sleep(3)
driver.find_element_by_name("委托单").click()
sleep(3)
try:
    cjzt=driver.find_element_by_id("com.fcaimao.stock:id/tv_status").get_attribute("text")
except BaseException as e:
    print("暂无委托单成交记录")
else:
    print("最近一条委托单状态："+cjzt)
sleep(3)
driver.back()
sleep(3)

# 南交所资产页面
driver.find_element_by_id("com.fcaimao.stock:id/layout_right").click()
sleep(5)
# 持仓保证金
ccbzj=driver.find_element_by_id("com.fcaimao.stock:id/positionMargin").get_attribute("text")
# 持仓盈亏
ccyk=driver.find_element_by_id("com.fcaimao.stock:id/positionProfitAndLoss").get_attribute("text")
# 预扣保证金
ykbzj=driver.find_element_by_id("com.fcaimao.stock:id/withholdingMargin").get_attribute("text")
# 可用资金
kyzj=driver.find_element_by_id("com.fcaimao.stock:id/enableMoney").get_attribute("text")
sleep(3)
print("----南交所资产显示-----")
print("持仓保证金："+ccbzj)
print("持仓盈亏："+ccyk)
print("预扣保证金："+ykbzj)
print("可用资金："+kyzj)
sleep(3)


# 融货融资页面
print("---融资融货费----")
sleep(3)
driver.find_element_by_name("更多").click()
driver.find_element_by_name("融资费").click()
sleep(3)
rzf=driver.find_element_by_id("com.fcaimao.stock:id/totalRzOrRhFee").get_attribute("text")
print("融资费合计"+rzf)
driver.find_element_by_name("融货费").click()
sleep(3)
rhf=driver.find_element_by_id("com.fcaimao.stock:id/totalRzOrRhFee").get_attribute("text")
print("融货费合计"+rhf)
driver.back()
driver.back()
sleep(3)

# 转账页面
print("----转账页面-----")
print("----转入页面-----")
driver.find_element_by_name("转账").click()
sleep(3)
bank=driver.find_element_by_id("com.fcaimao.stock:id/bank_name").get_attribute("text")
print("绑定的银行为："+bank)
bank_desc=driver.find_element_by_id("com.fcaimao.stock:id/bank_desc").getAttribute("text");
print("绑定的银行为："+bank_desc)
sleep(3)
driver.find_element_by_id("com.fcaimao.stock:id/et_money").send_keys("1")
sleep(3)
driver.back()
sleep(3)
driver.find_element_by_name("确定转入").click()
try:
    driver.find_element_by_id("com.fcaimao.stock:id/psw_input").send_keys("111111")
except BaseException as e:
    try:
        driver.find_element_by_id("com.fcaimao.stock:id/requestCheckCode").click()
    except BaseException as e1:
        print("转账有误!!!!")
    else:
        print("此卡为浙商渠道")
else:
    sleep(2)
    driver.find_element_by_name("确定").click()
    print("此卡为易宝渠道")
sleep(5)

print("----转出页面-----")
driver.find_element_by_name("转出").click()
sleep(3)

# 可转余额
et_money=driver.find_element_by_id("com.fcaimao.stock:id/et_money").get_attribute("text")
print("可转余额"+et_money)
try:
    assert (int(et_money[-1]) > 1), "可转余额不足"
except AssertionError as msg:
    driver.find_element_by_name("为什么我有钱却转出不了？").click()
    sleep(3)
    driver.back()
else:
    driver.find_element_by_id("com.fcaimao.stock:id/et_money").send_keys("1")
    driver.back()
    driver.find_element_by_name("确定转出").click()
    driver.find_element_by_id("com.fcaimao.stock:id/psw_input").send_keys("123457")
sleep(3)

print("----转账查询页面-----")
driver.find_element_by_name("转账查询").click()
sleep(3)
driver.find_element_by_name("查询历史转账记录").click()
sleep(5)
driver.find_element_by_id("com.fcaimao.stock:id/tv_query_value").click()
sleep(3)
swipeUp(1000)
driver.find_element_by_name("确定").click()
sleep(3)
try:
    item_time=driver.find_element_by_id("com.fcaimao.stock:id/item_time").get_attribute("text")
except BaseException as e:
    pass
else:
    item_type=driver.find_element_by_id("com.fcaimao.stock:id/item_type").get_attribute("text")
    item_money=driver.find_element_by_id("com.fcaimao.stock:id/item_money").get_attribute("text")
    item_status=driver.find_element_by_id("com.fcaimao.stock:id/item_status").get_attribute("text")
    print("最近一条转账时间"+item_time+item_type+item_money+item_status)
sleep(3)
driver.back()
driver.back()
print("-----交易模块测试结束-------")



