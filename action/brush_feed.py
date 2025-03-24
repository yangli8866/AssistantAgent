from appium import webdriver
from action.chat import chat
from agent.chat_agent import chat_llm
from utils.historical_dialogue import *
from utils.utils import *
from utils.user_info_mysql import *

def brush_feed(driver):
    """
    brush feed steam
    :param driver: webdriver object
    :return: null
    """
    while True:
        try:
            # 检测是否有未读消息
            red_point = driver.find_element_by_xpath("红点")

            while red_point:
                # 有未读消息，进入消息列表
                home_tab = driver.find_element_by_xpath("//android.widget.TextView[@text='消息']")
                home_tab.click()
                # 回复消息
                # 找到未读消息的红点位置
                x,y = find_red_point()
                red_point_position = driver.find_element("坐标xy")
                # 点击红点，进入聊天详情页
                red_point_position.click()
                # todo 页面截图 或者 直接看能不能拿到消息的元素，提取文字，获取聊天内容
                new_dia = get_new_dialogue()
                save_msg(new_dia)
                # 根据用户名获取用户id
                user_name = driver.find_element("获取顶部用户吗")
                user_id = get_msg(user_name)
                # 根据用户id获取用户历史聊天记录
                history_dia = get_historical_dialogue(user_id)
                # 调用聊天大模型，生成智能回复
                msg = chat_llm()
                # 将回复信息发送给对方
                driver.find_element_by_xpath("聊天输入框").send_keys(msg)
                driver.find_element_by_xpath("发送").click()
                # 返回消息列表
                driver.find_element_by_xpath("左上角返回按钮").click()
                # 继续检测消息列表是否有未读消息
                x,y = find_red_point()
                if x > 0:
                    red_point = True
                else:
                    red_point = False

        except Exception:
            break