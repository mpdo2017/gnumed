#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.5 from "/home/ncq/Projekte/gm-git/gnumed/gnumed/client/wxg/wxgTextExpansionFillInDlg.wxg"

import wx

# begin wxGlade: extracode
# end wxGlade


class wxgTextExpansionFillInDlg(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: wxgTextExpansionFillInDlg.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER | wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX | wx.THICK_FRAME
        wx.Dialog.__init__(self, *args, **kwds)
        self._LBL_top_part = wx.StaticText(self, -1, "")
        self._LBL_left_part = wx.StaticText(self, -1, "")
        self._TCTRL_fillin = wx.TextCtrl(self, -1, "", style=wx.TE_PROCESS_ENTER | wx.NO_BORDER)
        self._LBL_right_part = wx.StaticText(self, -1, "")
        self._LBL_bottom_part = wx.StaticText(self, -1, "")
        self._BTN_OK = wx.Button(self, wx.ID_OK, "")
        self._BTN_forward = wx.Button(self, wx.ID_FORWARD, "")
        self._BTN_cancel = wx.Button(self, wx.ID_CANCEL, "")
        self._LBL_hint = wx.StaticText(self, -1, "")
        self.__szr_hint_staticbox = wx.StaticBox(self, -1, "")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self._on_forward_button_pressed, self._BTN_forward)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: wxgTextExpansionFillInDlg.__set_properties
        self.SetTitle(_("dialog_3"))
        self._BTN_OK.SetToolTipString(_("Finish filling in text macro (ignores pending fill-in positions)."))
        self._BTN_OK.Enable(False)
        self._BTN_forward.SetToolTipString(_("Go to the next fill-in position."))
        self._BTN_forward.SetDefault()
        self._BTN_cancel.SetToolTipString(_("Cancel filling in the text expansion."))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: wxgTextExpansionFillInDlg.__do_layout
        __szr_main = wx.BoxSizer(wx.VERTICAL)
        self.__szr_hint_staticbox.Lower()
        __szr_hint = wx.StaticBoxSizer(self.__szr_hint_staticbox, wx.HORIZONTAL)
        __szr_buttons = wx.BoxSizer(wx.HORIZONTAL)
        __szr_single_line_replacement = wx.BoxSizer(wx.HORIZONTAL)
        __lbl_message = wx.StaticText(self, -1, _("\nPlease fill in an appropriate value below.\n"))
        __szr_main.Add(__lbl_message, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.ALIGN_CENTER_HORIZONTAL, 3)
        __hline_top = wx.StaticLine(self, -1)
        __szr_main.Add(__hline_top, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 3)
        __szr_main.Add(self._LBL_top_part, 0, wx.LEFT | wx.RIGHT | wx.EXPAND, 3)
        __szr_single_line_replacement.Add(self._LBL_left_part, 0, wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 3)
        __szr_single_line_replacement.Add(self._TCTRL_fillin, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        __szr_single_line_replacement.Add(self._LBL_right_part, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 3)
        __szr_single_line_replacement.Add((20, 20), 1, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 0)
        __szr_main.Add(__szr_single_line_replacement, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.EXPAND, 3)
        __szr_main.Add(self._LBL_bottom_part, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.EXPAND, 3)
        __szr_main.Add((20, 20), 1, wx.EXPAND, 0)
        __szr_buttons.Add((20, 20), 1, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 0)
        __szr_buttons.Add(self._BTN_OK, 0, wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 10)
        __szr_buttons.Add(self._BTN_forward, 0, wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 10)
        __szr_buttons.Add(self._BTN_cancel, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        __szr_buttons.Add((20, 20), 1, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 0)
        __szr_main.Add(__szr_buttons, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.EXPAND, 3)
        __szr_hint.Add(self._LBL_hint, 1, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 0)
        __szr_main.Add(__szr_hint, 0, wx.ALL | wx.EXPAND, 3)
        self.SetSizer(__szr_main)
        __szr_main.Fit(self)
        self.Layout()
        self.Centre()
        # end wxGlade

    def _on_ok_button_pressed(self, event):  # wxGlade: wxgTextExpansionFillInDlg.<event_handler>
        print "Event handler `_on_ok_button_pressed' not implemented!"
        event.Skip()

    def _on_forward_button_pressed(self, event):  # wxGlade: wxgTextExpansionFillInDlg.<event_handler>
        print "Event handler `_on_forward_button_pressed' not implemented!"
        event.Skip()

# end of class wxgTextExpansionFillInDlg
if __name__ == "__main__":
    import gettext
    gettext.install("app") # replace with the appropriate catalog name

    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    dialog_1 = (None, -1, "")
    app.SetTopWindow(dialog_1)
    dialog_1.Show()
    app.MainLoop()
