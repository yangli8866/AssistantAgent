from appium import webdriver
from agent import chat_agent

def chat(driver):
    """
    brush feed steam
    :param driver: webdriver object
    :return: null
    """
    chat_agent.chat_llm()