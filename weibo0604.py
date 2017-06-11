# -*- coding: utf-8 -*-
import unittest
from time import sleep
from appium import webdriver


class weibo0604(unittest.TestCase):
    #预置条件
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] ='Android'
        desired_caps['deviceName'] ='F8UDU16225002638'
        desired_caps['appPackage'] ='com.sina.weibo'
        desired_caps['appActivity'] ='com.sina.weibo.SplashActivity'
        desired_caps['unicodeKeyboard'] ='true'
        desired_caps['resetKeyboard'] ='true'
        self.driver=webdriver.Remote("http://127.0.0.1:4722/wd/hub",desired_caps)

        #self.login("15910591452", "lyj123456")
    #清理环境
    def tearDown(self):
        #self.driver.quit();
        #self.exit()
        print('每一个case运行完都会运行我来清理环境!')
    def test_send(self):
        #self.login("15910591452", "lyj123456")
        self.send("1234567")
        # self.review("1234567890")

    #发微博
    def send(self,content):
        sleep(10)
        self.driver.find_element_by_id("我的资料").click()
        self.driver.find_element_by_id("plus_icon").click()
        self.driver.find_element_by_id("composer_item_image").click()
        self.driver.find_element_by_id("sv_element_container").send_keys(content)
        self.driver.find_element_by_id("titleSave").click()
        sleep(10)
        #验证是否发布微博成功/
        self.driver.find_element_by_id("cabWeibo").click()
        el=self.driver.find_elements_by_xpath(xpath="//android.widget.TextView")
        #el=self.driver.find_elements_by_xpath("//android.widget.TextView")
        self.assertIn(u"1234567",el[4].text)

        #self.review()
        #self.exit()

    def login(self, username, password):
        sleep(10)
        ele = self.driver.find_element_by_id("rltitleSave")
        ele.click()
        sleep(10)
        uname = self.driver.find_element_by_id("etLoginUsername")
        uname.clear()
        uname.send_keys(username)
        pwd = self.driver.find_element_by_id("etPwd")
        pwd.clear()
        pwd.send_keys(password)
        log = self.driver.find_element_by_id("bnLogin")
        log.click()
        sleep(10)
        my_name = self.driver.find_element_by_accessibility_id("我的资料")
        my_name.click()
        nice_name=self.driver.find_element_by_name("李阳洁531").text
        self.assertEqual(u"李阳洁531",nice_name,msg="eorr!")

        # 退出微博!
    def exit(self):
        sleep(10)
        mybutton=self.element_is_present("content","我的资料")
        while mybutton is False:
            self.driver.press_keycode(4)
            mybutton = self.element_is_present("content", "我的资料")
        sz = self.driver.find_element_by_name("设置")
        sz.click()
        sleep(10)
        ac = self.driver.find_element_by_id("accountContent")
        ac.click()
        sleep(10)
        eac = self.driver.find_element_by_id("exitAccountContent")
        eac.click()
        qd = self.driver.find_element_by_name("确定")
        qd.click()

        # 评论
    def review(self,content):
        my = self.driver.find_element_by_accessibility_id("我的资料")
        my.click()
        #sy = self.assertDictContainsSubset("李阳洁531")
        cwb = self.driver.find_element_by_id("cabWeibo")
        cwb.click()
        sleep(10)
        twc = self.driver.find_element_by_id("tweet_comment")
        twc.click()
        sec = self.driver.find_element_by_id("sv_element_container")
        sec.send_keys(content)
        fs = self.driver.find_element_by_name("发送")
        fs.click()
        sleep(10)
        # 刷新
        self.driver.swipe(360,838,360,1354)
        lfl = self.driver.find_element_by_id("ly_feed_like_icon")
        lfl.click()
        tc = self.driver.find_element_by_id("tweet_comment")
        tc.click()
        pl = self.driver.find_element_by_name("评论 1")
        sleep(10)
        fch = self.driver.find_element_by_name("1234567890")
        fch.click()
        sc = self.driver.find_element_by_name("删除")
        sc.click()
        qd = self.driver.find_element_by_name("确定")
        qd.click()

    def element_is_present(self,by,locator):
        try:
            if by=="id":
                self.driver.find_element_by_id(locator)
                return True
            elif  by=="name":
                self.driver.find_element_by_name(locator)
                return True
            elif by=="content":
                self.driver.find_element_by_accessibility_id(locator)
                return True
        except:
            return False
    # 执行所以测试代码
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(weibo0604)
    unittest.TextTestRunner(verbosity=2).run(suite)