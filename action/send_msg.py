import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from utils.user_info_mysql import store_user_msg

class SendServer:

    @staticmethod
    def send_msg(person, hello_msg):
        # driver初始化
        # Appium 服务器地址
        APPIUM_SERVER = 'http://localhost:4723/wd/hub'

        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'emulator-5554 ',  # 设备名称（通过 `adb devices` 获取）
            'appPackage': 'com.example.app',  # 应用的包名：抖音apk
            'appActivity': 'com.example.app.MainActivity',  # 应用的启动 Activity
            'automationName': 'UiAutomator2',
            'noReset': True
        }
        # 初始化驱动
        driver = webdriver.Remote(APPIUM_SERVER, desired_caps)

        for i in range(person):
            user_msg = {}
            # step1：下滑页面
            window_size = driver.get_window_size()
            start_x = window_size['width'] * 0.5
            start_y = window_size['height'] * 0.8
            end_y = window_size['height'] * 0.2
            driver.swipe(start_x, start_y, start_x, end_y, 500)
            time.sleep(2)

            # Step 2: 点击用户头像，进入主页
            user_avatar = driver.find_element(MobileBy.ID, 'avatar')
            # 获取、存储用户信息
            user_msg_name = driver.find_element(MobileBy.XPATH,'/name')
            user_msg_id = driver.find_element(MobileBy.XPATH, '/name')
            user_msg["user_msg_name"] = user_msg_name
            user_msg["user_msg_id"] = user_msg_id
            store_user_msg(user_msg)
            user_avatar.click()
            time.sleep(3)

            # Step 3: 点击【私信】按钮，进入私信聊天界面
            chat_button = driver.find_element(MobileBy.ID, 'chat_button')
            chat_button.click()
            time.sleep(3)

            # Step 4: 点击聊天框，输入内容
            chat_input = driver.find_element(MobileBy.ID, 'chat_input')
            chat_input.click()
            chat_input.send_keys(hello_msg)
            time.sleep(2)

            # Step 5: 点击发送
            send_button = driver.find_element(MobileBy.ID, 'send_button')
            send_button.click()
            time.sleep(2)

            # Step 6: 返回个人主页
            driver.back()
            time.sleep(2)

            # Step 7: 返回 feed 流
            driver.back()
            time.sleep(2)
