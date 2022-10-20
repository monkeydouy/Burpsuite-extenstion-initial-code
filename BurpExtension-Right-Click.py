# -*- coding: utf-8 -*-

from burp import IBurpExtender, IContextMenuFactory, IHttpRequestResponse
from java.util import ArrayList
from javax.swing import JMenuItem
import sys
from base64 import b64decode
from base64 import b64encode
import os
import subprocess

class BurpExtender(IBurpExtender, IContextMenuFactory, IHttpRequestResponse):
    def registerExtenderCallbacks(self, callbacks):
        # your extension code here
        sys.stdout = callbacks.getStdout()
        self.callbacks = callbacks
        self.helpers = callbacks.getHelpers()
        self.callbacks.setExtensionName("Extension Name")
        callbacks.registerContextMenuFactory(self)
        print "Success"
        return
    
    def createMenuItems(self, invocation):
        self.context = invocation
        menuList = ArrayList()
        menuItem = JMenuItem("Encrypt",actionPerformed=self.encrypt)
        menuList.add(menuItem)
        menuItem = JMenuItem("Decrypt", actionPerformed=self.decrypt)
        menuList.add(menuItem)
        return menuList

    def encrypt(self,  event):
        print "Encrypt"

    def decrypt(self, event):
        print "Decrypt"

try:
    from exceptions_fix import FixBurpExceptions
except ImportError:
    pass