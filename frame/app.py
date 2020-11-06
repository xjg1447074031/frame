'''
    测试框架搭建 ：分包
    核心 api+case+data
        api：封装 request 相关实现 ，直接访问 服务器（请求业务）
        case：封装 unittest 相关实现，断言业务 +参数化
        data：封装测试数据
        三者关系 ：case 是核心
        case 的测试函数中需要调用api  的请求业务 ，且需要通过参数化读取 data 中的数据
    报告： report +tools+run_suite.py
        report ：保存最终生成的测试报告
        tools：工具
        run_suite.py ：组织测试套件，并调用 tools 生成写出测试报告
    配置： app.py
    app.py ：封装接口的资源路径前缀
            封装项目绝对路径的获取
            封装日志输出的配置信息
    程序中资源路径问题补充：
        场景：程序中经常会和磁盘文件交互，交互前提，先能定位磁盘文件，定位磁盘文件时，如何设计路径
        实现方式1：使用写死的绝对路径 （优先级低，不建议使用，因为存在移植性问题）
        实现方式2：使用相对路径（不建议使用，当程序中出现“代码包含”，相对路径存在安全隐患）
        实现方式3：动态获取绝对路径（建议使用，即不存在移植性问题，又不存在安全隐患）
        优先级： 动态》相对路径》绝对路径

        Python中动态获取项目路径演示
'''
import os
import logging
import logging.handlers
BASE_URL="http://localhost:8080/"

#获取app.py 文件的绝对路径
APP_PATH =os.path.abspath(__file__)
print("app.py的绝对路径",APP_PATH)
#获取app.py 文件的绝对路径的父级 路径 （项目路径）
PRO_PATH=os.path.dirname(APP_PATH)
print("项目的绝对路径",PRO_PATH)
#简单应用 日志信息
# logging.warning("这是警告信息")
# logging.info("hah")
#高级应用
# 日志在实际应用中，会指定输出级别，可以输出目标，可以指定输出格式...
#需求：可以生成并输出 info 以及以上级别的日志信息，日志信息要是写出到控制台以及磁盘文件，写出格式年月日 用户 级别 函数...
#
def my_log_config():
    #获取日志对象
    logger = logging.getLogger()
    #为日志对象设计输出日志级别
    logger.setLevel(logging.INFO)
    #设置日志的输出目标（多目标）
    to_1=logging.StreamHandler() #默认到控制台
    to_2=logging.handlers.TimedRotatingFileHandler(PRO_PATH+"/log/hello.log",
                                                   when="h",
                                                   interval=12,
                                                   backupCount=10,
                                                   encoding="utf-8"
                                                   ) #输出到本地磁盘
    #指定输出格式
    formatter=logging.Formatter("%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")
    to_1.setFormatter(formatter)
    to_2.setFormatter(formatter)
    #组合： 输出格式与输出目标和日志对象相组合
    logger.addHandler(to_1)
    logger.addHandler(to_2)
my_log_config()
logging.info("nihao")