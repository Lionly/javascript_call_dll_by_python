#!/usr/bin/env python
# -*- coding: utf-8 -*-
# webd.py

from bottle import route,run, request
from ctypes import *
import threading

# bin.dll 的源代码来自 tcc 的 example
"""
//+---------------------------------------------------------------------------
//
//  dll.c - Windows DLL example - dynamically linked part
//

#include <windows.h>
#define DLL_EXPORT __declspec(dllexport)

DLL_EXPORT void HelloWorld (void)
{
    MessageBox (0, "Hello World!", "From DLL", MB_ICONINFORMATION);
}
"""
def call_dll():
	DLL = CDLL('bin.dll') # bin.dll 的源代码来自 tcc 的 example，如上
	DLL.HelloWorld()

@route("/")
def index():
    return 'Python Bottle web 框架<br />解决 JavaScript 不能执行本地程序的一个另类解决方案';

@route('/dll')
def function():
	callback = request.query.callback
	t = threading.Thread(target=call_dll, name='callDll')
	t.start()
	json =  {'code':1, 'msg':'OK, DLL 调用成功'}
	return '%s ( %s )' % (callback, json)

def main():
    run(host='localhost', port=8089)

if __name__ == "__main__":
    # main()
    # call_dll()
    print u'请不要直接运行 web 服务'
