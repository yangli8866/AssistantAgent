# AssistantAgent

## 主播助理机器人实现思路
- 自动化操作：使用Appium来模拟手机操作，实现滑动、点击、输入等行为。
- 定时任务调度：使用schedule库来实现定时任务调度。
- 自然语言处理：使用qwen、Deepseek模型来生成智能回复。
- 私信管理：通过OCR来读取私信内容，并调用模型判断是否需要回复，模型给给出回复内容

## 项目目录
- main.py入口
- action 操作封装 
    - chat.py 聊天功能：检测消息红点，有红点就进入聊天界面，智能agent进行聊天
    - send_msg.py 发送私信功能，feed流下滑页面，挨个进入发送私信
- agent 智能体封装
    - check_red_point.py  检测消息红点
    - chat_agent.py 调用llm模型，结合RAG，智能对话
- utils 工具类
    - historical_dialogue.py 存储、获取每人历史消息
    - user_info_mysql.py.py 存储、读取 个人信息
    