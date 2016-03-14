

# 安装


1、打包 exe
```
python setup.py py2exe
```

2、添加并启动 Windows 服务
```
sc create MyWind binPath= G:\python\winweb\dist\wind.exe
sc start MyWind
```

