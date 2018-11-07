#!/usr/bin/env python 
#$ coding:utf-8 $
#__Author__:Peter Du


import logging
from  logging import handlers

class IgnoreBackupLogFilter(logging.Filter):
    """
    忽略db backup 的日志
    """
    def filter(self, record):#固定写法
        return "db backup"  in record.getMessage()
# 1.生成logger对象
logger = logging.getLogger("web")
logger.setLevel(logging.INFO)#设置全局的日志级别

#1.1把filter对象添加到logger中
logger.addFilter(IgnoreBackupLogFilter())

# 2.生成handler对象
ch = logging.StreamHandler()#创建打印在屏幕上的对象
#fh = logging.FileHandler("web.log")#创建输出到文件中的对象
# fh = handlers.RotatingFileHandler("web.log",maxBytes=10, backupCount=3)#按maxbyte存储，最多存在3个，web.log是最新的
fh = handlers.TimedRotatingFileHandler("web.log",when="S",interval=5,backupCount=3)#按时间存储，interval表示5，
# when表示时间时分秒，backupcount表示最大存储数
fh.setLevel(logging.WARNING)#设置输入到文件的日志级别

# 2.1.把handler对象 绑定到logger对象
logger.addHandler(ch)
logger.addHandler(fh)

# 3.生成formatter对象
# 3.1.把formatter对象绑定到handler对象
file_formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s:%(filename)s:%(levelno)s',
                                   datefmt='%Y-%m-%d %H:%M:%S %p')#设置日志文件的格式化输出
console_formatter = logging.Formatter('%(asctime)s---%(levelname)s:--(message)s:%(filename)s',
                                      datefmt='%Y-%m-%d %H:%M:%S %p')#设置屏幕的格式化输出

ch.setFormatter(console_formatter)#
fh.setFormatter(file_formatter)#把formatter绑定到fh上

logger.debug("debug")
logger.info("info")
logger.warning("waring")
logger.error("error")
logger.critical("critical")
logger.warning("db backup")