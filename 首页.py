#coding=utf-8

import os
import unittest,sys,time,re,datetime
from selenium import webdriver
from appium import webdriver
from time import sleep
import sys
from appium.webdriver.common.touch_action import TouchAction


PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__), p))

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['version'] = '7.0'
desired_caps['deviceName'] = 'meizu-m5_note-621QEBPQ2F42W'
desired_caps['appPackage'] = 'com.fcaimao.stock'
desired_caps['appActivity'] = '.ui.activity.SplashActivity'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 获取屏幕大小(1080,1920)
def getSize():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)
# 屏幕向下滑动
def swipeUp(t):
    l = getSize()
    x1 = int(l[0] * 0.5)  # x坐标
    y1 = int(l[1] * 0.75)  # 起始y坐标
    y2 = int(l[1] * 0.25)  # 终点y坐标
    driver.swipe(x1, y1, x1, y2, t)
# 屏幕向上滑动
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
sleep(8)
# 滑动轮播图
swipLeft(1000)
sleep(3)
try:
    driver.find_element_by_id("com.fcaimao.stock:id/bannerViewPager").click()
except BaseException as e:
    print("当前只有一张轮播图")
else:
    print("---轮播图滑动正常---")
sleep(5)
driver.back()
sleep(3)

# 添加自选行情
try:
    driver.find_element_by_id("com.fcaimao.stock:id/add_my_fav").click()
except BaseException as e:
    # 编辑首页自选行情模块
    m=50
    while m>0:
        m-=1
        try:
            driver.find_element_by_id("com.fcaimao.stock:id/add_my_fav").click()
        except BaseException as e:
            def zixuan(t):
                l = getSize()
                x1 = int(l[0] * 0.88)
                y1 = int(l[1] * 0.34)
                x2 = int(l[0] * 0.1)
                driver.swipe(x1, y1, x2, y1, t)
            zixuan(1000)
            sleep(2)
        else:
            break
else:
    pass
sleep(3)
driver.find_element_by_id("com.fcaimao.stock:id/search_button").click()
sleep(3)
driver.back()
driver.find_element_by_id("com.fcaimao.stock:id/search_src_text").send_keys("ag")
sleep(3)
driver.find_element_by_id("com.fcaimao.stock:id/addText").click()
sleep(3)
addText=driver.find_element_by_id("com.fcaimao.stock:id/addText").get_attribute("text")
sleep(3)
try:
    assert(addText == "添加")
except AssertionError as msg:
    driver.back()
    driver.back()
    try:
        driver.find_element_by_name("[南]白银10g").click()
        sleep(3)
    except BaseException as msg:
        print("首页添加白银失败")
    else:
        driver.back()
        print("首页添加白银成功")
else:
    driver.back()
    driver.back()
    try:
        driver.find_element_by_name("[南]白银10g").click()
        sleep(3)
    except BaseException as msg:
        print("首页删除白银成功")
    else:
        driver.back()
        print("首页删除白银失败")

print("---添加删除自选通过---")
sleep(3)

#咨询热线
driver.find_element_by_name("咨询热线").click()
#点击咨询热线跳转到登录页面
try:
    driver.find_element_by_accessibility_id("发送").click()
except BaseException as e:
    driver.find_element_by_id("com.fcaimao.stock:id/account").clear()
    sleep(3)
    driver.back()
    sleep(3)
    driver.find_element_by_id("com.fcaimao.stock:id/account").send_keys("18368481916")
    driver.find_element_by_id("com.fcaimao.stock:id/password").send_keys("123456a")
    driver.find_element_by_id("com.fcaimao.stock:id/login").click()
    sleep(3)
    driver.find_element_by_name("首页").click()
    driver.find_element_by_name("咨询热线").click()
else:
    pass
'''
#点击发送自动跳转登录页面
try:
    driver.find_element_by_id("com.fcaimao.stock:id/account").send_keys("18368481916")
except BaseException as e:
    pass
else:
    driver.find_element_by_id("com.fcaimao.stock:id/password").send_keys("123456a")
    driver.find_element_by_id("com.fcaimao.stock:id/login").click()
'''
sleep(5)
driver.find_element_by_class_name("android.widget.EditText").click()
sleep(3)
driver.find_element_by_class_name("android.widget.EditText").send_keys("hello")
sleep(5)
driver.find_element_by_class_name("android.widget.Button").click()

driver.back()
sleep(3)
driver.find_element_by_name("我的").click()
driver.find_element_by_id("com.fcaimao.stock:id/userIcon").click()
driver.find_element_by_name("退出登录").click()
sleep(3)
driver.find_element_by_name("首页").click()
print("---咨询热线测试通过---")

#新手学堂
driver.find_element_by_name("新手学堂").click()
driver.find_element_by_accessibility_id("第一课：为什么投资贵金属").click()
sleep(5)
swipRight(1000)
sleep(3)
driver.back()
driver.find_element_by_id("com.fcaimao.stock:id/iv_finish").click()
print("---新手学堂测试通过---")
sleep(3)

#点击开户送白银
try:
    driver.find_element_by_name("独家资讯").click()
except BaseException as e:
    driver.find_element_by_name("开户送白银").click()
    sleep(5)
    driver.find_element_by_accessibility_id("请登录").click()
    sleep(3)
    driver.find_element_by_id("com.fcaimao.stock:id/account").send_keys("18368481916")
    driver.find_element_by_id("com.fcaimao.stock:id/password").send_keys("123456a")
    driver.find_element_by_id("com.fcaimao.stock:id/login").click()
    sleep(3)
    el1 = driver.find_element_by_class_name("android.widget.Button").get_attribute("name")
    try:
        assert (el1 == "已参与"), "还未参与活动"
    except AssertionError as msg:
        sleep(3)
        driver.find_element_by_class_name("android.widget.Button").click()
    else:
        print("已参与活动")
    sleep(3)
    driver.back()
    print("---开户送白银测试通过---")
else:
    print("----实战分析测试通过----")


#点击开户申请和财经日历
try:
    driver.find_element_by_name("开户申请").click()
except BaseException as e:
    driver.find_element_by_name("财经日历").click()
else:
    driver.find_element_by_id("com.fcaimao.stock:id/account").send_keys("18368481916")
    driver.find_element_by_id("com.fcaimao.stock:id/password").send_keys("123456a")
    driver.find_element_by_id("com.fcaimao.stock:id/login").click()
    sleep(3)
    driver.find_element_by_name("首页").click()
    driver.find_element_by_name("财经日历").click()
driver.back()
print("---开户申请和财经日历测试通过---")
sleep(3)

# 实时解盘
driver.find_element_by_id("com.fcaimao.stock:id/tab2").click()
sleep(3)
driver.find_element_by_id("com.fcaimao.stock:id/icon").click()
sleep(3)
L1 = driver.find_element_by_id("com.fcaimao.stock:id/likeLayout").is_selected()
driver.find_element_by_id("com.fcaimao.stock:id/likeLayout").click()
sleep(3)
try:
    driver.find_element_by_id("com.fcaimao.stock:id/account").click()
except BaseException as e:
    print("已登录彩猫账号")
else:
    driver.find_element_by_id("com.fcaimao.stock:id/account").send_keys("15558207835")
    driver.find_element_by_id("com.fcaimao.stock:id/password").send_keys("123456a")
    sleep(2)
    driver.find_element_by_id("com.fcaimao.stock:id/login").click()
    sleep(3)
    driver.find_element_by_id("com.fcaimao.stock:id/likeLayout").click()
sleep(3)
L2 = driver.find_element_by_id("com.fcaimao.stock:id/likeLayout").is_selected()
try:
    assert (L1 != L2), "点赞功能测试通过"
except AssertionError as msg:
    pass
else:
    print("点赞功能异常")

sleep(3)
driver.find_element_by_id("com.fcaimao.stock:id/comment").click()
driver.find_element_by_id("com.fcaimao.stock:id/comment").send_keys("good")
sleep(3)
driver.find_element_by_id("com.fcaimao.stock:id/send").click()
sleep(3)
driver.back()

# 24h快讯
sleep(3)
driver.find_element_by_id("com.fcaimao.stock:id/tab1").click()
swipeUp(1000)
sleep(3)
print("----首页测试结束-----")


























