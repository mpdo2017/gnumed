#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 from "/home/ncq/Projekte/gm-cvs/branches/HEAD/gnumed/gnumed/client/wxg/wxgMeasurementsReviewDlg.wxg"

import wx

# begin wxGlade: extracode
# end wxGlade



class wxgMeasurementsReviewDlg(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: wxgMeasurementsReviewDlg.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER|wx.MAXIMIZE_BOX|wx.MINIMIZE_BOX|wx.THICK_FRAME|wx.STAY_ON_TOP
        wx.Dialog.__init__(self, *args, **kwds)
        self.__szr_relevant_staticbox = wx.StaticBox(self, -1, _("Clinically relevant"))
        self.__szr_abnormal_staticbox = wx.StaticBox(self, -1, _("Technically abnormal"))
        self._LBL_tests = wx.StaticText(self, -1, _("... test results listing goes here ..."))
        self._RBTN_confirm_abnormal = wx.RadioButton(self, -1, _("Leave as is"), style=wx.RB_GROUP)
        self._RBTN_results_normal = wx.RadioButton(self, -1, _("&Normal"))
        self._RBTN_results_abnormal = wx.RadioButton(self, -1, _("A&bnormal"))
        self._RBTN_confirm_relevance = wx.RadioButton(self, -1, _("Leave as is"), style=wx.RB_GROUP)
        self._RBTN_results_not_relevant = wx.RadioButton(self, -1, _("Not relevant"))
        self._RBTN_results_relevant = wx.RadioButton(self, -1, _("&Relevant"))
        self._TCTRL_comment = wx.TextCtrl(self, -1, "")
        self._CHBOX_responsible = wx.CheckBox(self, -1, _("&Take responsibility"))
        self._BTN_sign_off = wx.Button(self, wx.ID_APPLY, "")
        self._BTN_cancel = wx.Button(self, wx.ID_CANCEL, "")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self._on_signoff_button_pressed, self._BTN_sign_off)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: wxgMeasurementsReviewDlg.__set_properties
        self.SetTitle(_("Signing off test results"))
        self._RBTN_confirm_abnormal.SetToolTipString(_("Select this if you want to agree with the current decision on technical abnormality of the results."))
        self._RBTN_confirm_abnormal.SetValue(1)
        self._RBTN_results_normal.SetToolTipString(_("Select this if you think the selected results are normal regardless of what the result provider said."))
        self._RBTN_results_abnormal.SetToolTipString(_("Select this if you think the selected results are technically abnormal - regardless of what the result provider said."))
        self._RBTN_confirm_relevance.SetToolTipString(_("Select this if you want to agree with the current decision on clinical relevance of the results."))
        self._RBTN_confirm_relevance.SetValue(1)
        self._RBTN_results_not_relevant.SetToolTipString(_("Select this if you think the selected results are clinically not significant."))
        self._RBTN_results_relevant.SetToolTipString(_("Select this if you think the selected results are cliniccally significant."))
        self._TCTRL_comment.SetToolTipString(_("Enter a comment on this review. Only available if the review applies to a single result only."))
        self._TCTRL_comment.Enable(False)
        self._CHBOX_responsible.SetToolTipString(_("Check this to take over responsibility for initiating action on these results."))
        self._BTN_sign_off.SetToolTipString(_("Sign off test results and save review status for all selected results."))
        self._BTN_cancel.SetToolTipString(_("Cancel and discard review, that is, do NOT sign off results."))
        self._BTN_cancel.SetDefault()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: wxgMeasurementsReviewDlg.__do_layout
        __szr_main = wx.BoxSizer(wx.VERTICAL)
        __szr_buttons = wx.BoxSizer(wx.HORIZONTAL)
        __szr_comment = wx.BoxSizer(wx.HORIZONTAL)
        __szr_review = wx.BoxSizer(wx.HORIZONTAL)
        __szr_relevant = wx.StaticBoxSizer(self.__szr_relevant_staticbox, wx.HORIZONTAL)
        __szr_abnormal = wx.StaticBoxSizer(self.__szr_abnormal_staticbox, wx.HORIZONTAL)
        __msg_top = wx.StaticText(self, -1, _("This signing applies to ALL results currently selected in the viewer.\n\nIf you want to change the scope of the sign-off\nyou need to narrow or widen the selection of results."), style=wx.ALIGN_CENTRE)
        __szr_main.Add(__msg_top, 0, wx.LEFT|wx.RIGHT|wx.TOP|wx.EXPAND, 5)
        __hline_atop_tests = wx.StaticLine(self, -1)
        __szr_main.Add(__hline_atop_tests, 0, wx.ALL|wx.EXPAND, 5)
        __szr_main.Add(self._LBL_tests, 1, wx.LEFT|wx.RIGHT|wx.EXPAND, 5)
        __szr_abnormal.Add(self._RBTN_confirm_abnormal, 0, wx.EXPAND, 3)
        __szr_abnormal.Add(self._RBTN_results_normal, 0, wx.LEFT|wx.RIGHT|wx.EXPAND, 3)
        __szr_abnormal.Add(self._RBTN_results_abnormal, 0, wx.EXPAND, 0)
        __szr_review.Add(__szr_abnormal, 1, wx.EXPAND, 0)
        __szr_relevant.Add(self._RBTN_confirm_relevance, 0, wx.RIGHT|wx.EXPAND, 3)
        __szr_relevant.Add(self._RBTN_results_not_relevant, 0, wx.LEFT|wx.RIGHT|wx.EXPAND, 3)
        __szr_relevant.Add(self._RBTN_results_relevant, 0, wx.EXPAND, 3)
        __szr_review.Add(__szr_relevant, 1, wx.EXPAND, 0)
        __szr_main.Add(__szr_review, 0, wx.LEFT|wx.RIGHT|wx.TOP|wx.EXPAND, 5)
        __lbl_comment = wx.StaticText(self, -1, _("Comment"))
        __szr_comment.Add(__lbl_comment, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        __szr_comment.Add(self._TCTRL_comment, 1, wx.LEFT|wx.RIGHT|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5)
        __szr_comment.Add(self._CHBOX_responsible, 0, wx.EXPAND, 5)
        __szr_main.Add(__szr_comment, 0, wx.ALL|wx.EXPAND, 5)
        __szr_buttons.Add((20, 20), 2, wx.EXPAND, 5)
        __szr_buttons.Add(self._BTN_sign_off, 0, wx.EXPAND, 0)
        __szr_buttons.Add((20, 20), 1, wx.EXPAND, 5)
        __szr_buttons.Add(self._BTN_cancel, 0, wx.EXPAND, 0)
        __szr_buttons.Add((20, 20), 2, wx.EXPAND, 5)
        __szr_main.Add(__szr_buttons, 0, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(__szr_main)
        __szr_main.Fit(self)
        self.Layout()
        self.Centre()
        # end wxGlade

    def _on_signoff_button_pressed(self, event): # wxGlade: wxgMeasurementsReviewDlg.<event_handler>
        print "Event handler `_on_signoff_button_pressed' not implemented!"
        event.Skip()

# end of class wxgMeasurementsReviewDlg


if __name__ == "__main__":
    import gettext
    gettext.install("app") # replace with the appropriate catalog name

    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    wxPanel = wxgMeasurementsReviewDlg(None, -1, "")
    app.SetTopWindow(wxPanel)
    wxPanel.Show()
    app.MainLoop()
