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
#资讯
sleep(5)
driver.find_element_by_name("资讯").click()
print("-----实时快讯-----")
n1=driver.find_element_by_id("com.fcaimao.stock:id/time").get_attribute("text")
n2=driver.find_element_by_id("com.fcaimao.stock:id/tv_content").get_attribute("text")
print(n1+n2)
sleep(5)
driver.find_element_by_name("财经日历").click()
print("-----财经日历-----")
sleep(3)
n3=driver.find_element_by_id("com.fcaimao.stock:id/event").get_attribute("text")
n4=driver.find_element_by_id("com.fcaimao.stock:id/preValue").get_attribute("text")
n5=driver.find_element_by_id("com.fcaimao.stock:id/forecast").get_attribute("text")
n6=driver.find_element_by_id("com.fcaimao.stock:id/actual").get_attribute("text")
sleep(3)
print(n3+"前值"+n4+"预期"+n5+"实际"+n6)

sleep(3)
driver.find_element_by_name("筛选").click()
sleep(5)
driver.find_element_by_name("美国").click()
driver.find_element_by_name("1星-3星").click()
driver.find_element_by_name("确定").click()
sleep(3)
driver.find_element_by_name("筛选").click()
driver.find_element_by_name("重置").click()
driver.find_element_by_name("确定").click()
sleep(3)
driver.find_element_by_id("com.fcaimao.stock:id/day1Date").click()
sleep(3)
n7=driver.find_element_by_id("com.fcaimao.stock:id/event").get_attribute("text")
n8=driver.find_element_by_id("com.fcaimao.stock:id/preValue").get_attribute("text")
n9=driver.find_element_by_id("com.fcaimao.stock:id/forecast").get_attribute("text")
n10=driver.find_element_by_id("com.fcaimao.stock:id/actual").get_attribute("text")
sleep(3)
print(n7+"前值"+n8+"预期"+n9+"实际"+n10)
sleep(3)
driver.find_element_by_id("com.fcaimao.stock:id/datePicker").click()
driver.find_element_by_id("android:id/next").click()
sleep(3)
driver.find_element_by_name("15").click()
driver.find_element_by_name("确定").click()

sleep(3)
"""
print("-----操作建议----")
driver.find_element_by_name("操作建议").click()
driver.find_element_by_name("AG").click()
driver.swipe(450,1500,450,500)
driver.swipe(450,1500,450,500)
sleep(3)
driver.back()
sleep(3)
m1=driver.find_element_by_id("com.fcaimao.stock:id/wareName").get_attribute("text")
m2=driver.find_element_by_id("com.fcaimao.stock:id/datetime").get_attribute("text")
m3=driver.find_element_by_id("com.fcaimao.stock:id/direction").get_attribute("text")
m4=driver.find_element_by_id("com.fcaimao.stock:id/price").get_attribute("text")
m5=driver.find_element_by_id("com.fcaimao.stock:id/upPrice").get_attribute("text")
m6=driver.find_element_by_id("com.fcaimao.stock:id/downPrice").get_attribute("text")
print(m2+"发布操作建议"+m1+"操作方向："+m3+"操作价格："+m4+m5+m6)
sleep(3)
"""
print("-----实战分析----")
driver.find_element_by_name("实战分析").click()
driver.find_element_by_id("com.fcaimao.stock:id/newsTitle").click()
sleep(5)
swipeUp(1000)
swipeUp(1000)
driver.back()
print("----资讯模块测试结束----")


# 我的模块
sleep(3)
print("----我的模块----")
driver.find_element_by_name("我的").click()
username=driver.find_element_by_id("com.fcaimao.stock:id/username").get_attribute("text")
try:
    assert(username=="请登录"),"已登录账号"
except AssertionError as e:
    pass
else:
    driver.find_element_by_id("com.fcaimao.stock:id/username").click()
    driver.find_element_by_id("com.fcaimao.stock:id/account").send_keys("18368481916")
    driver.find_element_by_id("com.fcaimao.stock:id/password").send_keys("123456a")
    driver.find_element_by_id("com.fcaimao.stock:id/login").click()
    sleep(3)
print("----进入我的账户页面----")
sleep(3)
driver.find_element_by_id("com.fcaimao.stock:id/userIcon").click()
sleep(3)
driver.find_element_by_id("com.fcaimao.stock:id/userIcon").click()
sleep(3)
driver.find_element_by_id("com.fcaimao.stock:id/v_selected").click()
sleep(3)
driver.find_element_by_name("完成").click()
sleep(3)
driver.find_element_by_name("完成").click()
sleep(3)
Status=driver.find_element_by_id("com.fcaimao.stock:id/gestureStatus").get_attribute("text")

try:
    assert(Status == '关闭'),"手势密码已开启"
except AssertionError as msg:
    driver.find_element_by_id("com.fcaimao.stock:id/gestureUnlock").click()
    unlock = TouchAction(driver).press(x=250, y=700).wait(ms=100).move_to(x=0, y=300).wait(ms=100).move_to(
        x=0, y=300).wait(ms=100).move_to(x=300, y=0).wait(ms=100).move_to(x=300, y=0).wait(ms=100).release()
    unlock.perform()
    sleep(3)
else:
    driver.find_element_by_id("com.fcaimao.stock:id/gestureSwitch").click()
    sleep(3)
    driver.find_element_by_id("com.fcaimao.stock:id/password").send_keys("123456a")
    driver.find_element_by_id("com.fcaimao.stock:id/login").click()
    sleep(3)
    driver.find_element_by_id("com.fcaimao.stock:id/gestureUnlock").click()
    sleep(3)
    driver.find_element_by_id("com.fcaimao.stock:id/gestureSwitch").click()
    sleep(3)
    driver.find_element_by_id("com.fcaimao.stock:id/password").send_keys("123456a")
    driver.find_element_by_id("com.fcaimao.stock:id/login").click()
    sleep(3)
    unlock = TouchAction(driver).press(x=250, y=700).wait(ms=100).move_to(x=0, y=300).wait(ms=100).move_to(
        x=0, y=300).wait(ms=100).move_to(x=300, y=0).wait(ms=100).move_to(x=300, y=0).wait(ms=100).release()
    unlock.perform()
    sleep(3)
    unlock = TouchAction(driver).press(x=250, y=700).wait(ms=100).move_to(x=0, y=300).wait(ms=100).move_to(
        x=0, y=300).wait(ms=100).move_to(x=300, y=0).wait(ms=100).move_to(x=300, y=0).wait(ms=100).release()
    unlock.perform()
    sleep(3)
    kaiguan= driver.find_element_by_id("com.fcaimao.stock:id/gestureSwitch").get_attribute("text")
    try:
        assert (kaiguan == "开启"),"手势密码设置失败"
    except AssertionError as e:
        pass
    else:
        print("手势密码设置成功")
sleep(3)
driver.find_element_by_name("修改彩猫密码").click()
driver.back()
driver.back()

print("----进入南交所资产页面----")
driver.find_element_by_id("com.fcaimao.stock:id/southTradeAsset").click()
sleep(3)
driver.find_element_by_name("说明").click()
sleep(3)
driver.back()
sleep(3)
swipeUp(1000)
driver.find_element_by_name("转入/转出资金").click()
driver.back()
driver.back()
sleep(3)

print("----进入交易所信息与变更页面----")
driver.find_element_by_id("com.fcaimao.stock:id/tradeInfoAndModify").click()
sleep(3)
tradeAccount=driver.find_element_by_id("com.fcaimao.stock:id/tradeAccount").get_attribute("text")
print("南交所交易账号："+tradeAccount)
driver.find_element_by_name("修改资金密码").click()
sleep(3)
driver.back()
driver.find_element_by_name("修改交易密码").click()
sleep(3)
driver.back()
driver.back()

print("----进入消息提醒页面----")
driver.find_element_by_id("com.fcaimao.stock:id/messageNotify").click()
sleep(3)
driver.find_element_by_name("交易提醒").click()
sleep(3)
driver.find_element_by_name("查看详情").click()
sleep(3)
try:
    driver.find_element_by_name("委托单").click()
except BaseException as e:
    print("未跳转到历史订单页面")
else:
    print("成功跳转到历史订单页面")
sleep(3)
driver.back()
driver.back()
driver.find_element_by_name("行情提醒").click()
driver.back()
sleep(3)
driver.find_element_by_name("风险提醒").click()
sleep(3)
driver.find_element_by_name("查看详情").click()
sleep(3)
try:
    assert_et_value=driver.find_element_by_name("com.fcaimao.stock:id/assert_et_value").get_attribute("text")
except BaseException as e:
    print("未跳转到持仓页面")
else:
    print("成功跳转到持仓页面")
sleep(3)
driver.find_element_by_name("我的").click()
sleep(3)

print("----进入帮助中心页面----")
driver.find_element_by_name("帮助中心").click()
sleep(3)
driver.find_element_by_accessibility_id("开户常识  ").click()
sleep(3)
driver.find_element_by_accessibility_id("注册指南").click()
sleep(3)
driver.find_element_by_accessibility_id("开户指南").click()
driver.back()
driver.back()
sleep(3)

print("----进入新手学堂页面----")
driver.find_element_by_name("新手学堂").click()
sleep(3)
driver.find_element_by_accessibility_id("第一课：1分钟看懂K线图").click()
sleep(3)
swipeUp(1000)
driver.back()
driver.back()
sleep(3)

print("----进入设置页面----")
driver.find_element_by_name("设置").click()
driver.find_element_by_id("com.fcaimao.stock:id/switch_cjtx").click()
driver.find_element_by_id("com.fcaimao.stock:id/switch_kptx").click()
driver.find_element_by_id("com.fcaimao.stock:id/switch_market").click()
sleep(3)
try:
    switch_market=driver.find_element_by_id("com.fcaimao.stock:id/switch_market").get_attribute("text")
    assert (switch_market == "关闭"),"已开启行情提醒"
except AssertionError as msg:
    pass
else:
    print("已关闭行情提醒")
sleep(3)
driver.find_element_by_id("com.fcaimao.stock:id/switch_night").click()
try:
    switch_market=driver.find_element_by_id("com.fcaimao.stock:id/switch_night").get_attribute("text")
    assert (switch_market == "开启"),"已切换到黑夜模式"
except AssertionError as msg:
    pass
else:
    print("已切换到白天模式")
driver.back()
sleep(3)

print("----进入联系客服页面----")
driver.find_element_by_name("联系客服").click()
swipeUp(1000)
sleep(3)
driver.back()
sleep(3)

print("----进入关于页面----")
swipeUp(1000)
driver.find_element_by_name("关于").click()
sleep(3)
app_version=driver.find_element_by_id("com.fcaimao.stock:id/app_version").get_attribute("text")
print("彩猫贵金属版本号："+app_version)
sleep(3)
driver.find_element_by_id("com.fcaimao.stock:id/disclaimer").click()
sleep(3)
driver.back()
driver.back()
sleep(3)
print("----我的模块测试结束----")