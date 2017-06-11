# -*- coding: utf-8 -*-
import unittest
from time import sleep
from appium import webdriver


class Weibo(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] ='Android'
        desired_caps['deviceName'] ='F8UDU16225002638'
        desired_caps['appPackage'] ='com.sina.weibo'
        desired_caps['appActivity'] ='com.sina.weibo.SplashActivity'
        self.driver=webdriver.Remote("http://127.0.0.1:4722/wd/hub",desired_caps)

#登录
    def test_login(self):
     sleep(10)
     ele=self.driver.find_element_by_id("rltitleSave")
     ele.click()
     sleep(10)
     uname=self.driver.find_element_by_id("etLoginUsername")
     uname.clear()
     uname.send_keys("15910591452")
     pwd = self.driver.find_element_by_id("etPwd")
     pwd.clear()
     pwd.send_keys("lyj123456")
     log = self.driver.find_element_by_id("bnLogin")
     log.click()
     sleep(10)
     e2=self.driver.find_element_by_id("我的资料")
     e2.click()
   #  e2.find_element_by_name("李阳洁531")
     sleep(10)
     e3=self.driver.find_element_by_name("设置")
     e3.click()
     e4 = self.driver.find_element_by_id("accountContent")
     e4.click()
     sleep(10)
     e5 = self.driver.find_element_by_id("exitAccountContent")
     e5.click()
     e6=self.driver.find_element_by_name("确定")
     e6.click()
#发微博
     def test_send(self):
         my = self.driver.find_element_by_id("我的资料")
         my.click()
         sy = self.assertDictContainsSubset("李阳洁531")
         ep = self.driver.find_element_by_id("plus_icon")
         ep.click()
         cii=self.driver.find_element_by_id("composer_item_image")
         cii.click()
         sec=self.driver.find_element_by_id("sv_element_container")
         sec.send_keys("abcd")
         tsav=self.driver.find_element_by_id("titleSave")
         tsav.click()
         sleep(10)

    # 转微博
    def test_review(self):
        my = self.driver.find_element_by_id("我的资料")
        my.click()
        sy=self.assertDictContainsSubset("李阳洁531")
        cwb=self.driver.find_element_by_id("cabWeibo")
        cwb.click()
        sleep(10)
        twc = self.driver.find_element_by_id("tweet_comment")
        twc.click()
        sec = self.driver.find_element_by_id("sv_element_container")
        sec.send_keys("非常好")
        fs= self.driver.find_element_by_name("发送")
        fs.click()
        sleep(10)
        #刷新
        lfl = self.driver.find_element_by_id("ly_feed_like_icon")
        lfl.click()
        tc = self.driver.find_element_by_id("tweet_comment")
        tc.click()
        pl=self.driver.find_element_by_name("评论 1")
        sleep(10)
        fch=self.driver.find_element_by_name("非常好")
        fch.click()
        sc=self.driver.find_element_by_name("删除")
        sc.click()
        qd=self.driver.find_element_by_name("确定")
        qd.click()


#退出微博
    def test_exit(self):
        sleep(10)
        sz=self.driver.find_element_by_name("设置")
        sz.click()
        sleep(10)
        ac=self.driver.find_element_by_id("accountContent")
        ac.click()
        sleep(10)
        eac=self.driver.find_element_by_id("exitAccountContent")
        eac.click()
        qd=self.driver.find_element_by_name("确定")
        qd.click()

    def tearDown(self):
        self.login()
        self.driver.quit();
        print('每一个case运行完都会运行我来清理环境!')

    def login(self,uname,pwd):
         sleep(10)
         ele = self.driver.find_element_by_id("rltitleSave")
         ele.click()
         sleep(10)
         uname = self.driver.find_element_by_id("etLoginUsername")
         uname.clear()
         uname.send_keys(uname)
         pwd = self.driver.find_element_by_id("etPwd")
         pwd.clear()
         pwd.send_keys(pwd)
         log = self.driver.find_element_by_id("bnLogin")
         log.click()
         sleep(10)

    def test_send2(self):
         self.login(self,"15910591452","lyj123456")
         sleep(10)
         my = self.driver.find_element_by_id("我的资料")
         my.click()
         sy = self.assertDictContainsSubset("李阳洁531")
         ep = self.driver.find_element_by_id("plus_icon")
         ep.click()
         cii = self.driver.find_element_by_id("composer_item_image")
         cii.click()
         sec = self.driver.find_element_by_id("sv_element_container")
         sec.send_keys("abcd")
         tsav = self.driver.find_element_by_id("titleSave")
         tsav.click()
         sleep(10)



#执行所以测试代码

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Weibo)
    unittest.TextTestRunner(verbosity=2).run(suite)