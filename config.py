#!/user/local/python2.6.6/bin/python
# -*- coding: utf-8 -*-
# __project__ = lib
# __author__ = kassien@163.com
# __date__ = 2015-12-16 
# __time__ = 14:11

# 源码所在目录名（要求源代码目录与本程序所在目录，为同级目录）
SRC_DIR_NAME = "src"
# 编译时要排除的文件
EXCLUDE_FILE = ["config", "build", "g_v"]
# 编译时要排除的目录
EXCLUE_DIR = ["test2", "build", "tornado-4.2.1"]

# 需要直接打包的文件列表
STATIC_FILE = ["config.py", "g_v.py"]
# 需要直接打包的目录列表
STATIC_DIR = ["template", "static"]

# 文件要传输的目标位置
RSYNC_DST = "192.168.2.193::dev"

