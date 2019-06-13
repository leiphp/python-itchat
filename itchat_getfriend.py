import itchat
import time


@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def reply_msg(msg):
    print("收到一条群["+msg['User']['NickName']+"]信息：", msg['ActualNickName'], msg['Content'])
    nickname = msg['ActualNickName']
    result = itchat.search_friends(name=nickname)
    print(result)
	#print(msg['User'])
    


def after_login():
    chatroomUserName = '@1234567'
    friend = itchat.get_friends()[2]
    print(friend)
    print('*****************************************************')
    r = itchat.add_member_into_chatroom(chatroomUserName, [friend])
    print(r)
    if r['BaseResponse']['ErrMsg'] == '':
	    print(r['MemberList'])
        #status = r['MemberList'][0]['MemberStatus']
        #itchat.delete_member_from_chatroom(chatroom['UserName'], [friend])
        #return { 3: u'该好友已经将你加入黑名单。',4: u'该好友已经将你删除。', }.get(status,u'该好友仍旧与你是好友关系。')



if __name__ == '__main__':
    itchat.auto_login(loginCallback=after_login)
    itchat.run()
