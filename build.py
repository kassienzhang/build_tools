#!/user/local/python2.6.6/bin/python
# -*- coding: utf-8 -*-
# __project__ = lib
# __author__ = kassien@163.com
# __date__ = 2015-12-15 
# __time__ = 14:13

from distutils.core import setup
from Cython.Build import cythonize
import os
import sys
import time
import shutil

from dir_file import *
from config import *
from date_time import no_separate_date_time_str

def main():
    # 获得本程序所在目录
    work_dir = get_work_abspath()
    # 获得源码所在目录（要求源代码目录与本程序所在目录，为同级目录）
    src_dir = os.path.join(os.path.dirname(work_dir), SRC_DIR_NAME)
    # __init__.py文件不需要编译
    exclude_file_list = EXCLUDE_FILE + ["__init__.py"]
    py_list = get_file_list(src_dir, file_suffix=".py", exclude_file_prefix=exclude_file_list,
                            exclude_dir_prefix=EXCLUE_DIR, include_root=False)
    # for f in py_list:
    #     print f
    #time.sleep(5)

    # 过滤出所有的__init__.py文件
    init_file_list = get_file_list(src_dir, "__init__.py", include_root=False)
    # 编译成so
    os.chdir(src_dir)
    setup(name="build so", ext_modules=cythonize(py_list),)

    # 获取so文件列表
    release_file_list = get_file_list(src_dir, file_suffix=".so", include_root=False)

    # 将需要直接打包的文件加入的发布列表
    release_file_list += STATIC_FILE + init_file_list

    # 从需要直接打包的目录中遍历出文件列表
    for static_dir in STATIC_DIR:
        release_file_list += get_file_list(static_dir)

    # 移动so文件到发布目录
    ver_dir = no_separate_date_time_str()
    ver_dir = sys.platform + ver_dir
    release_dir = os.path.join(os.path.dirname(src_dir), "release", ver_dir)
    j = 0
    for f in release_file_list:
        new_dir = os.path.dirname(os.path.join(release_dir, f))
        if not os.path.isdir(new_dir):
            os.makedirs(new_dir)

        os_file = os.path.join(src_dir, f)
        # print os_file, "--->", new_dir
        # shutil.move(os_file, new_dir)
        shutil.copy(os_file, new_dir)
        j += 1
    print "copy file counter: ", j

    release_zip = ver_dir+".zip"
    zip_file_list(release_dir, release_zip, release_file_list)

    release_file = os.path.join(release_dir, release_zip)
    rsync_file(release_file, RSYNC_DST)
    print "release file zip:", release_zip
    os.remove(release_file)


if __name__ == "__main__":
    main()
