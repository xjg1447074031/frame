'''
 设计case 实现
'''
# 导包
import json
import unittest
from parameterized import parameterized
import requests

from frame import app
from frame.api.LoginAPI import Login
def read_json():
    # 1.创建一个空列表
    data=[]
    # 打开文件流并解析,解析得到的数据添加进空列表
    with open(app.PRO_PATH+"/data/login_data.json","r",encoding="utf-8") as f:
    #读文件流
        # my_file=json.load(f)
        # print("加载后整个文件流信息",my_file)
        # vs=my_file.values()
        # print("json的值：",vs)
        for v in json.load(f).values():
            username= v.get("username")
            password= v.get("password")
            verify_code= v.get("verify_code")
            msg= v.get("msg")
            status= v.get("status")
            ele=(username,password,verify_code,msg,status)
            data.append(ele)
    return data
   # return [("18231327985","123456789","登录成功",8888,1)]
#创建测试类
class TestLogin(unittest.TestCase):
    #3初始化函数
    def setUp(self):
        self.session=requests.Session() #创建session对象
        self.login_obj = Login()
    #资源卸载函数
    def tearDown(self):
        self.session.close()
    #5.测试函数
    #5.1测试验证码
    def test_get_verify_code(self):
        #1.请求业务（当前实现：需要将该业务单独封装_封装进api包）
        #基本实现思想
        #封装：api 包下创建一个Python文件，Python文件中创建 class 封装一个请求函数，返回请求结果
        #调用： 创建api 包下的class 的对象，然后对象.函数（）调用
        #关键点：session的传递
        response = self.login_obj.get_verify_code(self.session)#传参
        # print("验证码接口响应的状态码",response.status_code)
        # print("验证码接口的响应体",response.content)
        # 2.断言业务
        #断言响应头的Content-type
        ct=response.headers.get("Content-Type")
        self.assertIn("image",ct)
        #print(ct)
    #测试登录
    #登录与验证码获取比较
    #相同点：都有请求业务与断言（要调用api实现）
    #不同点：登录需要使用到参数化
    #实现顺序：参数化--》请求--》断言
    @parameterized.expand(read_json())
    def test_login(self,username,password,verify_code,msg,status):
        print('-'*100)
        print(username,password,verify_code,msg,status)
        #请求业务
        #获取验证码
        response1=self.login_obj.get_verify_code(self.session)
        response2=self.login_obj.login(self.session,username,password,verify_code)
        print(response2.json())

        #断言业务
        #需要断言的是  响应中自定义状态码 与响应体的提示信息
        #获取实际结果
        status_response=response2.json().get("status")
        msg_response=response2.json().get("msg")
        #预期结果：参数化导入的msg 与status
        self.assertIn(msg,msg_response)
        self.assertEqual(status,status_response)
