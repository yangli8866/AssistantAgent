from action.chat import ChatServer
from action.send_msg import SendServer

if __name__=="__main__":
    # 给person个人发私信
    person = 10000
    hello_msg = "你好，有兴趣加入我们**公司吗？"
    SendServer.send_msg(person,hello_msg)

    ChatServer.chat()
