# build_tools
    用于将py文件编译成so文件
# 1.使用说明
    1.1.安装Cython
    1.2.创建一个与build_tools同级的目录src；
    1.3.将需要编译的py文件放置在src目录下；
    1.4.配置要忽略的文件，及要直接打包的文件；
    1.5.执行python build_tools/build.py build_ext --inplace.
# 2.注意事项
    2.1 为保证生产的so文件目录结构与源文件一直，请保证每个目录含有__init__.py文件；
    2.2.src目录下不要包含__init__.py文件，否则可能造成多一级src目录。


