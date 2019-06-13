# -*- coding: utf-8 -*-
import datetime
import requests
import json
import os.path
#os.path.isfile(fname)
 
class WeChat():
    def __init__(self,openid,name,phone,content):
        self.openid=openid
        self.name=name
        self.phone=phone
        self.data=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.content=content

    def get_token(self):
        if(os.path.exists('access_token.txt')):
            print('文件存在')
        else:
           self.get_tokentxt()

        try:
            with open("access_token.txt","r",encoding="utf-8") as f:
                content=f.read()
                print(content)
                data_dict = json.loads(content) # 根据字符串书写格式，将字符串自动转换成 字典类型(注意json格式都要双引号)
                print (data_dict)

                #data_dict=eval(content)
                print("get_txt",data_dict)
                time=datetime.datetime.strptime(data_dict["time"],'%Y-%m-%d %H:%M:%S')
 
            if (datetime.datetime.now()-time).seconds<7000:
                print("未到两小时，从文件读取")
                return data_dict["access_token"]
            else:
                #超过两小时，重新获取
                print("超过两小时，重新获取")
                payload = {
                     'grant_type': 'client_credential',
                     'appid': '******************',                #公众号appid,按自己实际填写
                     'secret': '*****************',#待按自己实际填写
                     }
                url="https://api.weixin.qq.com/cgi-bin/token?"  
                try:
                    respone=requests.get(url, params=payload, timeout=50)
                    access_token=respone.json().get("access_token")
                    content="{'access_token':"+str(access_token)+",'time':"+str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))+"}"
                    #写入文件
                    with open("access_token.txt","w") as f:
                        f.write(content)
 
                    print("get_token",access_token)
                    return access_token
                except Exception as e:
                    print(e)
        except Exception as e:
            print("get_token,file",e)
 
 
    def post_data(self):
        data={
               "touser":self.openid,
               "template_id":"fAAO3DNYrEktU0ifDVpbRNWTtTzU8_wLhAkVUlLqaLg",#模板ID 青果研发
               # "miniprogram":{
               #   "appid":"wx67afc56d7f6cfac0",  #待使用上线小程序appid
               #   "path":"pages/reserve/mgr/mgr"
               # },
               "data":{
                       "first": {
                           "value":"您好，您已签到成功！",
                           "color":"#173177"
                       },
                       "keyword1":{
                           "value":self.name,
                           "color":"#173177"
                       },
                       "keyword2": {
                           "value":self.data,
                           "color":"#173177"
                       },
                       "keyword3": {
                           "value":self.phone,
                           "color":"#173177"
                       },
                         "keyword4": {
                           "value":self.content,
                           "color":"#173177"
                       },
                       "remark":{
                           "value":"感谢您的使用！",
                           "color":"#173177"
                       }
               }
           }
        json_template=json.dumps(data)
        #self.get_tokentxt()
        access_token=self.get_token()
        #access_token='22_-9huq777k3HFq6yVJsJZbaJMl3CvB0cKyNcbD8iF5CejPCPyDMc77efPtREvMhHQvupNWLGz3bFL78ESMlr12pYhpbYdA6aafP8kVL0nwM1CHnazOGANVDvaXX8pkI5I0_C3QHDyj9rscdp-BDRhAIAMOC'
        print("access_token--",access_token)
        url="https://api.weixin.qq.com/cgi-bin/message/template/send?access_token="+access_token
        try:
            respone=requests.post(url,data=json_template, timeout=50)
            #拿到返回值
            errcode=respone.json().get("errcode")
            print("test--",respone.json())
            if(errcode==0):
                print("模板消息发送成功")
            else:
                print("模板消息发送失败")
        except Exception as e:
            print("test++",e)
 
 
 
