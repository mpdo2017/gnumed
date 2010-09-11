#!/usr/bin/env python
# -*- coding: ISO-8859-15 -*-
# generated by wxGlade 0.4.1 on Wed Jan  3 16:20:33 2007

import wx

class wxgEpisodeEditAreaPnl(wx.ScrolledWindow):
    def __init__(self, *args, **kwds):

        from Gnumed.wxpython import gmEMRStructWidgets

        # begin wxGlade: wxgEpisodeEditAreaPnl.__init__
        kwds["style"] = wx.NO_BORDER|wx.TAB_TRAVERSAL
        wx.ScrolledWindow.__init__(self, *args, **kwds)
        self._TCTRL_patient = wx.TextCtrl(self, -1, "", style=wx.NO_BORDER)
        self._PRW_issue = gmEMRStructWidgets.cIssueSelectionPhraseWheel(self, -1, "", style=wx.NO_BORDER)
        self._PRW_description = gmEMRStructWidgets.cEpisodeDescriptionPhraseWheel(self, -1, "", style=wx.NO_BORDER)
        self._PRW_classification = gmEMRStructWidgets.cDiagnosticCertaintyClassificationPhraseWheel(self, -1, "", style=wx.NO_BORDER)
        self._CHBOX_closed = wx.CheckBox(self, -1, _("Closed"))
        self._TCTRL_status = wx.TextCtrl(self, -1, "", style=wx.TE_MULTILINE|wx.NO_BORDER)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: wxgEpisodeEditAreaPnl.__set_properties
        self.SetScrollRate(10, 10)
        self._TCTRL_patient.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_BACKGROUND))
        self._PRW_issue.SetToolTipString(_("Select the health issue this episode belongs to."))
        self._PRW_description.SetToolTipString(_("Type or select the description for this episode. It should be a summary for the episode of illness."))
        self._PRW_classification.SetToolTipString(_("The diagnostic classification or grading of this episode.\n\nThis documents how certain one is about this episode being a true diagnosis."))
        self._CHBOX_closed.SetToolTipString(_("If this box is checked the episode is over. If not it is currently ongoing."))
        self._TCTRL_status.SetToolTipString(_("The current status of this episode."))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: wxgEpisodeEditAreaPnl.__do_layout
        __szr_main = wx.BoxSizer(wx.VERTICAL)
        __gzsr_details = wx.FlexGridSizer(5, 2, 3, 5)
        __szr_status = wx.BoxSizer(wx.HORIZONTAL)
        __lbl_patient = wx.StaticText(self, -1, _("Patient"))
        __gzsr_details.Add(__lbl_patient, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        __gzsr_details.Add(self._TCTRL_patient, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        __lbl_issue = wx.StaticText(self, -1, _("Nest under"))
        __gzsr_details.Add(__lbl_issue, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        __gzsr_details.Add(self._PRW_issue, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        __lbl_description = wx.StaticText(self, -1, _("Description"))
        __lbl_description.SetForegroundColour(wx.Colour(255, 0, 0))
        __gzsr_details.Add(__lbl_description, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        __gzsr_details.Add(self._PRW_description, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        __lbl_certainty = wx.StaticText(self, -1, _("Certainty"))
        __gzsr_details.Add(__lbl_certainty, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        __szr_status.Add(self._PRW_classification, 1, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 15)
        __szr_status.Add(self._CHBOX_closed, 1, wx.ALIGN_CENTER_VERTICAL, 0)
        __gzsr_details.Add(__szr_status, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        __lbl_status = wx.StaticText(self, -1, _("Current\nstatus"))
        __gzsr_details.Add(__lbl_status, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        __gzsr_details.Add(self._TCTRL_status, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        __gzsr_details.AddGrowableCol(1)
        __szr_main.Add(__gzsr_details, 1, wx.EXPAND, 0)
        self.SetSizer(__szr_main)
        __szr_main.Fit(self)
        # end wxGlade

    def _on_standalone_chbox_checked(self, event): # wxGlade: wxgEpisodeEditAreaPnl.<event_handler>
        print "Event handler `_on_standalone_chbox_checked' not implemented!"
        event.Skip()

# end of class wxgEpisodeEditAreaPnl


