import unittest
from selenium import webdriver
import time


class MbrTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get('https://account.samsung.com/membership/intro')

    def test_account_signup(self):
        time.sleep(5)
        self.driver.find_element_by_xpath(
            "//*[@id='signup_button']").click()  # .send_keys("Selenium2")#点击登录按钮#############修改处
        time.sleep(3)
        self.driver.find_element_by_xpath(
            "//html/body/div[1]/main/div/div[1]/div[2]/div/div[10]/div/label/span").click()  # 勾选同意全部#############修改处
        time.sleep(3)
        agreen = self.driver.find_element_by_xpath("//html/body/div[1]/main/div/div[2]/div/button[@type='button']")
        #
        self.driver.execute_script("arguments[0].click();", agreen)  # 点击同意按钮

        time.sleep(3)
        self.driver.find_element_by_xpath(
            "//html/body/div[1]/main/div/div[1]/div[2]/a[@href='#']").click()  # 点击使用邮箱进行注册

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)