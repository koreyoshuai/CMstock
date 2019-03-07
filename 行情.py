#coding=utf-8

import os
import unittest,sys,time,re,datetime,HTMLTestRunner
from selenium import webdriver
from appium import webdriver
from time import sleep
import sys
from appium.webdriver.common.touch_action import TouchAction


PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__), p))

desired_caps = {}
# 设备系统
desired_caps['platformName'] = 'Android'
# 设备系统版本号
desired_caps['version'] = '6.0'
# 设备名称
desired_caps['deviceName'] = 'meizu-m5_note-621QEBPQ2F42W'
# 应用的包名
desired_caps['appPackage'] = 'com.fcaimao.stock'
desired_caps['appActivity'] = '.ui.activity.SplashActivity'
# 启动app
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
# 点击屏幕
def tapscreen(t):
    l=getSize()
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.8)
    TouchAction(driver).tap(None,x1,y1).release().perform()


# 行情
sleep(5)
driver.find_element_by_name("自选").click()
sleep(3)

driver.find_element_by_id("com.fcaimao.stock:id/addFav").click()
sleep(3)
addtest1=driver.find_element_by_id("com.fcaimao.stock:id/addText").get_attribute("text")
try:
    assert (addtest1 == "添加")
except AssertionError as msg:
    pass
else:
    driver.find_element_by_id("com.fcaimao.stock:id/addText").click()
sleep(3)
driver.back()

driver.find_element_by_name("南交所").click()
sleep(3)
driver.find_element_by_name("[南]白银10g").click()
sleep(5)

# 第一次安装点击引导图
try:
    driver.find_element_by_name("分时").click()
except BaseException as e:
    tapscreen(500)
    sleep(3)
    tapscreen(500)
else:
    pass


# 读取当日行情
el3=driver.find_element_by_id("com.fcaimao.stock:id/openPx").get_attribute("text")
el4=driver.find_element_by_id("com.fcaimao.stock:id/preclosePx").get_attribute("text")
el5=driver.find_element_by_id("com.fcaimao.stock:id/highPx").get_attribute("text")
el6=driver.find_element_by_id("com.fcaimao.stock:id/lowPx").get_attribute("text")
print("该日开盘价"+el3+"昨日收盘价"+el4+"该日最高价"+el5+"该日最低价"+el6)


# 读取当前实时行情
el1=driver.find_element_by_id("com.fcaimao.stock:id/time").get_attribute("text")
sleep(3)
el2=driver.find_element_by_id("com.fcaimao.stock:id/lastPx").get_attribute("text")
print(el1+"时白银实时价格为"+el2)


# 自定义设置标签
sleep(5)
try:
    driver.find_element_by_name("日K").click()
except BaseException as e:
    driver.find_element_by_id("com.fcaimao.stock:id/tabSetting").click()
    sleep(3)
    TouchAction(driver).long_press(driver.find_element_by_name("日K"), 2000).move_to(x=600, y=360).release().perform()
    sleep(3)
    driver.back()
    sleep(3)
    driver.find_element_by_name("日K").click()
else:
    pass
sleep(8)


sleep(3)
try:
    driver.find_element_by_name("5分").click()
except BaseException as e:
    driver.find_element_by_id("com.fcaimao.stock:id/tabSetting").click()
    sleep(3)
    TouchAction(driver).long_press(driver.find_element_by_name("5分"), 2000).move_to(x=600, y=360).release().perform()
    sleep(3)
    driver.back()
    sleep(3)
    driver.find_element_by_name("5分").click()
else:
    pass
sleep(8)
TouchAction(driver).press(x=1026,y=1100).wait(ms=2000).release().perform()
sleep(5)
# 读取该时刻的行情
L1=driver.find_element_by_id("com.fcaimao.stock:id/open").get_attribute("text")
L2=driver.find_element_by_id("com.fcaimao.stock:id/close").get_attribute("text")
L3=driver.find_element_by_id("com.fcaimao.stock:id/high").get_attribute("text")
L4=driver.find_element_by_id("com.fcaimao.stock:id/low").get_attribute("text")
L5=driver.find_element_by_id("com.fcaimao.stock:id/change").get_attribute("text")
print("该分钟开盘价："+L1+"该分钟收盘价："+L2+"该分钟最高价："+L3+"该分钟最低价："+L4+"该分钟涨跌幅："+L5)
sleep(3)
TouchAction(driver).tap(None,x=550,y=1000).perform().release()
sleep(3)

# 滑动行情图表
try:
    swipRight(1000)
    sleep(3)
    swipRight(1000)
except BaseException as e:
    print("滑动1分钟行情图失败")
else:
    print("滑动1分钟行情图行情成功")
driver.find_element_by_name("BOLL").click()
sleep(3)

# 横竖屏切换
driver.find_element_by_id("com.fcaimao.stock:id/fullScreen").click()
sleep(5)
driver.back()

sleep(3)
# 切换副指标
p=50
while p>0:
    p=p-1
    try:
        driver.find_element_by_name("VOL").click()
    except BaseException as e:
        driver.find_element_by_id("com.fcaimao.stock:id/combinedChartBottom").click()
    else:
        break
sleep(3)



# 设置指标参数
driver.find_element_by_name("月K").click()
sleep(5)
driver.find_element_by_id("com.fcaimao.stock:id/setting").click()
sleep(3)
driver.find_element_by_id("com.fcaimao.stock:id/setting").click()
sleep(3)
test1=driver.find_element_by_id("com.fcaimao.stock:id/curValue").get_attribute("text")
sleep(3)
yidong = TouchAction(driver).press(driver.find_element_by_id("com.fcaimao.stock:id/seekBar")).wait(ms=1000).move_to(x=300,y=320).release()
yidong.perform()
sleep(3)
test2=driver.find_element_by_id("com.fcaimao.stock:id/curValue").get_attribute("text")
driver.back()
driver.find_element_by_id("com.fcaimao.stock:id/setting").click()



# 判断是否保存更改的参数
try:
    assert (test1 != test2),"参数更改失败"
except BaseException as e:
    pass
else:
    print("参数更改成功")
sleep(3)


# 恢复默认
driver.find_element_by_name("恢复默认").click()
test3=driver.find_element_by_id("com.fcaimao.stock:id/curValue").get_attribute("text")
try:
    assert (test3 == test1),"恢复默认错误"
except BaseException as e:
    print("恢复默认后显示"+test3+"与初始值不一致")
else:
    print("恢复默认成功")
sleep(3)
driver.back()



# 拖动更换指标顺序
sleep(3)
TouchAction(driver).long_press(x=1010,y=990).move_to(x=1010,y=600).release().perform()
print("更换指标位置成功")
sleep(3)
driver.back()

try:
    driver.find_element_by_id("com.fcaimao.stock:id/combinedChartBottom").click()
    sleep(3)
    driver.find_element_by_id("com.fcaimao.stock:id/combinedChartBottom").click()
except BaseException as e:
    print("点击屏幕切换副指标失败")
else:
    print("点击屏幕切换副指标成功")


# 涨跌提醒
sleep(3)
driver.find_element_by_id("com.fcaimao.stock:id/warnSetting").click()
sleep(3)
try:
    driver.find_element_by_id("com.fcaimao.stock:id/account").send_keys("15558207835")
except BaseException as e:
    print("已登录彩猫账号")
else:
    driver.find_element_by_id("com.fcaimao.stock:id/password").send_keys("123456a")
    sleep(3)
    driver.find_element_by_id("com.fcaimao.stock:id/login").click()
sleep(3)
driver.find_element_by_id("com.fcaimao.stock:id/upTo").clear()
sleep(3)
NewPrice=driver.find_element_by_id("com.fcaimao.stock:id/price").get_attribute("text")
NewPrice1=str(float(NewPrice)+1)
sleep(3)
driver.find_element_by_id("com.fcaimao.stock:id/upTo").send_keys(NewPrice1)
sleep(2)
driver.find_element_by_id("com.fcaimao.stock:id/downTo").send_keys("0")
sleep(2)
driver.find_element_by_id("com.fcaimao.stock:id/switchDownTo").click()
sleep(3)
driver.find_element_by_id("com.fcaimao.stock:id/save").click()


# 闪电买入
try:
    driver.find_element_by_name("闪电买入").click()
except BaseException as e:
    driver.find_element_by_id("com.fcaimao.stock:id/quickSwitchBtn").click()
    sleep(3)
    driver.find_element_by_name("闪电买入").click()
else:
    pass
sleep(3)
try:
    driver.find_element_by_id("com.fcaimao.stock:id/account").send_keys("15558207835")
except BaseException as e:
    try:
        messageTv=driver.find_element_by_id("com.fcaimao.stock:id/messageTv").get_attribute("text")
    except BaseException as e:
        driver.find_element_by_id("com.fcaimao.stock:id/password").send_keys("123456a")
        sleep(5)
        driver.find_element_by_id("com.fcaimao.stock:id/login").click()
    else:
        unlock = TouchAction(driver).press(x=250, y=700).wait(ms=100).move_to(x=0, y=300).wait(ms=100).move_to(
            x=0, y=300).wait(ms=100).move_to(x=300, y=0).wait(ms=100).move_to(x=300, y=0).wait(ms=100).release()
        unlock.perform()    
else:
    driver.find_element_by_id("com.fcaimao.stock:id/password").send_keys("123456a")
    driver.find_element_by_id("com.fcaimao.stock:id/login").click()
    sleep(5)
    unlock = TouchAction(driver).press(x=250, y=700).wait(ms=100).move_to(x=0, y=300).wait(ms=100).move_to(
        x=0, y=300).wait(ms=100).move_to(x=300, y=0).wait(ms=100).move_to(x=300, y=0).wait(ms=100).release()
    unlock.perform()
sleep(3)
max_can_amount=driver.find_element_by_id("com.fcaimao.stock:id/max_can_amount").get_attribute("text")
sleep(3)
try:
    assert (int(max_can_amount[:1])>0)
except AssertionError as msg:
    sleep(3)
    price=driver.find_element_by_id("com.fcaimao.stock:id/price").get_attribute("text")
    print("当前白银市场价格为："+price)
    sleep(3)
    print("当前可用资金不足，无法购买")
    driver.find_element_by_name("取消").click()
else:
    driver.find_element_by_id("com.fcaimao.stock:id/text").send_keys("1")
    sleep(3)
    driver.find_element_by_name("取消").click()


# 切换到普通买卖模式
sleep(3)
driver.find_element_by_id("com.fcaimao.stock:id/quickSwitchBtn").click()
sleep(3)
driver.find_element_by_name("卖出").click()
sleep(3)
tradeType=driver.find_element_by_id("com.fcaimao.stock:id/tradeType").get_attribute("text")
try:
    assert (tradeType[2:4] =="卖出"),"未成功跳转到卖出页面"
except AssertionError as e:
    pass
else:
    print("成功跳转到交易卖出页面")
sleep(3)
driver.find_element_by_name("自选").click()
sleep(3)
driver.find_element_by_name("南交所").click()
sleep(5)
driver.find_element_by_name("[南]白银10g").click()
sleep(5)


# 查看品种介绍
driver.find_element_by_id("com.fcaimao.stock:id/varieties").click()
sleep(5)
driver.back()
driver.back()
sleep(3)


# 编辑
driver.find_element_by_name("编辑").click()
sleep(3)
print("----进入编辑页面----")
# 删除
driver.find_element_by_id("com.fcaimao.stock:id/deleteLayout").click()
sleep(3)
# 置顶
TouchAction(driver).tap(None, 750, 600).perform()
sleep(3)
# 拖动
w = driver.get_window_size()['width']
h = driver.get_window_size()['height']
TouchAction(driver).long_press(x=0.93*w,y=2/5*h).move_to(x=0.93*w,y=0.17*h).release().perform()
sleep(3)
driver.find_element_by_name("完成").click()
sleep(3)
print("----行情测试结束----")
