#!/user/local/python2.6.6/bin/python
# -*- coding: utf-8 -*-
# __project__ = lib
# __author__ = kassien@163.com
# __date__ = 2015-08-27 
# __time__ = 17:06
"""此模块包含常用的文件操作方法
"""

import os
import sys
import zipfile
import subprocess


def get_file_list(search_dir='./', name_filter='', file_prefix='', file_suffix='',
                  exclude_file_prefix=[], exclude_dir_prefix=[],
                  include_root=True):
    """遍历制定目录下的所有文件，根据name_filter、file_start、file_end过滤出想要的文件列表，

    Args:
        search_dir: 指定要查找的目录, 默认为当前目录
        name_filter: 指定文件名中要包含的字符串，默认为‘’，表示返回所有文件
        file_prefix: 指定文件名的开始字符串，默认为‘’，表示返回所有文件
        file_suffix: 指定文件名的结束字符串，默认为‘’，表示返回所有文件
        exclude_file_prefix: 指定要排除的文件的文件名前缀列表, 默认为[], 表示返回所有文件
        exclude_dir_prefix: 指定要排除的目录的目录名前缀列表, 默认为[], 表示返回所有目录下的文件
        include_root: 是否包含基础路径

    Returns:
        一个包含路径的文件列表

    Raises：

    """
    file_list = []
    try:
        for root, dirs, files in os.walk(search_dir):
            # 过滤掉需要排除的路径
            flag = False
            for d in exclude_dir_prefix:
                n_d = os.path.join(search_dir, d)
                if root.startswith(n_d):
                    # print "jump dir: ", root
                    flag = True
                    break
            if flag:
                continue

            if not include_root:
                root = root.replace(search_dir, '', 1).lstrip('/')
            for f in files:
                # 过滤掉需要排除的文件
                flag = False
                for p in exclude_file_prefix:
                    if f.startswith(p):
                        flag = True
                        break
                if flag:
                    continue

                if f.find(name_filter) > -1 and f.startswith(file_prefix) and f.endswith(file_suffix):
                    full_file = os.path.join(root, f)
                    file_list.append(full_file)
        return file_list

    except Exception, e:
        raise e


def get_work_abspath():
    """获取执行程序所在的绝对路径
    Args:
        无
    Returns:
        一个目录字符串
    """
    work_dir = os.path.dirname(sys.argv[0])
    if len(work_dir) == 0:
        work_dir = "."
    return os.path.abspath(work_dir)


def zip_file_list(dir_name, zip_file_name, file_list=[]):
    """将给定目录下指定的文件进行压缩, 如果指定的文件列表为空，则压缩目录下所有文件
    Args：
        dir_name: 被压缩文件所在目录
        zip_file_name: 压缩后的文件名
        file_list: 被压缩的文件列表，如果为空，则压缩所有dir_name下的文件
    Returns:
        无
    """
    tmp_file_list = []
    if os.path.isdir(dir_name):
        os.chdir(dir_name)
        if file_list:
            tmp_file_list = file_list
        else:
            for root, dirs, files in os.walk("./"):
                for f in files:
                    tmp_file_list.append(os.path.join(root, f))
        zf = zipfile.ZipFile(zip_file_name, "w", zipfile.zlib.DEFLATED)
        for f in tmp_file_list:
            zf.write(f)
        zf.close()


def unzip_file(zip_filename, unzip_to_dir):
    """将zip文件解压到制定的目录下
    Args:
        zip_filename: zip格式的压缩文件
        unzip_to_dir: 用于保存解压出来的文件
    Returns:
        无
    """
    if not os.path.exists(unzip_to_dir):
        os.makedirs(unzip_to_dir)
    zf_obj = zipfile.ZipFile(zip_filename)
    for name in zf_obj.namelist():
        name = name.replace('\\', '/')  # 替换路径分隔符为linux格式
        if name.endswith('/'):
            os.makedirs(os.path.join(unzip_to_dir, name))
        else:
            ext_filename = os.path.join(unzip_to_dir, name)
            ext_dir = os.path.dirname(ext_filename)
            if not os.path.exists(ext_dir):
                os.makedirs(ext_dir)
            outfile = open(ext_filename, 'wb')
            outfile.write(zf_obj.read(name))
            outfile.close()


def rsync_file(src, dst, password_file=None):
    """通过调用系统命令将文件同步到目标服务器，例如：
       rsync_file("abc/aa.txt", "192.168.2.193::dev")
       rsync_file("abc/bb/", "192.168.2.193::dev")
       rsync_file("abc/bb/", "user@192.168.2.193::dev", "password_file")

    Args:
        src: 要同步的源
        dst: 要同步的目标
        password_file: 密码文件
    Returns:
        无

    """
    rsync_bin = "rsync -a %s %s" % (src, dst)
    if password_file:
        rsync_bin = "%s --password-file %s" % (rsync_bin, password_file)

    # 通过rsync命令尝试同步文件，如果失败，最多尝试3次
    i = 0
    try_times = 3
    while i < try_times:
        ret = subprocess.call(rsync_bin, shell=True)
        if ret == 0:
            break
        i += 1


if __name__ == '__main__':
    # for f in get_file_list('.', file_suffix='.py', exclude_dir_prefix=["tornado", "requests"],
    #                        exclude_file_prefix=["build"]):
    #     print f
    rsync_file("build.py", "rsync_user@192.168.2.193::dev")