'''
    测试报告生成
'''
#导包
import unittest
from frame.case.TestTPshopLogin import TestLogin
import time
#创建测试套件对象，组织被执行的测试函数
from frame.tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()
#suite.addTest(类名（函数名）)
suite.addTest(unittest.makeSuite(TestLogin))
#执行测试套件，借助于 HTmltestrunner  将结果写出为测试报告文件（使用文件流）
#打开文件流---》创建HTmltestrunner对象 ---》执行suite
with open("./report/"+time.strftime("%Y-%m-%d-%H-%M-%S")+".html","wb") as f:
    runner=HTMLTestRunner(f,title="我的测试报告",description="TPshop Login v1.0")
    runner.run(suite)