#!/usr/bin/env python
# -*- coding: ISO-8859-15 -*-
# generated by wxGlade 0.4.1 on Thu Jan  4 17:21:17 2007

import wx

class wxgEpisodeEditAreaDlg(wx.Dialog):
    def __init__(self, *args, **kwds):

        from Gnumed.wxpython import gmEMRStructWidgets

        # begin wxGlade: wxgEpisodeEditAreaDlg.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER|wx.MAXIMIZE_BOX|wx.MINIMIZE_BOX|wx.THICK_FRAME|wx.STAY_ON_TOP
        wx.Dialog.__init__(self, *args, **kwds)
        self._PNL_edit_area = gmEMRStructWidgets.cEpisodeEditAreaPnl(self, -1)
        self._BTN_save = wx.Button(self, wx.ID_OK, _("Save"))
        self._BTN_close = wx.Button(self, wx.ID_CANCEL, _("Cancel"))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self._on_save_button_pressed, id=wx.ID_OK)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: wxgEpisodeEditAreaDlg.__set_properties
        self.SetTitle(_("Edit episode details"))
        self._BTN_save.SetToolTipString(_("Save the episode details."))
        self._BTN_close.SetToolTipString(_("Close this dialog."))
        self._BTN_close.SetDefault()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: wxgEpisodeEditAreaDlg.__do_layout
        __szr_main = wx.BoxSizer(wx.VERTICAL)
        __szr_buttons = wx.BoxSizer(wx.HORIZONTAL)
        __szr_main.Add(self._PNL_edit_area, 1, wx.ALL|wx.EXPAND, 2)
        __szr_buttons.Add(self._BTN_save, 0, wx.EXPAND, 0)
        __szr_buttons.Add((20, 20), 1, wx.EXPAND, 0)
        __szr_buttons.Add(self._BTN_close, 0, wx.EXPAND, 0)
        __szr_main.Add(__szr_buttons, 0, wx.EXPAND, 0)
        self.SetAutoLayout(True)
        self.SetSizer(__szr_main)
        __szr_main.Fit(self)
        __szr_main.SetSizeHints(self)
        self.Layout()
        self.Centre()
        # end wxGlade

    def _on_save_button_pressed(self, event): # wxGlade: wxgEpisodeEditAreaDlg.<event_handler>
        print "Event handler `_on_save_button_pressed' not implemented!"
        event.Skip()

# end of class wxgEpisodeEditAreaDlg


