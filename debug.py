#coding=utf-8

import os
import unittest,sys,time,re,datetime,HTMLTestRunner
from selenium import webdriver
from appium import webdriver
from time import sleep
import sys
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains

PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__), p))


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['version'] = '6.0'
desired_caps['deviceName'] = 'meizu-m5_note-621QEBPQ2F42W'
desired_caps['appPackage'] = 'com.fcaimao.stock'
desired_caps['appActivity'] = '.ui.activity.SplashActivity'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 获得机器屏幕大小x,y(1080,1920)
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

def tapscreen(t):
    l=getSize()
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.8)
    TouchAction(driver).tap(None,x1,y1).release().perform()

sleep(3)
driver.find_element_by_name("自选").click()
sleep(3)
driver.find_element_by_name("南交所").click()
sleep(3)
driver.find_element_by_name("[南]白银10g").click()
sleep(3)
driver.find_element_by_id("com.fcaimao.stock:id/setting").click()
sleep(3)
TouchAction(driver).long_press(x=1010,y=990).move_to(x=1010,y=600).release().perform()
print("更换指标位置成功")
sleep(3)
driver.back()

