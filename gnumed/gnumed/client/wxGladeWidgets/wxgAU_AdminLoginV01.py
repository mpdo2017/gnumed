#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
# generated by wxGlade 0.4cvs on Thu Jan 19 00:51:58 2006

import wx

class cAU_AdminLoginDialogV01(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: cAU_AdminLoginDialogV01.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER|wx.THICK_FRAME|wx.STAY_ON_TOP
        wx.Dialog.__init__(self, *args, **kwds)
        self.label_3 = wx.StaticText(self, -1, "host")
        self.text_ctrl_3 = wx.TextCtrl(self, -1, "localhost")
        self.label_4 = wx.StaticText(self, -1, "port")
        self.text_ctrl_4 = wx.TextCtrl(self, -1, "")
        self.label_5 = wx.StaticText(self, -1, "database")
        self.text_ctrl_5 = wx.TextCtrl(self, -1, "gnumed_v2")
        self.label_1 = wx.StaticText(self, -1, "admin user")
        self.text_ctrl_1 = wx.TextCtrl(self, -1, "")
        self.label_2 = wx.StaticText(self, -1, "password")
        self.text_ctrl_2 = wx.TextCtrl(self, -1, "", style=wx.TE_PASSWORD)
        self.button_1 = wx.Button(self, -1, "ok")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.admin_login_ok, self.button_1)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: cAU_AdminLoginDialogV01.__set_properties
        self.SetTitle("Admin Login Required")
        self.text_ctrl_1.SetFocus()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: cAU_AdminLoginDialogV01.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer_1 = wx.GridSizer(5, 2, 0, 0)
        grid_sizer_1.Add(self.label_3, 0, wx.ADJUST_MINSIZE, 0)
        grid_sizer_1.Add(self.text_ctrl_3, 1, wx.ADJUST_MINSIZE, 0)
        grid_sizer_1.Add(self.label_4, 0, wx.ADJUST_MINSIZE, 0)
        grid_sizer_1.Add(self.text_ctrl_4, 1, wx.ADJUST_MINSIZE, 0)
        grid_sizer_1.Add(self.label_5, 0, wx.ADJUST_MINSIZE, 0)
        grid_sizer_1.Add(self.text_ctrl_5, 1, wx.ADJUST_MINSIZE, 0)
        grid_sizer_1.Add(self.label_1, 0, wx.ADJUST_MINSIZE, 0)
        grid_sizer_1.Add(self.text_ctrl_1, 1, wx.EXPAND|wx.ADJUST_MINSIZE, 0)
        grid_sizer_1.Add(self.label_2, 0, wx.ADJUST_MINSIZE, 0)
        grid_sizer_1.Add(self.text_ctrl_2, 0, wx.EXPAND|wx.ADJUST_MINSIZE, 0)
        sizer_1.Add(grid_sizer_1, 1, wx.EXPAND, 0)
        sizer_2.Add(self.button_1, 0, wx.ADJUST_MINSIZE, 0)
        sizer_2.Add((20, 20), 0, wx.ADJUST_MINSIZE, 0)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
        self.SetAutoLayout(True)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        sizer_1.SetSizeHints(self)
        self.Layout()
        # end wxGlade

    def admin_login_ok(self, event): # wxGlade: cAU_AdminLoginDialogV01.<event_handler>
        print "Event handler `admin_login_ok' not implemented!"
        event.Skip()

# end of class cAU_AdminLoginDialogV01


