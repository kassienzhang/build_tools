#!/user/local/python2.6.6/bin/python
# -*- coding: utf-8 -*-
# __project__ = lib
# __author__ = kassien@163.com
# __date__ = 2015-12-16 
# __time__ = 15:52

"""常用的时间处理方法
"""

import time


def normal_date_time_str(t=0):
    """
    根据整形时间戳t, 计算一个%Y-%m-%d %H:%M:%S格式的时间字符串，如果t为0，则计算当前时间的时间字符串
    Args:
        t： 整形时间戳
    Returns:
        %Y-%m-%d %H:%M:%S 格式的时间字符串
    """
    fmt = "%Y-%m-%d %H:%M:%S"
    if t == 0:
        return time.strftime(fmt, time.localtime(time.time()))
    else:
        return time.strftime(fmt, time.localtime(t))


def normal_date_str(t=0):
    """
    根据整形时间戳t, 计算一个%Y-%m-%d格式的日期字符串，如果t为0，则计算当前时间的日期字符串
    Args:
        t： 整形时间戳
    Returns:
        %Y-%m-%d格式的时间字符串
    """
    return normal_date_time_str(t)[:10]


def no_separate_date_time_str(t=0):
    """
    根据整形时间戳t, 计算一个没有任何分割字符的%Y%m%d%H%M%S格式的时间字符串，如果t为0，则计算当前时间的时间字符串
    Args:
        t： 整形时间戳
    Returns:
        %Y%m%d%H%M%S 格式的时间字符串
    """
    fmt = "%Y%m%d%H%M%S"
    if t == 0:
        return time.strftime(fmt, time.localtime(time.time()))
    else:
        return time.strftime(fmt, time.localtime(t))


def no_separate_date_str(t=0):
    """
    根据整形时间戳t, 计算一个没有任何分割字符的%Y%m%d格式的日期字符串，如果t为0，则计算当前时间的日期字符串
    Args:
        t： 整形时间戳
    Returns:
        %Y%m%d 格式的时间字符串
    """
    return no_separate_date_time_str(t)[:8]


if __name__ == "__main__":
    print normal_date_time_str()
    print normal_date_str()
    print no_separate_date_time_str()
    print no_separate_date_str()