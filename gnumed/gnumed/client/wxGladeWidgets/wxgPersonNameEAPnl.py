# -*- coding: UTF-8 -*-
#
# generated by wxGlade
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class wxgPersonNameEAPnl(wx.ScrolledWindow):
	def __init__(self, *args, **kwds):
		# begin wxGlade: wxgPersonNameEAPnl.__init__
		kwds["style"] = kwds.get("style", 0) | wx.BORDER_NONE | wx.TAB_TRAVERSAL
		wx.ScrolledWindow.__init__(self, *args, **kwds)
		from Gnumed.wxpython.gmDemographicsWidgets import cFirstnamePhraseWheel
		self._PRW_firstname = cFirstnamePhraseWheel(self, wx.ID_ANY, "")
		from Gnumed.wxpython.gmDemographicsWidgets import cLastnamePhraseWheel
		self._PRW_lastname = cLastnamePhraseWheel(self, wx.ID_ANY, "")
		from Gnumed.wxpython.gmDemographicsWidgets import cNicknamePhraseWheel
		self._PRW_nick = cNicknamePhraseWheel(self, wx.ID_ANY, "")
		self._TCTRL_comment = wx.TextCtrl(self, wx.ID_ANY, "")
		self._CHBOX_active = wx.CheckBox(self, wx.ID_ANY, _("Active name"))

		self.__set_properties()
		self.__do_layout()
		# end wxGlade

	def __set_properties(self):
		# begin wxGlade: wxgPersonNameEAPnl.__set_properties
		self.SetScrollRate(10, 10)
		self._TCTRL_comment.SetToolTip(_("Enter a comment relevant to this name (such as \"before marriage\")."))
		self._CHBOX_active.SetToolTip(_("Check this to make this the currently active name."))
		# end wxGlade

	def __do_layout(self):
		# begin wxGlade: wxgPersonNameEAPnl.__do_layout
		_gszr_main = wx.FlexGridSizer(5, 2, 3, 5)
		__LBL_firstname = wx.StaticText(self, wx.ID_ANY, _("First name"))
		_gszr_main.Add(__LBL_firstname, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		_gszr_main.Add(self._PRW_firstname, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		__LBL_lastname = wx.StaticText(self, wx.ID_ANY, _("Last name"))
		_gszr_main.Add(__LBL_lastname, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		_gszr_main.Add(self._PRW_lastname, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		__LBL_preferred = wx.StaticText(self, wx.ID_ANY, _("Nick name"))
		_gszr_main.Add(__LBL_preferred, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		_gszr_main.Add(self._PRW_nick, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		__LBL_comment = wx.StaticText(self, wx.ID_ANY, _("Comment"))
		_gszr_main.Add(__LBL_comment, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		_gszr_main.Add(self._TCTRL_comment, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		_gszr_main.Add((20, 20), 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		_gszr_main.Add(self._CHBOX_active, 0, wx.ALIGN_CENTER_VERTICAL, 10)
		self.SetSizer(_gszr_main)
		_gszr_main.Fit(self)
		_gszr_main.AddGrowableCol(1)
		self.Layout()
		# end wxGlade

# end of class wxgPersonNameEAPnl
