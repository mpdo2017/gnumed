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


class wxgExternalIDEditAreaPnl(wx.ScrolledWindow):
	def __init__(self, *args, **kwds):
		# begin wxGlade: wxgExternalIDEditAreaPnl.__init__
		kwds["style"] = kwds.get("style", 0) | wx.BORDER_NONE | wx.TAB_TRAVERSAL
		wx.ScrolledWindow.__init__(self, *args, **kwds)
		from Gnumed.wxpython.gmDemographicsWidgets import cExternalIDTypePhraseWheel
		self._PRW_type = cExternalIDTypePhraseWheel(self, wx.ID_ANY, "")
		self._TCTRL_value = wx.TextCtrl(self, wx.ID_ANY, "")
		from Gnumed.wxpython.gmDemographicsWidgets import cExternalIDIssuerPhraseWheel
		self._PRW_issuer = cExternalIDIssuerPhraseWheel(self, wx.ID_ANY, "")
		self._TCTRL_comment = wx.TextCtrl(self, wx.ID_ANY, "")

		self.__set_properties()
		self.__do_layout()
		# end wxGlade

	def __set_properties(self):
		# begin wxGlade: wxgExternalIDEditAreaPnl.__set_properties
		self.SetScrollRate(10, 10)
		self._TCTRL_value.SetToolTip(_("Enter the actual ID (number, identifier, ...) here."))
		self._TCTRL_comment.SetToolTip(_("Enter a comment on this external ID."))
		# end wxGlade

	def __do_layout(self):
		# begin wxGlade: wxgExternalIDEditAreaPnl.__do_layout
		_gszr_main = wx.FlexGridSizer(4, 2, 3, 5)
		__LBL_type = wx.StaticText(self, wx.ID_ANY, _("ID Type"))
		_gszr_main.Add(__LBL_type, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		_gszr_main.Add(self._PRW_type, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		__LBL_value = wx.StaticText(self, wx.ID_ANY, _("Value"))
		_gszr_main.Add(__LBL_value, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		_gszr_main.Add(self._TCTRL_value, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		__LBL_issuer = wx.StaticText(self, wx.ID_ANY, _("Issuer"))
		_gszr_main.Add(__LBL_issuer, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		_gszr_main.Add(self._PRW_issuer, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		__LBL_comment = wx.StaticText(self, wx.ID_ANY, _("Comment"))
		_gszr_main.Add(__LBL_comment, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		_gszr_main.Add(self._TCTRL_comment, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		self.SetSizer(_gszr_main)
		_gszr_main.Fit(self)
		_gszr_main.AddGrowableCol(1)
		self.Layout()
		# end wxGlade

# end of class wxgExternalIDEditAreaPnl
