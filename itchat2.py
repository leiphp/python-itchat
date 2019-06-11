import itchat
import time


@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def reply_msg(msg):
    print("收到一条群["+msg['User']['NickName']+"]信息：", msg['ActualNickName'], msg['Content'])
    userinfo = itchat.search_friends(userName='@10d812d1e2fdaa690497c05b02e9b3fd4d003bf58f6156f9b510cca3c9be43de')
    print(userinfo)
    


def after_login():
    # 获得完整的群聊列表
    print("完整的群聊列表如下：")
    print(itchat.get_chatrooms())
    # 查找特定群聊
    time.sleep(10)
    # 通过群聊名查找
    chat_rooms = itchat.search_chatrooms(name='小22妹真年轻哦')
    print("通过群名查找的群聊列表如下：")
    print(chat_rooms)
    if len(chat_rooms) > 0:
        itchat.send_msg('测试', chat_rooms[0]['UserName'])



if __name__ == '__main__':
    itchat.auto_login(loginCallback=after_login)
    itchat.run()
