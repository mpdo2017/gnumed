#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 from "/home/ncq/Projekte/gm-cvs/branches/HEAD/gnumed/gnumed/client/wxg/wxgSoapNoteExpandoEditAreaPnl.wxg"

import wx

# begin wxGlade: extracode
# end wxGlade

class wxgSoapNoteExpandoEditAreaPnl(wx.ScrolledWindow):
    def __init__(self, *args, **kwds):

        from Gnumed.wxpython.gmTextCtrl import cExpandoTextCtrl
        from Gnumed.wxpython.gmVisualProgressNoteWidgets import cVisualSoapPresenterPnl
        from Gnumed.wxpython.gmCodingWidgets import cGenericCodesPhraseWheel

        # begin wxGlade: wxgSoapNoteExpandoEditAreaPnl.__init__
        kwds["style"] = wx.NO_BORDER|wx.TAB_TRAVERSAL
        wx.ScrolledWindow.__init__(self, *args, **kwds)
        self._PRW_Soap_codes = cGenericCodesPhraseWheel(self, -1, "", style=wx.TE_READONLY|wx.NO_BORDER)
        self._TCTRL_Soap = cExpandoTextCtrl(self, -1, "", style=wx.TE_WORDWRAP|wx.NO_BORDER)
        self._PRW_sOap_codes = cGenericCodesPhraseWheel(self, -1, "", style=wx.TE_READONLY|wx.NO_BORDER)
        self._TCTRL_sOap = cExpandoTextCtrl(self, -1, "", style=wx.TE_WORDWRAP|wx.NO_BORDER)
        self._PRW_soAp_codes = cGenericCodesPhraseWheel(self, -1, "", style=wx.TE_READONLY|wx.NO_BORDER)
        self._TCTRL_soAp = cExpandoTextCtrl(self, -1, "", style=wx.TE_WORDWRAP|wx.NO_BORDER)
        self._PRW_soaP_codes = cGenericCodesPhraseWheel(self, -1, "", style=wx.TE_READONLY|wx.NO_BORDER)
        self._TCTRL_soaP = cExpandoTextCtrl(self, -1, "", style=wx.TE_WORDWRAP|wx.NO_BORDER)
        self._PNL_visual_soap = cVisualSoapPresenterPnl(self, -1, style=wx.NO_BORDER)
        self._LBL_summary = wx.StaticText(self, -1, _("Episode synopsis"))
        self._PRW_episode_codes = cGenericCodesPhraseWheel(self, -1, "", style=wx.NO_BORDER)
        self._TCTRL_episode_summary = cExpandoTextCtrl(self, -1, "", style=wx.TE_WORDWRAP|wx.NO_BORDER)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: wxgSoapNoteExpandoEditAreaPnl.__set_properties
        self.SetScrollRate(10, 10)
        self._PRW_Soap_codes.SetToolTipString(_("Codes relevant to this Subjective\nseparated by \";\"."))
        self._PRW_Soap_codes.Enable(False)
        self._PRW_sOap_codes.SetToolTipString(_("Codes relevant to this Objective\nseparated by \";\"."))
        self._PRW_sOap_codes.Enable(False)
        self._PRW_soAp_codes.SetToolTipString(_("Codes relevant to this Assessment\nseparated by \";\"."))
        self._PRW_soAp_codes.Enable(False)
        self._PRW_soaP_codes.SetToolTipString(_("Codes relevant to this Plan\nseparated by \";\"."))
        self._PRW_soaP_codes.Enable(False)
        self._PRW_episode_codes.SetToolTipString(_("Codes relevant to this episode\nseparated by \";\"."))
        self._TCTRL_episode_summary.SetToolTipString(_("Here you can modify the cumulative summary (status) of the episode this SOAP narrative belongs to."))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: wxgSoapNoteExpandoEditAreaPnl.__do_layout
        __szr_main = wx.BoxSizer(wx.VERTICAL)
        __szr_summary = wx.BoxSizer(wx.HORIZONTAL)
        __szr_soaP = wx.BoxSizer(wx.HORIZONTAL)
        __szr_soAp = wx.BoxSizer(wx.HORIZONTAL)
        __szr_sOap = wx.BoxSizer(wx.HORIZONTAL)
        __szr_Soap = wx.BoxSizer(wx.HORIZONTAL)
        __lbl_Soap = wx.StaticText(self, -1, _("Subjective"))
        __szr_Soap.Add(__lbl_Soap, 1, wx.ALIGN_CENTER_VERTICAL, 10)
        __vline_Soap = wx.StaticLine(self, -1, style=wx.LI_VERTICAL)
        __szr_Soap.Add(__vline_Soap, 0, wx.RIGHT|wx.EXPAND, 5)
        __lbl_Soap_codes = wx.StaticText(self, -1, _("Codes:"))
        __lbl_Soap_codes.Hide()
        __szr_Soap.Add(__lbl_Soap_codes, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        __szr_Soap.Add(self._PRW_Soap_codes, 3, wx.TOP|wx.BOTTOM|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 2)
        __szr_main.Add(__szr_Soap, 0, wx.LEFT|wx.RIGHT|wx.EXPAND, 3)
        __szr_main.Add(self._TCTRL_Soap, 0, wx.LEFT|wx.RIGHT|wx.EXPAND, 3)
        __lbl_sOap = wx.StaticText(self, -1, _("Objective"))
        __szr_sOap.Add(__lbl_sOap, 1, wx.ALIGN_CENTER_VERTICAL, 5)
        __vline_sOap = wx.StaticLine(self, -1, style=wx.LI_VERTICAL)
        __szr_sOap.Add(__vline_sOap, 0, wx.RIGHT|wx.EXPAND, 5)
        __lbl_sOap_codes = wx.StaticText(self, -1, _("Codes:"))
        __lbl_sOap_codes.Hide()
        __szr_sOap.Add(__lbl_sOap_codes, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        __szr_sOap.Add(self._PRW_sOap_codes, 3, wx.TOP|wx.BOTTOM|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 2)
        __szr_main.Add(__szr_sOap, 0, wx.LEFT|wx.RIGHT|wx.EXPAND, 3)
        __szr_main.Add(self._TCTRL_sOap, 0, wx.LEFT|wx.RIGHT|wx.EXPAND, 3)
        __lbl_soAp = wx.StaticText(self, -1, _("Assessment"))
        __szr_soAp.Add(__lbl_soAp, 1, wx.ALIGN_CENTER_VERTICAL, 5)
        __vline_soAp = wx.StaticLine(self, -1, style=wx.LI_VERTICAL)
        __szr_soAp.Add(__vline_soAp, 0, wx.RIGHT|wx.EXPAND, 5)
        __lbl_soAp_codes = wx.StaticText(self, -1, _("Codes:"))
        __lbl_soAp_codes.Hide()
        __szr_soAp.Add(__lbl_soAp_codes, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        __szr_soAp.Add(self._PRW_soAp_codes, 3, wx.TOP|wx.BOTTOM|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 2)
        __szr_main.Add(__szr_soAp, 0, wx.LEFT|wx.RIGHT|wx.EXPAND, 3)
        __szr_main.Add(self._TCTRL_soAp, 0, wx.LEFT|wx.RIGHT|wx.EXPAND, 3)
        __lbl_soaP = wx.StaticText(self, -1, _("Plan"))
        __szr_soaP.Add(__lbl_soaP, 1, wx.ALIGN_CENTER_VERTICAL, 5)
        __vline_soaP = wx.StaticLine(self, -1, style=wx.LI_VERTICAL)
        __szr_soaP.Add(__vline_soaP, 0, wx.RIGHT|wx.EXPAND, 5)
        __lbl_soaP_codes = wx.StaticText(self, -1, _("Codes:"))
        __lbl_soaP_codes.Hide()
        __szr_soaP.Add(__lbl_soaP_codes, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        __szr_soaP.Add(self._PRW_soaP_codes, 3, wx.TOP|wx.BOTTOM|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 2)
        __szr_main.Add(__szr_soaP, 0, wx.LEFT|wx.RIGHT|wx.EXPAND, 3)
        __szr_main.Add(self._TCTRL_soaP, 0, wx.LEFT|wx.RIGHT|wx.BOTTOM|wx.EXPAND, 3)
        __szr_main.Add(self._PNL_visual_soap, 0, wx.EXPAND, 0)
        _hline_above_summary = wx.StaticLine(self, -1)
        __szr_main.Add(_hline_above_summary, 0, wx.LEFT|wx.RIGHT|wx.TOP|wx.EXPAND, 5)
        __szr_summary.Add(self._LBL_summary, 1, wx.ALIGN_CENTER_VERTICAL, 5)
        __vline_summary = wx.StaticLine(self, -1, style=wx.LI_VERTICAL)
        __szr_summary.Add(__vline_summary, 0, wx.RIGHT|wx.EXPAND, 5)
        __lbl_summary_codes = wx.StaticText(self, -1, _("Codes:"))
        __szr_summary.Add(__lbl_summary_codes, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        __szr_summary.Add(self._PRW_episode_codes, 3, wx.TOP|wx.BOTTOM|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 2)
        __szr_main.Add(__szr_summary, 0, wx.LEFT|wx.RIGHT|wx.EXPAND, 3)
        __szr_main.Add(self._TCTRL_episode_summary, 0, wx.LEFT|wx.RIGHT|wx.BOTTOM|wx.EXPAND, 3)
        self.SetSizer(__szr_main)
        __szr_main.Fit(self)
        # end wxGlade

    def _on_manage_Soap_codes_button_pressed(self, event): # wxGlade: wxgSoapNoteExpandoEditAreaPnl.<event_handler>
        print "Event handler `_on_manage_Soap_codes_button_pressed' not implemented"
        event.Skip()

    def _on_manage_sOap_codes_button_pressed(self, event): # wxGlade: wxgSoapNoteExpandoEditAreaPnl.<event_handler>
        print "Event handler `_on_manage_sOap_codes_button_pressed' not implemented"
        event.Skip()

    def _on_manage_soAp_codes_button_pressed(self, event): # wxGlade: wxgSoapNoteExpandoEditAreaPnl.<event_handler>
        print "Event handler `_on_manage_soAp_codes_button_pressed' not implemented"
        event.Skip()

    def _on_manage_soaP_codes_button_pressed(self, event): # wxGlade: wxgSoapNoteExpandoEditAreaPnl.<event_handler>
        print "Event handler `_on_manage_soaP_codes_button_pressed' not implemented"
        event.Skip()

# end of class wxgSoapNoteExpandoEditAreaPnl


