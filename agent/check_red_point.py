def red_point():
    # 红点识别，获取红点的位置
    # 返回页面最上面的一个红点的位置
    # 如果当前页面没有红点，则下滑页面，直至页面下滑到底部
    red_x = 120
    red_y = 50
    if red_x is None:
        return None
    return red_x, red_y
