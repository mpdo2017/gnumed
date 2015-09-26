#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.7.0
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
from Gnumed.wxpython.gmListWidgets import cReportListCtrl
from Gnumed.wxpython.gmTextCtrl import cTextCtrl
# end wxGlade


class wxgPACSPluginPnl(wx.Panel):
	def __init__(self, *args, **kwds):
		# begin wxGlade: wxgPACSPluginPnl.__init__
		kwds["style"] = wx.BORDER_NONE | wx.TAB_TRAVERSAL
		wx.Panel.__init__(self, *args, **kwds)
		self._TCTRL_host = cTextCtrl(self, wx.ID_ANY, "", style=wx.BORDER_NONE)
		self._TCTRL_port = cTextCtrl(self, wx.ID_ANY, "", style=wx.BORDER_NONE)
		self._TCTRL_user = cTextCtrl(self, wx.ID_ANY, "", style=wx.BORDER_NONE)
		self._TCTRL_password = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.BORDER_NONE | wx.TE_PASSWORD)
		self._BTN_connect = wx.Button(self, wx.ID_ANY, _("&Connect"), style=wx.BU_EXACTFIT)
		self._BTN_browse_pacs = wx.Button(self, wx.ID_ANY, _("&Browse"), style=wx.BU_EXACTFIT)
		self._LBL_PACS_identification = wx.StaticText(self, wx.ID_ANY, _("<not connected>"))
		self._LBL_patient_identification = wx.StaticText(self, wx.ID_ANY, "")
		self._LBL_no_of_studies = wx.StaticText(self, wx.ID_ANY, "")
		self._BTN_browse_patient = wx.Button(self, wx.ID_ANY, _("Browse all"), style=wx.BU_EXACTFIT)
		self._BTN_export_all_studies = wx.Button(self, wx.ID_ANY, _("Export all"), style=wx.BU_EXACTFIT)
		self._BTN_browse_study = wx.Button(self, wx.ID_ANY, _("Browse"), style=wx.BU_EXACTFIT)
		self._BTN_export_study = wx.Button(self, wx.ID_ANY, _("Export"), style=wx.BU_EXACTFIT)
		self._BTN_save_selected_studies = wx.Button(self, wx.ID_ANY, _("Save"), style=wx.BU_EXACTFIT)
		self._LCTRL_studies = cReportListCtrl(self, wx.ID_ANY, style=wx.BORDER_NONE | wx.LC_REPORT)
		self._LCTRL_series = cReportListCtrl(self, wx.ID_ANY, style=wx.BORDER_NONE | wx.LC_REPORT)

		self.__set_properties()
		self.__do_layout()

		self.Bind(wx.EVT_BUTTON, self._on_connect_button_pressed, self._BTN_connect)
		self.Bind(wx.EVT_BUTTON, self._on_browse_pacs_button_pressed, self._BTN_browse_pacs)
		self.Bind(wx.EVT_BUTTON, self._on_browse_patient_button_pressed, self._BTN_browse_patient)
		self.Bind(wx.EVT_BUTTON, self._on_export_all_studies_button_pressed, self._BTN_export_all_studies)
		self.Bind(wx.EVT_BUTTON, self._on_browse_study_button_pressed, self._BTN_browse_study)
		self.Bind(wx.EVT_BUTTON, self._on_export_study_button_pressed, self._BTN_export_study)
		self.Bind(wx.EVT_BUTTON, self._on_save_selected_studies_button_pressed, self._BTN_save_selected_studies)
		self.Bind(wx.EVT_LIST_ITEM_SELECTED, self._on_studies_list_item_selected, self._LCTRL_studies)
		# end wxGlade

	def __set_properties(self):
		# begin wxGlade: wxgPACSPluginPnl.__set_properties
		self._TCTRL_host.SetToolTipString(_("Enter the PACS host address."))
		self._TCTRL_port.SetToolTipString(_("Enter the PACS port."))
		self._TCTRL_user.SetToolTipString(_("Enter the PACS user."))
		self._TCTRL_password.SetToolTipString(_("Enter the PACS password. It will not be shown."))
		self._BTN_connect.SetToolTipString(_("Connect to PACS."))
		self._BTN_browse_pacs.SetToolTipString(_("Browse PACS at top level."))
		self._BTN_browse_patient.SetToolTipString(_("Browse overview of studies for this patient."))
		self._BTN_browse_patient.Enable(False)
		self._BTN_export_all_studies.SetToolTipString(_("Copy all studies into export area."))
		self._BTN_export_all_studies.Enable(False)
		self._BTN_browse_study.SetToolTipString(_("Browse topmost selected study."))
		self._BTN_browse_study.Enable(False)
		self._BTN_export_study.SetToolTipString(_("Copy selected studies into export area."))
		self._BTN_export_study.Enable(False)
		self._BTN_save_selected_studies.SetToolTipString(_("Save selected studies to disk."))
		self._BTN_save_selected_studies.Enable(False)
		# end wxGlade

	def __do_layout(self):
		# begin wxGlade: wxgPACSPluginPnl.__do_layout
		__szr_main = wx.BoxSizer(wx.VERTICAL)
		__szr_buttons = wx.BoxSizer(wx.HORIZONTAL)
		__szr_PACS_details = wx.BoxSizer(wx.HORIZONTAL)
		__lbl_host = wx.StaticText(self, wx.ID_ANY, _("Host:"))
		__szr_PACS_details.Add(__lbl_host, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 3)
		__szr_PACS_details.Add(self._TCTRL_host, 1, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 5)
		__lbl_port = wx.StaticText(self, wx.ID_ANY, _("Port:"))
		__szr_PACS_details.Add(__lbl_port, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 3)
		__szr_PACS_details.Add(self._TCTRL_port, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 5)
		__lbl_user = wx.StaticText(self, wx.ID_ANY, _("User:"))
		__szr_PACS_details.Add(__lbl_user, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 3)
		__szr_PACS_details.Add(self._TCTRL_user, 1, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 5)
		__lbl_password = wx.StaticText(self, wx.ID_ANY, _("Password"))
		__szr_PACS_details.Add(__lbl_password, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 3)
		__szr_PACS_details.Add(self._TCTRL_password, 1, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 5)
		__szr_PACS_details.Add(self._BTN_connect, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 0)
		__szr_PACS_details.Add(self._BTN_browse_pacs, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		__szr_main.Add(__szr_PACS_details, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 3)
		__szr_main.Add(self._LBL_PACS_identification, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 3)
		__szr_main.Add(self._LBL_patient_identification, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 3)
		__szr_buttons.Add(self._LBL_no_of_studies, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 3)
		__szr_buttons.Add(self._BTN_browse_patient, 0, wx.RIGHT, 3)
		__szr_buttons.Add(self._BTN_export_all_studies, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 3)
		__lbl_selected_study = wx.StaticText(self, wx.ID_ANY, _("Selected studies:"))
		__szr_buttons.Add(__lbl_selected_study, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 3)
		__szr_buttons.Add(self._BTN_browse_study, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 3)
		__szr_buttons.Add(self._BTN_export_study, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 3)
		__szr_buttons.Add(self._BTN_save_selected_studies, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		__szr_main.Add(__szr_buttons, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 3)
		__szr_main.Add(self._LCTRL_studies, 2, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 3)
		__szr_main.Add(self._LCTRL_series, 3, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 3)
		self.SetSizer(__szr_main)
		__szr_main.Fit(self)
		self.Layout()
		# end wxGlade

	def _on_connect_button_pressed(self, event):  # wxGlade: wxgPACSPluginPnl.<event_handler>
		print "Event handler '_on_connect_button_pressed' not implemented!"
		event.Skip()

	def _on_browse_pacs_button_pressed(self, event):  # wxGlade: wxgPACSPluginPnl.<event_handler>
		print "Event handler '_on_browse_pacs_button_pressed' not implemented!"
		event.Skip()

	def _on_browse_patient_button_pressed(self, event):  # wxGlade: wxgPACSPluginPnl.<event_handler>
		print "Event handler '_on_browse_patient_button_pressed' not implemented!"
		event.Skip()

	def _on_export_all_studies_button_pressed(self, event):  # wxGlade: wxgPACSPluginPnl.<event_handler>
		print "Event handler '_on_export_all_studies_button_pressed' not implemented!"
		event.Skip()

	def _on_browse_study_button_pressed(self, event):  # wxGlade: wxgPACSPluginPnl.<event_handler>
		print "Event handler '_on_browse_study_button_pressed' not implemented!"
		event.Skip()

	def _on_export_study_button_pressed(self, event):  # wxGlade: wxgPACSPluginPnl.<event_handler>
		print "Event handler '_on_export_study_button_pressed' not implemented!"
		event.Skip()

	def _on_save_selected_studies_button_pressed(self, event):  # wxGlade: wxgPACSPluginPnl.<event_handler>
		print "Event handler '_on_save_selected_studies_button_pressed' not implemented!"
		event.Skip()

	def _on_studies_list_item_selected(self, event):  # wxGlade: wxgPACSPluginPnl.<event_handler>
		print "Event handler '_on_studies_list_item_selected' not implemented!"
		event.Skip()

# end of class wxgPACSPluginPnl
