from appium import webdriver
import time

# 配置 Desired Capabilities
desired_caps = {
    'platformName': 'Android',  # 平台名称
    'platformVersion': '12',  # 模拟器的 Android 版本
    'deviceName': '127.0.0.1:16384',  # 模拟器设备名称
    'appPackage': 'com.ss.android.ugc.aweme',  # 抖音的包名
    'appActivity': 'com.ss.android.ugc.aweme.splash.SplashActivity',  # 抖音的启动 Activity
    'noReset': True  # 不清空应用数据
}

# 连接 Appium Server
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 等待应用启动
driver.implicitly_wait(10)

# 示例操作：点击“首页”标签
home_tab = driver.find_element_by_xpath("//android.widget.TextView[@text='首页']")
home_tab.click()
time.sleep(10)

driver.

# 退出会话
driver.quit()