import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
from selenium.webdriver.common.actions.pointer_input import PointerInput
from agent.check_red_point import red_point
from agent.chat_agent import chat_llm
from utils.user_info_mysql import get_msg
from utils.historical_dialogue import get_historical_dialogue


class ChatServer:

    @staticmethod
    def chat():
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

        for i in range(10000):
            # step 1：检测红点
            red_x, red_y = red_point()
            if red_x is None:
                break

            # step 2：下滑页面到红点位置
            window_size = driver.get_window_size()
            start_x = window_size['width'] * 0.5
            start_y = window_size['height'] * 0.8
            driver.swipe(start_x, start_y, red_x, red_y, 500)
            time.sleep(2)

            # Step 3: 点击红点进入聊天对话框
            pointer_input = PointerInput(POINTER_TOUCH, "finger")
            actions = ActionBuilder(driver, mouse=pointer_input)
            actions.pointer_action.move_to_location(50, 100)
            actions.pointer_action.click()
            actions.perform()
            time.sleep(2)

            # step 4：获取用户历史聊天信息
            title_element = driver.find_element(MobileBy.ID, "com.example.app:id/dialog_title")
            history_msg = get_msg(title_element.text)
            get_historical_dialogue(history_msg)
            # step 5：调用聊天agent，智能回复

            # Step 6: 返回私信列表
            driver.back()
            time.sleep(2)
