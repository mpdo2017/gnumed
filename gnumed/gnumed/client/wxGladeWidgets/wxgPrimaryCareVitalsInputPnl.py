# -*- coding: UTF-8 -*-
#
# generated by wxGlade
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
import wx.lib.analogclock
import wx.lib.hyperlink
import wx.lib.masked
# end wxGlade


class wxgPrimaryCareVitalsInputPnl(wx.Panel):
	def __init__(self, *args, **kwds):
		# begin wxGlade: wxgPrimaryCareVitalsInputPnl.__init__
		kwds["style"] = kwds.get("style", 0) | wx.TAB_TRAVERSAL
		wx.Panel.__init__(self, *args, **kwds)
		self._TCTRL_RR_left = wx.lib.masked.TextCtrl(self, wx.ID_ANY, "")
		self._LNK_SI = wx.lib.hyperlink.HyperLinkCtrl(self, wx.ID_ANY, _("Schock index"), style=wx.TE_CENTRE | wx.TE_READONLY)
		self._TCTRL_RR_right = wx.lib.masked.TextCtrl(self, wx.ID_ANY, "")
		self._LBL_SI_value = wx.StaticText(self, wx.ID_ANY, _("<SI>"), style=wx.ALIGN_CENTER)
		self._TCTRL_pulse = wx.TextCtrl(self, wx.ID_ANY, "")
		self._RBTN_rhythmic = wx.RadioButton(self, wx.ID_ANY, _("rhythmic"))
		self._RBTN_arrhythmic = wx.RadioButton(self, wx.ID_ANY, _("arrhythmic"))
		self._TCTRL_pulse_quality = wx.TextCtrl(self, wx.ID_ANY, "")
		self._TCTRL_temp_periph = wx.TextCtrl(self, wx.ID_ANY, "")
		self._TCTRL_temp_rect = wx.TextCtrl(self, wx.ID_ANY, "")
		self._RBTN_centigrade = wx.RadioButton(self, wx.ID_ANY, _(u"\u00b0C"), style=wx.RB_GROUP)
		self._RBTN_fahrenheit = wx.RadioButton(self, wx.ID_ANY, _(u"\u00b0F"))
		self._TCTRL_respiration = wx.TextCtrl(self, wx.ID_ANY, "")
		self._TCTRL_height = wx.TextCtrl(self, wx.ID_ANY, "")
		self._LBL_last_height = wx.StaticText(self, wx.ID_ANY, _("<last height>"))
		self._LNK_BMI = wx.lib.hyperlink.HyperLinkCtrl(self, wx.ID_ANY, _("BMI"), style=wx.TE_CENTRE | wx.TE_READONLY)
		self._TCTRL_weight = wx.TextCtrl(self, wx.ID_ANY, "")
		self._LBL_last_weight = wx.StaticText(self, wx.ID_ANY, _("<last weight>"))
		self._LBL_BMI_value = wx.StaticText(self, wx.ID_ANY, _("<BMI>"), style=wx.ALIGN_CENTER)
		self._TCTRL_waist = wx.TextCtrl(self, wx.ID_ANY, "")
		self._LBL_last_waist = wx.StaticText(self, wx.ID_ANY, _("<last waist>"))
		self._clock = wx.lib.analogclock.AnalogClock(self, wx.ID_ANY)

		self.__set_properties()
		self.__do_layout()
		# end wxGlade

	def __set_properties(self):
		# begin wxGlade: wxgPrimaryCareVitalsInputPnl.__set_properties
		self._TCTRL_RR_left.SetToolTip(_("RR measured on the left arm."))
		self._LNK_SI.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
		self._LNK_SI.SetToolTip(_("SI = Pulse / RR (syst)\n\n  0.4-0.7 = normal\n  >1 = critical"))
		self._TCTRL_RR_right.SetToolTip(_("RR measured on the right arm."))
		self._TCTRL_pulse.SetToolTip(_("Heart rate in beats per minute."))
		self._RBTN_rhythmic.SetValue(1)
		self._TCTRL_pulse_quality.SetToolTip(_("The quality of the pulse.\nLet's not forget good old GP medicine !"))
		self._TCTRL_temp_periph.SetToolTip(_("Peripheral body temperature:\n axillar\n oral\n forehead\n tympanic"))
		self._TCTRL_temp_rect.SetToolTip(_("\"Core\" body temperature:\n rectal\n intravascular"))
		self._RBTN_centigrade.SetValue(1)
		self._TCTRL_respiration.SetToolTip(_("Respiration rate."))
		self._TCTRL_height.SetToolTip(_("Current height in cm."))
		self._LNK_BMI.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
		self._LNK_BMI.SetToolTip(_(u"Body Mass Index.\n\nBMI = weight / height\u00b2"))
		self._TCTRL_weight.SetToolTip(_("Current weight in gram or kg.\n\nCutoff is 500:\n <500: kg\n >500: g"))
		self._TCTRL_waist.SetToolTip(_("Current waist circumference in cm."))
		self._clock.SetMinSize((100, 100))
		# end wxGlade

	def __do_layout(self):
		# begin wxGlade: wxgPrimaryCareVitalsInputPnl.__do_layout
		__szr_main = wx.BoxSizer(wx.VERTICAL)
		__gzsr_main = wx.FlexGridSizer(12, 3, 2, 4)
		__szr_waist = wx.BoxSizer(wx.HORIZONTAL)
		__szr_weight = wx.BoxSizer(wx.HORIZONTAL)
		__szr_height = wx.BoxSizer(wx.HORIZONTAL)
		__szr_respiration = wx.BoxSizer(wx.HORIZONTAL)
		__szr_temp_details = wx.BoxSizer(wx.HORIZONTAL)
		__szr_pulse_details = wx.BoxSizer(wx.HORIZONTAL)
		__szr_pulse = wx.BoxSizer(wx.HORIZONTAL)
		__szr_RR_right = wx.BoxSizer(wx.HORIZONTAL)
		__szr_RR = wx.BoxSizer(wx.HORIZONTAL)
		__gzsr_main.Add((20, 20), 0, wx.EXPAND, 0)
		__lbl_vitals = wx.StaticText(self, wx.ID_ANY, _("Vitals"))
		__lbl_vitals.SetForegroundColour(wx.Colour(95, 159, 159))
		__gzsr_main.Add(__lbl_vitals, 0, wx.ALIGN_CENTER, 0)
		__gzsr_main.Add((20, 20), 0, wx.EXPAND, 0)
		__lbl_RR_left = wx.StaticText(self, wx.ID_ANY, _("RR left"))
		__gzsr_main.Add(__lbl_RR_left, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
		__szr_RR.Add(self._TCTRL_RR_left, 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND | wx.RIGHT, 3)
		__lbl_mmHg_left = wx.StaticText(self, wx.ID_ANY, _("mmHg"))
		__szr_RR.Add(__lbl_mmHg_left, 0, wx.ALIGN_CENTER_VERTICAL, 15)
		__gzsr_main.Add(__szr_RR, 1, wx.EXPAND, 0)
		__gzsr_main.Add(self._LNK_SI, 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 15)
		__lbl_RR_right = wx.StaticText(self, wx.ID_ANY, _("RR right"))
		__gzsr_main.Add(__lbl_RR_right, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
		__szr_RR_right.Add(self._TCTRL_RR_right, 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND | wx.RIGHT, 3)
		__lbl_mmHg_right = wx.StaticText(self, wx.ID_ANY, _("mmHg"))
		__szr_RR_right.Add(__lbl_mmHg_right, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		__gzsr_main.Add(__szr_RR_right, 1, wx.EXPAND, 0)
		__gzsr_main.Add(self._LBL_SI_value, 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 15)
		__lbl_pulse = wx.StaticText(self, wx.ID_ANY, _("Pulse"))
		__gzsr_main.Add(__lbl_pulse, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
		__szr_pulse.Add(self._TCTRL_pulse, 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND | wx.RIGHT, 3)
		__lbl_bpm = wx.StaticText(self, wx.ID_ANY, _("/min"))
		__szr_pulse.Add(__lbl_bpm, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 10)
		__szr_pulse.Add(self._RBTN_rhythmic, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 3)
		__szr_pulse.Add(self._RBTN_arrhythmic, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		__gzsr_main.Add(__szr_pulse, 1, wx.EXPAND, 0)
		__gzsr_main.Add((20, 20), 0, wx.EXPAND, 0)
		__gzsr_main.Add((20, 20), 0, wx.EXPAND, 0)
		__szr_pulse_details.Add(self._TCTRL_pulse_quality, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		__gzsr_main.Add(__szr_pulse_details, 1, wx.EXPAND, 0)
		__gzsr_main.Add((20, 20), 0, wx.EXPAND, 0)
		__lbl_temp = wx.StaticText(self, wx.ID_ANY, _("Temp"))
		__gzsr_main.Add(__lbl_temp, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
		__szr_temp_details.Add(self._TCTRL_temp_periph, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 3)
		__lbl_temp_periph = wx.StaticText(self, wx.ID_ANY, _("(axill./oral/...)"))
		__szr_temp_details.Add(__lbl_temp_periph, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 10)
		__szr_temp_details.Add(self._TCTRL_temp_rect, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 3)
		__lbl_temp_rect = wx.StaticText(self, wx.ID_ANY, _("(rectal)"))
		__szr_temp_details.Add(__lbl_temp_rect, 0, wx.ALIGN_CENTER_VERTICAL, 3)
		__szr_temp_details.Add((20, 20), 1, wx.EXPAND, 0)
		__szr_temp_details.Add(self._RBTN_centigrade, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 3)
		__szr_temp_details.Add(self._RBTN_fahrenheit, 0, wx.ALIGN_CENTER_VERTICAL, 3)
		__gzsr_main.Add(__szr_temp_details, 1, wx.EXPAND, 0)
		__gzsr_main.Add((20, 20), 0, wx.EXPAND, 0)
		__lbl_resp_rate = wx.StaticText(self, wx.ID_ANY, _("Resp"))
		__gzsr_main.Add(__lbl_resp_rate, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
		__szr_respiration.Add(self._TCTRL_respiration, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 3)
		__lbl_units_respiration = wx.StaticText(self, wx.ID_ANY, _("/min"))
		__szr_respiration.Add(__lbl_units_respiration, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		__gzsr_main.Add(__szr_respiration, 1, wx.EXPAND, 0)
		__gzsr_main.Add((20, 20), 0, wx.EXPAND, 0)
		__gzsr_main.Add((20, 20), 0, wx.EXPAND, 0)
		__lbl_figure = wx.StaticText(self, wx.ID_ANY, _("Figure"))
		__lbl_figure.SetForegroundColour(wx.Colour(95, 159, 159))
		__gzsr_main.Add(__lbl_figure, 0, wx.ALIGN_CENTER, 0)
		__gzsr_main.Add((20, 20), 0, wx.EXPAND, 0)
		__lbl_height = wx.StaticText(self, wx.ID_ANY, _("Height"))
		__gzsr_main.Add(__lbl_height, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
		__szr_height.Add(self._TCTRL_height, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 3)
		__lbl_unit_height = wx.StaticText(self, wx.ID_ANY, _("cm"))
		__szr_height.Add(__lbl_unit_height, 0, wx.ALIGN_CENTER_VERTICAL, 10)
		__szr_height.Add((20, 20), 1, wx.EXPAND, 0)
		__szr_height.Add(self._LBL_last_height, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		__gzsr_main.Add(__szr_height, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		__gzsr_main.Add(self._LNK_BMI, 0, wx.ALIGN_CENTER | wx.EXPAND, 15)
		__lbl_weight = wx.StaticText(self, wx.ID_ANY, _("Weight"))
		__gzsr_main.Add(__lbl_weight, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 3)
		__szr_weight.Add(self._TCTRL_weight, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 3)
		__lbl_unit_weight = wx.StaticText(self, wx.ID_ANY, _("g or kg"))
		__szr_weight.Add(__lbl_unit_weight, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		__szr_weight.Add((20, 20), 1, wx.EXPAND, 0)
		__szr_weight.Add(self._LBL_last_weight, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		__gzsr_main.Add(__szr_weight, 1, wx.EXPAND, 0)
		__gzsr_main.Add(self._LBL_BMI_value, 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 15)
		__lbl_waist = wx.StaticText(self, wx.ID_ANY, _("Waist"))
		__gzsr_main.Add(__lbl_waist, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
		__szr_waist.Add(self._TCTRL_waist, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 3)
		__lbl_unit_waist = wx.StaticText(self, wx.ID_ANY, _("cm"))
		__szr_waist.Add(__lbl_unit_waist, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		__szr_waist.Add((20, 20), 1, wx.EXPAND, 0)
		__szr_waist.Add(self._LBL_last_waist, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		__gzsr_main.Add(__szr_waist, 1, wx.EXPAND, 0)
		__gzsr_main.Add((20, 20), 0, wx.EXPAND, 0)
		__gzsr_main.Add((20, 20), 0, wx.EXPAND, 0)
		__gzsr_main.Add(self._clock, 1, wx.ALIGN_CENTER, 0)
		__gzsr_main.Add((20, 20), 0, wx.EXPAND, 0)
		__gzsr_main.AddGrowableCol(1)
		__szr_main.Add(__gzsr_main, 1, wx.EXPAND, 0)
		self.SetSizer(__szr_main)
		__szr_main.Fit(self)
		self.Layout()
		# end wxGlade

# end of class wxgPrimaryCareVitalsInputPnl
