#!/usr/bin/env python
# -*- coding: ISO-8859-15 -*-
# generated by wxGlade 0.4.1 on Sun Mar  4 15:38:52 2007

import wx

class wxgDataMiningPnl(wx.ScrolledWindow):
    def __init__(self, *args, **kwds):

        from Gnumed.wxpython import gmDataMiningWidgets, gmPhraseWheel

        # begin wxGlade: wxgDataMiningPnl.__init__
        kwds["style"] = wx.NO_BORDER|wx.TAB_TRAVERSAL
        wx.ScrolledWindow.__init__(self, *args, **kwds)
        self._splitter = wx.SplitterWindow(self, -1, style=wx.SP_3D|wx.SP_BORDER)
        self._splitter_bottom_panel = wx.Panel(self._splitter, -1, style=wx.NO_BORDER|wx.TAB_TRAVERSAL)
        self.splitter_top_panel = wx.Panel(self._splitter, -1, style=wx.NO_BORDER|wx.TAB_TRAVERSAL)
        self._PRW_report_name = gmPhraseWheel.cPhraseWheel(self.splitter_top_panel, -1, "", style=wx.NO_BORDER)
        self._TCTRL_query = wx.TextCtrl(self.splitter_top_panel, -1, "", style=wx.TE_MULTILINE|wx.TE_WORDWRAP|wx.NO_BORDER)
        self._BTN_run = wx.Button(self.splitter_top_panel, -1, _("Run"), style=wx.BU_EXACTFIT)
        self._BTN_visualize = wx.Button(self.splitter_top_panel, -1, _("Visualize"), style=wx.BU_EXACTFIT)
        self._BTN_clear = wx.Button(self.splitter_top_panel, -1, _("Clear"), style=wx.BU_EXACTFIT)
        self._BTN_save = wx.Button(self.splitter_top_panel, -1, _("Save"), style=wx.BU_EXACTFIT)
        self._BTN_delete = wx.Button(self.splitter_top_panel, -1, _("Delete"), style=wx.BU_EXACTFIT)
        self._BTN_contribute = wx.Button(self.splitter_top_panel, -1, _("Contribute"), style=wx.BU_EXACTFIT)
        self._BTN_schema = wx.Button(self.splitter_top_panel, -1, _("Schema"), style=wx.BU_EXACTFIT)
        self._LCTRL_result = gmDataMiningWidgets.cPatientListingCtrl(self._splitter_bottom_panel, -1, style=wx.LC_REPORT|wx.LC_SINGLE_SEL|wx.SIMPLE_BORDER)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self._on_run_button_pressed, self._BTN_run)
        self.Bind(wx.EVT_BUTTON, self._on_visualize_button_pressed, self._BTN_visualize)
        self.Bind(wx.EVT_BUTTON, self._on_clear_button_pressed, self._BTN_clear)
        self.Bind(wx.EVT_BUTTON, self._on_save_button_pressed, self._BTN_save)
        self.Bind(wx.EVT_BUTTON, self._on_delete_button_pressed, self._BTN_delete)
        self.Bind(wx.EVT_BUTTON, self._on_contribute_button_pressed, self._BTN_contribute)
        self.Bind(wx.EVT_BUTTON, self._on_schema_button_pressed, self._BTN_schema)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: wxgDataMiningPnl.__set_properties
        self.SetScrollRate(10, 10)
        self._PRW_report_name.SetToolTipString(_("If you want to save this query into the database for later use you must provide a descriptive label for it here."))
        self._TCTRL_query.SetToolTipString(_("Enter the SQL commands to run here. It doesn't matter whether or not you enter a trailing \";\".\n\nNote that:\n- the query is run in a read-only transaction\n- the result list will be artificially limited to the first 1000 rows\n- you can include a column named \"pk_patient\" to make the result rows activate the corresponding patient on double-clicking"))
        self._BTN_run.SetToolTipString(_("Run the query and present the results below."))
        self._BTN_run.SetDefault()
        self._BTN_visualize.SetToolTipString(_("Visualize data from the result list below."))
        self._BTN_visualize.Enable(False)
        self._BTN_clear.SetToolTipString(_("Clear all fields."))
        self._BTN_save.SetToolTipString(_("Save the report definition."))
        self._BTN_delete.SetToolTipString(_("Delete this report definition."))
        self._BTN_contribute.SetToolTipString(_("Contribute this report definition to the GNUmed community. The report name and SQL command will be sent to the mailing list.\n\nPatient data will NOT be put AT RISK.\n\nYou may want to be careful about the SQL itself as it just might contain bits of sensitive data in, say, the WHERE conditions."))
        self._BTN_schema.SetToolTipString(_("Show the database schema definition in your web browser."))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: wxgDataMiningPnl.__do_layout
        _szr_main = wx.BoxSizer(wx.VERTICAL)
        __szr_splitter_bottom = wx.BoxSizer(wx.VERTICAL)
        _fgszr_top = wx.FlexGridSizer(3, 2, 1, 4)
        _szr_buttons = wx.BoxSizer(wx.HORIZONTAL)
        __LBL_report_name = wx.StaticText(self.splitter_top_panel, -1, _("Report"))
        _fgszr_top.Add(__LBL_report_name, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        _fgszr_top.Add(self._PRW_report_name, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        __LBL_query = wx.StaticText(self.splitter_top_panel, -1, _("\nCommand\n(SQL)"))
        _fgszr_top.Add(__LBL_query, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        _fgszr_top.Add(self._TCTRL_query, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        _fgszr_top.Add((20, 20), 0, wx.EXPAND, 0)
        _szr_buttons.Add(self._BTN_run, 0, wx.RIGHT|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 3)
        _szr_buttons.Add(self._BTN_visualize, 0, wx.RIGHT|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 3)
        _szr_buttons.Add(self._BTN_clear, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        _szr_buttons.Add((20, 20), 1, wx.EXPAND, 0)
        _szr_buttons.Add(self._BTN_save, 0, wx.RIGHT|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 3)
        _szr_buttons.Add(self._BTN_delete, 0, wx.RIGHT|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 3)
        _szr_buttons.Add(self._BTN_contribute, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        _szr_buttons.Add((20, 20), 1, wx.EXPAND, 0)
        _szr_buttons.Add(self._BTN_schema, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        _fgszr_top.Add(_szr_buttons, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 0)
        self.splitter_top_panel.SetSizer(_fgszr_top)
        _fgszr_top.AddGrowableRow(1)
        _fgszr_top.AddGrowableCol(1)
        __szr_splitter_bottom.Add(self._LCTRL_result, 1, wx.EXPAND, 0)
        self._splitter_bottom_panel.SetSizer(__szr_splitter_bottom)
        self._splitter.SplitHorizontally(self.splitter_top_panel, self._splitter_bottom_panel)
        _szr_main.Add(self._splitter, 1, wx.EXPAND, 0)
        self.SetSizer(_szr_main)
        _szr_main.Fit(self)
        # end wxGlade

    def _on_run_button_pressed(self, event): # wxGlade: wxgDataMiningPnl.<event_handler>
        print "Event handler `_on_run_button_pressed' not implemented"
        event.Skip()

    def _on_clear_button_pressed(self, event): # wxGlade: wxgDataMiningPnl.<event_handler>
        print "Event handler `_on_clear_button_pressed' not implemented"
        event.Skip()

    def _on_save_button_pressed(self, event): # wxGlade: wxgDataMiningPnl.<event_handler>
        print "Event handler `_on_save_button_pressed' not implemented"
        event.Skip()

    def _on_contribute_button_pressed(self, event): # wxGlade: wxgDataMiningPnl.<event_handler>
        print "Event handler `_on_contribute_button_pressed' not implemented"
        event.Skip()

    def _on_list_item_activated(self, event): # wxGlade: wxgDataMiningPnl.<event_handler>
        print "Event handler `_on_list_item_activated' not implemented"
        event.Skip()

    def _on_delete_button_pressed(self, event): # wxGlade: wxgDataMiningPnl.<event_handler>
        print "Event handler `_on_delete_button_pressed' not implemented"
        event.Skip()

    def _on_schema_button_pressed(self, event): # wxGlade: wxgDataMiningPnl.<event_handler>
        print "Event handler `_on_schema_button_pressed' not implemented"
        event.Skip()

    def _on_visualize_button_pressed(self, event): # wxGlade: wxgDataMiningPnl.<event_handler>
        print "Event handler `_on_visualize_button_pressed' not implemented"
        event.Skip()

# end of class wxgDataMiningPnl


