#!/usr/bin/env python
# -*- coding: utf-8 -*-
# wind.py

import win32serviceutil
import win32service
import win32event
import thread

class WindowsService(win32serviceutil.ServiceFramework):
    # 这两行必须
    _svc_name_ = "Web WindowsService"
    _svc_display_name_ = "Web WindowsService"
    
    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        import webd
        thread.start_new(webd.main, ())
        win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)

