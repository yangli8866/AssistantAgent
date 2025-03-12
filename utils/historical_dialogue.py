from utils.user_info_mysql import conn_mysql
from utils.user_info_mysql import save_msg
from utils.user_info_mysql import get_msg


def save_historical_dialogue(user_id, msg):
    conn_mysql()
    sql = ""

    pass


def get_historical_dialogue(user_id):
    conn_mysql()
    get_msg()
    return "historical_dialogue"
