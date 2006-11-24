#!/usr/bin/env python
# -*- coding: ISO-8859-15 -*-
# generated by wxGlade 0.4.1 on Tue Nov 21 23:59:55 2006

import wx

class wxgHealthIssueEditAreaPnl(wx.ScrolledWindow):
    def __init__(self, *args, **kwds):

        from Gnumed.wxpython import gmPhraseWheel, gmDateTimeInput

        # begin wxGlade: wxgHealthIssueEditAreaPnl.__init__
        kwds["style"] = wx.NO_BORDER|wx.TAB_TRAVERSAL
        wx.ScrolledWindow.__init__(self, *args, **kwds)
        self._PRW_condition = gmPhraseWheel.cPhraseWheel(self, -1, "", style=wx.NO_BORDER)
        self._ChBOX_left = wx.CheckBox(self, -1, _("left"))
        self._ChBOX_right = wx.CheckBox(self, -1, _("right"))
        self._TCTRL_notes = wx.TextCtrl(self, -1, "", style=wx.TE_MULTILINE|wx.TE_WORDWRAP|wx.NO_BORDER)
        self._PRW_age_diagnosed = gmPhraseWheel.cPhraseWheel(self, -1, "", style=wx.NO_BORDER)
        self._PRW_year_diagnosed = gmDateTimeInput.cFuzzyTimestampInput(self, -1, "", style=wx.NO_BORDER)
        self._ChBOX_active = wx.CheckBox(self, -1, _("active"))
        self._ChBOX_relevant = wx.CheckBox(self, -1, _("relevant"))
        self._ChBOX_is_operation = wx.CheckBox(self, -1, _("operated on"))
        self._ChBOX_confidential = wx.CheckBox(self, -1, _("confidential"))
        self._ChBOX_caused_death = wx.CheckBox(self, -1, _("caused death"))

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: wxgHealthIssueEditAreaPnl.__set_properties
        self.SetScrollRate(10, 10)
        self._PRW_condition.SetToolTipString(_("Enter the condition (health issue/past history item) here. Keep it short but precise."))
        self._TCTRL_notes.SetToolTipString(_("Enter past history facts about the condition here. Note that those can only ever be added to from this field."))
        self._PRW_age_diagnosed.SetToolTipString(_("Enter the age in years when this condition was diagnosed. Setting this will adjust the \"in the year\" field accordingly."))
        self._PRW_year_diagnosed.SetToolTipString(_("Enter the year when this condition was diagnosed. Setting this will adjust the \"at age\" field accordingly."))
        self._ChBOX_active.SetToolTipString(_("Check if this is an active, ongoing problem."))
        self._ChBOX_relevant.SetToolTipString(_("Check if this is a clinically relevant problem."))
        self._ChBOX_relevant.SetValue(1)
        self._ChBOX_is_operation.SetToolTipString(_("Check if this is an operated-on condition (eg. appendectomy)."))
        self._ChBOX_confidential.SetToolTipString(_("Check if this condition is to be kept confidential and not disclosed to anyone else."))
        self._ChBOX_caused_death.SetToolTipString(_("Check if this condition contributed to causing death of the patient."))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: wxgHealthIssueEditAreaPnl.__do_layout
        __gszr_main = wx.FlexGridSizer(4, 2, 2, 4)
        __szr_options = wx.BoxSizer(wx.HORIZONTAL)
        __szr_diagnosed = wx.BoxSizer(wx.HORIZONTAL)
        __szr_condition = wx.BoxSizer(wx.HORIZONTAL)
        _szr_laterality = wx.BoxSizer(wx.HORIZONTAL)
        __lbl_condition = wx.StaticText(self, -1, _("Condition"))
        __lbl_condition.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        __gszr_main.Add(__lbl_condition, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        __szr_condition.Add(self._PRW_condition, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        _szr_laterality.Add(self._ChBOX_left, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        _szr_laterality.Add(self._ChBOX_right, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        __szr_condition.Add(_szr_laterality, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        __gszr_main.Add(__szr_condition, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        __lbl_notes = wx.StaticText(self, -1, _("Progress note"))
        __gszr_main.Add(__lbl_notes, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        __gszr_main.Add(self._TCTRL_notes, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        __lbl_diagnosed = wx.StaticText(self, -1, _("Diagnosed"))
        __gszr_main.Add(__lbl_diagnosed, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        __lbl_age = wx.StaticText(self, -1, _("Age:"), style=wx.ALIGN_RIGHT)
        __szr_diagnosed.Add(__lbl_age, 0, wx.RIGHT|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 2)
        __szr_diagnosed.Add(self._PRW_age_diagnosed, 1, wx.RIGHT|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 2)
        __lbl_year = wx.StaticText(self, -1, _("Year:"), style=wx.ALIGN_RIGHT)
        __szr_diagnosed.Add(__lbl_year, 0, wx.RIGHT|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 2)
        __szr_diagnosed.Add(self._PRW_year_diagnosed, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        __gszr_main.Add(__szr_diagnosed, 1, wx.EXPAND, 0)
        __gszr_main.Add((1, 1), 0, wx.EXPAND, 0)
        __szr_options.Add(self._ChBOX_active, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        __szr_options.Add(self._ChBOX_relevant, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        __szr_options.Add(self._ChBOX_is_operation, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        __szr_options.Add(self._ChBOX_confidential, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        __szr_options.Add(self._ChBOX_caused_death, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        __gszr_main.Add(__szr_options, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        self.SetAutoLayout(True)
        self.SetSizer(__gszr_main)
        __gszr_main.Fit(self)
        __gszr_main.SetSizeHints(self)
        __gszr_main.AddGrowableRow(1)
        __gszr_main.AddGrowableCol(1)
        # end wxGlade

# end of class wxgHealthIssueEditAreaPnl


