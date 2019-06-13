
 
import itchat,time
from itchat.content import TEXT
 

 
itchat.auto_login(enableCmdQR = False)
#获取群
roomslist = itchat.get_chatrooms()
#群名称
itchat.dump_login_status() # 显示所有的群聊信息，默认是返回保存到通讯录中的群聊
myroom=itchat.search_chatrooms(name=u'青果') #群聊名称
gsq=itchat.update_chatroom(myroom[0]['UserName'], detailedMember=True)
 
#保存
with open('gss.txt','a',encoding='utf-8') as f:
    for c in gsq['MemberList']:
        f.write(c['NickName'] + ":" +  c['DisplayName'] + '\n')
        print(c)
        print('正在写入      '+c['NickName']+":",c['DisplayName'])
f.close()