# javascript_call_dll_by_python
解决 JavaScript 不能执行本地程序的一个另类解决方案



# 安装


1、打包 exe
```
cd javascript_call_dll_by_python/local
python setup.py py2exe
```

2、添加并启动 Windows 服务
```
sc create MyWind binPath= G:\python\winweb\dist\wind.exe
sc start MyWind
```

# 测试

test 目录上传到任意服务器即可

