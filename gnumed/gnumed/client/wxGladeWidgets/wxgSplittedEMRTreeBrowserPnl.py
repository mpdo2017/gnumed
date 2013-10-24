#!/usr/bin/env python
# -*- coding: ISO-8859-15 -*-
# generated by wxGlade 0.4cvs on Sun May 28 15:57:29 2006

import wx

class wxgSplittedEMRTreeBrowserPnl(wx.Panel):

    def __init__(self, *args, **kwds):

        from Gnumed.wxpython import gmEMRBrowser
        from Gnumed.wxpython.gmNarrativeWidgets import cVisualSoapPresenterPnl
        from Gnumed.wxpython.gmNarrativeWidgets import cFancySoapEditorPnl

        # begin wxGlade: wxgSplittedEMRTreeBrowserPnl.__init__
        kwds["style"] = wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self._splitter_browser = wx.SplitterWindow(self, wx.ID_ANY, style=wx.SP_3D | wx.SP_BORDER)
        self.__pnl_left_side = wx.Panel(self._splitter_browser, wx.ID_ANY, style=wx.NO_BORDER | wx.TAB_TRAVERSAL)
        self._pnl_emr_tree = gmEMRBrowser.cScrolledEMRTreePnl(self.__pnl_left_side, wx.ID_ANY, style=wx.NO_BORDER | wx.TAB_TRAVERSAL)
        self._PNL_right_side = wx.Panel(self._splitter_browser, wx.ID_ANY, style=wx.NO_BORDER)
        self._RBTN_details = wx.RadioButton(self._PNL_right_side, wx.ID_ANY, _("S&ynopsis"))
        self._RBTN_journal = wx.RadioButton(self._PNL_right_side, wx.ID_ANY, _("&Journal"))
        self._RBTN_revisions = wx.RadioButton(self._PNL_right_side, wx.ID_ANY, _("Revisions"))
        self._BTN_switch_browse_edit = wx.Button(self._PNL_right_side, wx.ID_ANY, _("&Edit"), style=wx.BU_EXACTFIT)
        self._PNL_browse = wx.Panel(self._PNL_right_side, wx.ID_ANY, style=wx.NO_BORDER | wx.TAB_TRAVERSAL)
        self._TCTRL_item_details = wx.TextCtrl(self._PNL_browse, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL | wx.TE_WORDWRAP | wx.NO_BORDER)
        self._PNL_visual_soap = cVisualSoapPresenterPnl(self._PNL_browse, wx.ID_ANY, style=wx.NO_BORDER)
        self._PNL_edit = cFancySoapEditorPnl(self._PNL_right_side, wx.ID_ANY, style=wx.NO_BORDER | wx.TAB_TRAVERSAL)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_RADIOBUTTON, self._on_show_details_selected, self._RBTN_details)
        self.Bind(wx.EVT_RADIOBUTTON, self._on_show_journal_selected, self._RBTN_journal)
        self.Bind(wx.EVT_RADIOBUTTON, self._on_show_revisions_selected, self._RBTN_revisions)
        self.Bind(wx.EVT_BUTTON, self._on_switch_browse_edit_button_pressed, self._BTN_switch_browse_edit)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: wxgSplittedEMRTreeBrowserPnl.__set_properties
        self._pnl_emr_tree.SetScrollRate(10, 10)
        self._RBTN_details.SetToolTipString(_("Show succinct item synopsis."))
        self._RBTN_details.SetValue(1)
        self._RBTN_journal.SetToolTipString(_("Show item journal."))
        self._RBTN_revisions.SetToolTipString(_("Show item revisions."))
        self._BTN_switch_browse_edit.SetToolTipString(_("Press this button to switch back and forth between browsing and entering SOAP notes."))
        self._PNL_edit.Hide()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: wxgSplittedEMRTreeBrowserPnl.__do_layout
        __szr_main = wx.BoxSizer(wx.HORIZONTAL)
        __szr_right_side = wx.BoxSizer(wx.VERTICAL)
        __szr_browse = wx.BoxSizer(wx.VERTICAL)
        __szr_item_details_options = wx.BoxSizer(wx.HORIZONTAL)
        __szr_left_side = wx.BoxSizer(wx.VERTICAL)
        __szr_left_side.Add(self._pnl_emr_tree, 1, wx.EXPAND, 0)
        self.__pnl_left_side.SetSizer(__szr_left_side)
        __lbl_show_mode = wx.StaticText(self._PNL_right_side, wx.ID_ANY, _("Show:"))
        __szr_item_details_options.Add(__lbl_show_mode, 0, wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 5)
        __szr_item_details_options.Add(self._RBTN_details, 0, wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 5)
        __szr_item_details_options.Add(self._RBTN_journal, 0, wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 5)
        __szr_item_details_options.Add(self._RBTN_revisions, 0, wx.ALIGN_CENTER_VERTICAL, 5)
        __szr_item_details_options.Add((20, 20), 1, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 0)
        __szr_item_details_options.Add(self._BTN_switch_browse_edit, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        __szr_right_side.Add(__szr_item_details_options, 0, wx.EXPAND, 0)
        __szr_browse.Add(self._TCTRL_item_details, 1, wx.TOP | wx.EXPAND, 3)
        __szr_browse.Add(self._PNL_visual_soap, 0, wx.EXPAND, 0)
        self._PNL_browse.SetSizer(__szr_browse)
        __szr_right_side.Add(self._PNL_browse, 1, wx.EXPAND, 0)
        __szr_right_side.Add(self._PNL_edit, 1, wx.EXPAND, 0)
        self._PNL_right_side.SetSizer(__szr_right_side)
        self._splitter_browser.SplitVertically(self.__pnl_left_side, self._PNL_right_side)
        __szr_main.Add(self._splitter_browser, 1, wx.EXPAND, 0)
        self.SetSizer(__szr_main)
        __szr_main.Fit(self)
        # end wxGlade

    def _on_show_details_selected(self, event): # wxGlade: wxgSplittedEMRTreeBrowserPnl.<event_handler>
        print "Event handler `_on_show_details_selected' not implemented"
        event.Skip()

    def _on_show_journal_selected(self, event): # wxGlade: wxgSplittedEMRTreeBrowserPnl.<event_handler>
        print "Event handler `_on_show_journal_selected' not implemented"
        event.Skip()

    def _on_switch_browse_edit_button_pressed(self, event):  # wxGlade: wxgSplittedEMRTreeBrowserPnl.<event_handler>
        print "Event handler `_on_switch_browse_edit_button_pressed' not implemented"
        event.Skip()

    def _on_show_revisions_selected(self, event):  # wxGlade: wxgSplittedEMRTreeBrowserPnl.<event_handler>
        print "Event handler '_on_show_revisions_selected' not implemented!"
        event.Skip()
# end of class wxgSplittedEMRTreeBrowserPnl

