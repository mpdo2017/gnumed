"""GNUmed billing handling widgets.
"""
#================================================================
__author__ = "Karsten Hilbert <Karsten.Hilbert@gmx.net>"

import logging
import sys


import wx


if __name__ == '__main__':
	sys.path.insert(0, '../../')
from Gnumed.pycommon import gmTools
from Gnumed.pycommon import gmDateTime
from Gnumed.pycommon import gmMatchProvider
from Gnumed.pycommon import gmDispatcher
from Gnumed.pycommon import gmPG2
#gmI18N, gmPrinting, gmCfg2, gmNetworkTools

from Gnumed.business import gmBilling
from Gnumed.business import gmPerson
from Gnumed.business import gmStaff
# gmSurgery

from Gnumed.wxpython import gmListWidgets
from Gnumed.wxpython import gmRegetMixin
from Gnumed.wxpython import gmPhraseWheel
from Gnumed.wxpython import gmGuiHelpers
from Gnumed.wxpython import gmEditArea
from Gnumed.wxpython import gmPersonContactWidgets


_log = logging.getLogger('gm.ui')

#================================================================
def manage_billables(parent=None):

	if parent is None:
		parent = wx.GetApp().GetTopWindow()
	#------------------------------------------------------------
#	def edit(substance=None):
#		return edit_consumable_substance(parent = parent, substance = substance, single_entry = (substance is not None))
	#------------------------------------------------------------
	def delete(billable):
		if billable.is_in_use:
			gmDispatcher.send(signal = 'statustext', msg = _('Cannot delete this billable item. It is in use.'), beep = True)
			return False
		return gmBillling.delete_billable(pk_billable = billable['pk_billable'])
	#------------------------------------------------------------
	def get_tooltip(item):
		if item is None:
			return None
		return item.format()
	#------------------------------------------------------------
	def refresh(lctrl):
		billables = gmBilling.get_billables()
		items = [ [
			b['billable_code'],
			b['billable_description'],
			u'%s %s' % (b['raw_amount'], b['currency']),
			u'%s (%s)' % (b['catalog_short'], b['catalog_version']),
			gmTools.coalesce(b['comment'], u''),
			b['pk_billable']
		] for b in billables ]
		lctrl.set_string_items(items)
		lctrl.set_data(billables)
	#------------------------------------------------------------
	msg = _('\nThese are the items for billing registered with GNUmed.\n')

	gmListWidgets.get_choices_from_list (
		parent = parent,
		msg = msg,
		caption = _('Showing billable items.'),
		columns = [_('Code'), _('Description'), _('Value'), _('Catalog'), _('Comment'), u'#'],
		single_selection = True,
		#new_callback = edit,
		#edit_callback = edit,
		delete_callback = delete,
		refresh_callback = refresh
		#, right_extra_button = (
		#	_('Catalogs (WWW)'),
		#	_('Browse billing catalogs on the web'),
		#	browse_catalogs
		#)
		, list_tooltip_callback = get_tooltip
	)

#================================================================
class cBillablePhraseWheel(gmPhraseWheel.cPhraseWheel):

	def __init__(self, *args, **kwargs):
		gmPhraseWheel.cPhraseWheel.__init__(self, *args, **kwargs)
		query = u"""
			SELECT -- DISTINCT ON (label)
				r_vb.pk_billable
					AS data,
				r_vb.billable_code || ': ' || r_vb.billable_description || ' (' || r_vb.catalog_short || ' - ' || r_vb.catalog_version || ')'
					AS list_label,
				r_vb.billable_code || ' (' || r_vb.catalog_short || ' - ' || r_vb.catalog_version || ')'
					AS field_label
			FROM
				ref.v_billables r_vb
			WHERE
				r_vb.active
					AND (
						r_vb.billable_code %(fragment_condition)s
							OR
						r_vb.billable_description %(fragment_condition)s
					)
			ORDER BY list_label
			LIMIT 20
		"""
		mp = gmMatchProvider.cMatchProvider_SQL2(queries = query)
		mp.setThresholds(1, 2, 4)
		self.matcher = mp
	#------------------------------------------------------------
	def _data2instance(self):
		return gmBilling.cBillable(aPK_obj = self._data.values()[0]['data'])
	#------------------------------------------------------------
	def _get_data_tooltip(self):
		if self.GetData() is None:
			return None
		billable = gmBilling.cBillable(aPK_obj = self._data.values()[0]['data'])
		return billable.format()
	#------------------------------------------------------------
	def set_from_instance(self, instance):
		val = u'%s (%s - %s)' % (
			instance['billable_code'],
			instance['catalog_short'],
			instance['catalog_version']
		)
		self.SetText(value = val, data = instance['pk_billable'])
	#------------------------------------------------------------
	def set_from_pk(self, pk):
		self.set_from_instance(gmBilling.cBillable(aPK_obj = pk))

#================================================================
# per-patient bill related widgets
#----------------------------------------------------------------
def manage_bills(parent=None, pk_patient=None):

	if parent is None:
		parent = wx.GetApp().GetTopWindow()

	if pk_patient is None:
		pk_patient = gmPerson.gmCurrentPatient().ID
	#------------------------------------------------------------
	# edit
	#------------------------------------------------------------
	def create_invoice(bill):
		if bill is None:
			return
		print "should create invoice from bill:"
		print bill
	#------------------------------------------------------------
	def show_pdf(bill):
		if bill is None:
			return
		print "should find PDF and display it for bill:"
		print bill
	#------------------------------------------------------------
	def delete(bill):
		do_it = gmGuiHelpers.gm_show_question (
			question = _('Do you truly want to irrevocably delete this bill ?'),
			title = _('Delete bill')
		)
		if not do_it:
			return False
		return gmBillling.delete_bill(pk_bill = bill['pk_bill'])
	#------------------------------------------------------------
	def get_tooltip(item):
		if item is None:
			return None
		return item.format()
	#------------------------------------------------------------
	def refresh(lctrl):
		bills = gmBilling.get_bills(pk_patient = pk_patient)
		items = []
		for b in bills:
			if b['close_date'] is None:
				close_date = u''
			else:
				close_date = gmDateTime.pydt_strftime(b['close_date'], '%Y %b %d')
			items.append([
				close_date,
				b['invoice_id'],
				u'%s %s' % (b['total_amount'], b['currency']),
				b['pk_bill']
			])
#		items = [ [
#			gmDateTime.pydt_strftime(b['close_date'], '%Y %b %d'),
#			b['invoice_id'],
#			u'%s %s' % (b['total_amount'], b['currency']),
#			b['pk_bill']
#		] for b in bills ]
		lctrl.set_string_items(items)
		lctrl.set_data(bills)
	#------------------------------------------------------------
	gmListWidgets.get_choices_from_list (
		parent = parent,
		#msg = msg,
		caption = _('Showing bills.'),
		columns = [_('Close date'), _('Invoice ID'), _('Value'), u'#'],
		single_selection = True,
		#new_callback = edit,
		#edit_callback = edit,
		delete_callback = delete,
		refresh_callback = refresh,
		left_extra_button = (
			_('Create invoice'),
			_('Create PDF invoice from bill'),
			create_invoice
		),
		middle_extra_button = (
			_('Show PDF'),
			_('Show the corresponding invoice PDF'),
			show_pdf
		),
		list_tooltip_callback = get_tooltip
	)

#================================================================
# per-patient bill items related widgets
#----------------------------------------------------------------
def edit_bill_item(parent=None, bill_item=None, single_entry=False):

	if bill_item is not None:
		if bill_item.is_in_use:
			gmDispatcher.send(signal = 'statustext', msg = _('Cannot edit already invoiced bill item.'), beep = True)
			return False

	ea = cBillItemEAPnl(parent = parent, id = -1)
	ea.data = bill_item
	ea.mode = gmTools.coalesce(bill_item, 'new', 'edit')
	dlg = gmEditArea.cGenericEditAreaDlg2(parent = parent, id = -1, edit_area = ea, single_entry = single_entry)
	dlg.SetTitle(gmTools.coalesce(bill_item, _('Adding new bill item'), _('Editing bill item')))
	if dlg.ShowModal() == wx.ID_OK:
		dlg.Destroy()
		return True
	dlg.Destroy()
	return False
#----------------------------------------------------------------
def manage_bill_items(parent=None, pk_patient=None):

	if parent is None:
		parent = wx.GetApp().GetTopWindow()
	#------------------------------------------------------------
	def edit(item=None):
		return edit_bill_item(parent = parent, bill_item = item, single_entry = (item is not None))
	#------------------------------------------------------------
	def delete(item):
		if item.is_in_use is not None:
			gmDispatcher.send(signal = 'statustext', msg = _('Cannot delete already invoiced bill items.'), beep = True)
			return False
		gmBilling.delete_bill_item(pk_bill_item = item['pk_bill_item'])
		return True
	#------------------------------------------------------------
	def refresh(lctrl):
		b_items = gmBilling.get_bill_items(pk_patient = pk_patient)
		items = [ [
			gmDateTime.pydt_strftime(b['date_to_bill'], '%x', accuracy = gmDateTime.acc_days),
			b['unit_count'],
			u'%s: %s%s' % (b['billable_code'], b['billable_description'], gmTools.coalesce(b['item_detail'], u'', u' - %s')),
			u'%s %s (%s x %sx%s)' % (
				b['final_amount'],
				b['currency'],
				b['unit_count'],
				b['net_amount_per_unit'],
				b['amount_multiplier']
			),
			u'%s %s (%s%%)' % (
				b['vat'],
				b['currency'],
				b['vat_multiplier'] * 100
			),
			u'%s (%s)' % (b['catalog_short'], b['catalog_version']),
			b['pk_bill_item']
		] for b in b_items ]
		lctrl.set_string_items(items)
		lctrl.set_data(b_items)
	#------------------------------------------------------------
	gmListWidgets.get_choices_from_list (
		parent = parent,
		#msg = msg,
		caption = _('Showing bill items.'),
		columns = [_('Date'), _('Count'), _('Description'), _('Value'), _('VAT'), _('Catalog'), u'#'],
		single_selection = True,
		new_callback = edit,
		edit_callback = edit,
		delete_callback = delete,
		refresh_callback = refresh
	)

#------------------------------------------------------------
class cPersonBillItemsManagerPnl(gmListWidgets.cGenericListManagerPnl):
	"""A list for managing a patient's bill items.

	Does NOT act on/listen to the current patient.
	"""
	def __init__(self, *args, **kwargs):

		try:
			self.__identity = kwargs['identity']
			del kwargs['identity']
		except KeyError:
			self.__identity = None

		gmListWidgets.cGenericListManagerPnl.__init__(self, *args, **kwargs)

		self.new_callback = self._add_item
		self.edit_callback = self._edit_item
		self.delete_callback = self._del_item
		self.refresh_callback = self.refresh

		self.__show_non_invoiced_only = True

		self.__init_ui()
		self.refresh()
	#--------------------------------------------------------
	# external API
	#--------------------------------------------------------
	def refresh(self, *args, **kwargs):
		if self.__identity is None:
			self._LCTRL_items.set_string_items()
			return

		b_items = gmBilling.get_bill_items(pk_patient = self.__identity.ID, non_invoiced_only = self.__show_non_invoiced_only)
		items = [ [
			gmDateTime.pydt_strftime(b['date_to_bill'], '%x', accuracy = gmDateTime.acc_days),
			b['unit_count'],
			u'%s: %s%s' % (b['billable_code'], b['billable_description'], gmTools.coalesce(b['item_detail'], u'', u' - %s')),
			u'%s %s' % (
				b['final_amount'],
				b['currency']
			),
			u'%s %s (%s%%)' % (
				b['vat'],
				b['currency'],
				b['vat_multiplier'] * 100
			),
			u'%s (%s)' % (b['catalog_short'], b['catalog_version']),
			u'%s x %s x %s' % (
				b['unit_count'],
				b['net_amount_per_unit'],
				b['amount_multiplier']
			),
			gmTools.coalesce(b['pk_bill'], gmTools.u_diameter),
			b['pk_encounter_to_bill'],
			b['pk_bill_item']
		] for b in b_items ]

		self._LCTRL_items.set_string_items(items = items)
		self._LCTRL_items.set_column_widths()
		self._LCTRL_items.set_data(data = b_items)
	#--------------------------------------------------------
	# internal helpers
	#--------------------------------------------------------
	def __init_ui(self):
		self._LCTRL_items.set_columns(columns = [
			_('Charge date'),
			_('Count'),
			_('Description'),
			_('Value'),
			_('VAT'),
			_('Catalog'),
			_('Count x Value x Factor'),
			_('Invoice'),
			_('Encounter'),
			u'#'
		])
#		self.left_extra_button = (
#			_('Select pending'),
#			_('Select non-invoiced - pending - items.'),
#			self._select_pending_items
#		)
		self.left_extra_button = (
			_('Invoice selected'),
			_('Create invoice from selected items.'),
			self._invoice_selected_items
		)
		self.middle_extra_button = (
			_('Browse bills'),
			_('Browse bills of this patient.'),
			self._browse_bills
		)
		self.right_extra_button = (
			_('Browse billables'),
			_('Browse list of billables.'),
			self._browse_billables
		)
	#--------------------------------------------------------
	def _add_item(self):
		return edit_bill_item(parent = self, bill_item = None, single_entry = False)
	#--------------------------------------------------------
	def _edit_item(self, bill_item):
		return edit_bill_item(parent = self, bill_item = bill_item, single_entry = True)
	#--------------------------------------------------------
	def _del_item(self, item):
		if item['pk_bill'] is not None:
			gmDispatcher.send(signal = 'statustext', msg = _('Cannot delete already invoiced bill items.'), beep = True)
			return False
		go_ahead = gmGuiHelpers.gm_show_question (
			_(	'Do you really want to delete this\n'
				'bill item from the patient ?'),
			_('Deleting bill item')
		)
		if not go_ahead:
			return False
		gmBilling.delete_bill_item(pk_bill_item = item['pk_bill_item'])
		return True
	#--------------------------------------------------------
	def _select_pending_items(self, item):
		pass
	#--------------------------------------------------------
	def _invoice_selected_items(self, item):
		bill_items = self._LCTRL_items.get_selected_item_data()
		if len(bill_items) == 0:
			return

		# any item already invoiced ?
		for item in bill_items:
			if item['pk_bill'] is not None:
				gmGuiHelpers.gm_show_warning (
					aTitle = _('Checking invoice items'),
					aMessage = _(
						'This item is already invoiced:\n'
						'\n'
						'%s\n'
						'\n'
						'Cannot put it on a second bill.'
					) % item.format()
				)
				return

		# create bill
		bill = gmBilling.create_bill(invoice_id = gmBilling.get_invoice_id(pk_patient = self.__identity.ID))
		adrs = self.__identity.get_addresses(address_type = u'billing')
		if len(adrs) == 0:
			adr = gmPersonContactWidgets.select_address(missing = u'billing', person = self.__identity)
			if adr is not None:
				bill['pk_receiver_address'] = adr['pk_lnk_person_org_address']
		else:
			bill['pk_receiver_address'] = adrs[0]['pk_lnk_person_org_address']
		bill.save()

		conn = gmPG2.get_connection(readonly = False)

		# add items
		for item in bill_items:
			item['pk_bill'] = bill['pk_bill']
			item.save(conn = conn)

		conn.commit()

		# cannot create invoice if no receiver address
		if bill['pk_receiver_address'] is None:
			gmGuiHelpers.gm_show_warning (
				aTitle = _('Creating bill'),
				aMessage = _(
					'Cannot create invoice from bill.\n'
					'\n'
					'There is no receiver address.'
				)
			)
			return

		# find 

	#--------------------------------------------------------
	def _browse_billables(self, item):
		manage_billables(parent = self)
		return False
	#--------------------------------------------------------
	def _browse_bills(self, item):
		manage_bills(parent = self, pk_patient = self.__identity.ID)
	#--------------------------------------------------------
	# properties
	#--------------------------------------------------------
	def _get_identity(self):
		return self.__identity

	def _set_identity(self, identity):
		self.__identity = identity
		self.refresh()

	identity = property(_get_identity, _set_identity)
	#--------------------------------------------------------
	def _get_show_non_invoiced_only(self):
		return self.__show_non_invoiced_only

	def _set_show_non_invoiced_only(self, value):
		self.__show_non_invoiced_only = value
		self.refresh()

	show_non_invoiced_only = property(_get_show_non_invoiced_only, _set_show_non_invoiced_only)

#------------------------------------------------------------
from Gnumed.wxGladeWidgets import wxgBillItemEAPnl

class cBillItemEAPnl(wxgBillItemEAPnl.wxgBillItemEAPnl, gmEditArea.cGenericEditAreaMixin):

	def __init__(self, *args, **kwargs):

		try:
			data = kwargs['bill_item']
			del kwargs['bill_item']
		except KeyError:
			data = None

		wxgBillItemEAPnl.wxgBillItemEAPnl.__init__(self, *args, **kwargs)
		gmEditArea.cGenericEditAreaMixin.__init__(self)

		self.mode = 'new'
		self.data = data
		if data is not None:
			self.mode = 'edit'

		self.__init_ui()
	#----------------------------------------------------------------
	def __init_ui(self):
		self._PRW_encounter.set_context(context = 'patient', val = gmPerson.gmCurrentPatient().ID)
		self._PRW_billable.add_callback_on_selection(self._on_billable_selected)
	#----------------------------------------------------------------
	# generic Edit Area mixin API
	#----------------------------------------------------------------
	def _valid_for_save(self):

		validity = True

		if self._TCTRL_factor.GetValue().strip() == u'':
			validity = False
			self.display_tctrl_as_valid(tctrl = self._TCTRL_factor, valid = False)
			self._TCTRL_factor.SetFocus()
		else:
			converted, factor = gmTools.input2decimal(self._TCTRL_factor.GetValue())
			if not converted:
				validity = False
				self.display_tctrl_as_valid(tctrl = self._TCTRL_factor, valid = False)
				self._TCTRL_factor.SetFocus()
			else:
				self.display_tctrl_as_valid(tctrl = self._TCTRL_factor, valid = True)

		if self._TCTRL_amount.GetValue().strip() == u'':
			validity = False
			self.display_tctrl_as_valid(tctrl = self._TCTRL_amount, valid = False)
			self._TCTRL_amount.SetFocus()
		else:
			converted, factor = gmTools.input2decimal(self._TCTRL_amount.GetValue())
			if not converted:
				validity = False
				self.display_tctrl_as_valid(tctrl = self._TCTRL_amount, valid = False)
				self._TCTRL_amount.SetFocus()
			else:
				self.display_tctrl_as_valid(tctrl = self._TCTRL_amount, valid = True)

		if self._TCTRL_count.GetValue().strip() == u'':
			validity = False
			self.display_tctrl_as_valid(tctrl = self._TCTRL_count, valid = False)
			self._TCTRL_count.SetFocus()
		else:
			converted, factor = gmTools.input2decimal(self._TCTRL_count.GetValue())
			if not converted:
				validity = False
				self.display_tctrl_as_valid(tctrl = self._TCTRL_count, valid = False)
				self._TCTRL_count.SetFocus()
			else:
				self.display_tctrl_as_valid(tctrl = self._TCTRL_count, valid = True)

		if self._PRW_date.is_valid_timestamp(allow_empty = True):
			self._PRW_date.display_as_valid(True)
		else:
			validity = False
			self._PRW_date.display_as_valid(False)
			self._PRW_date.SetFocus()

		if self._PRW_encounter.GetData() is None:
			validity = False
			self._PRW_encounter.display_as_valid(False)
			self._PRW_encounter.SetFocus()
		else:
			self._PRW_encounter.display_as_valid(True)

		if self._PRW_billable.GetData() is None:
			validity = False
			self._PRW_billable.display_as_valid(False)
			self._PRW_billable.SetFocus()
		else:
			self._PRW_billable.display_as_valid(True)

		return validity
	#----------------------------------------------------------------
	def _save_as_new(self):
		data = gmBilling.create_bill_item (
			pk_encounter = gmPerson.gmCurrentPatient().emr.active_encounter['pk_encounter'],
			pk_billable = self._PRW_billable.GetData(),
			pk_staff = gmStaff.gmCurrentProvider()['pk_staff']		# should be settable !
		)
		data['raw_date_to_bill'] = self._PRW_date.GetData()
		converted, data['unit_count'] = gmTools.input2decimal(self._TCTRL_count.GetValue())
		converted, data['net_amount_per_unit'] = gmTools.input2decimal(self._TCTRL_amount.GetValue())
		converted, data['amount_multiplier'] = gmTools.input2decimal(self._TCTRL_factor.GetValue())
		data['item_detail'] = self._TCTRL_comment.GetValue().strip()
		data.save()

		self.data = data
		return True
	#----------------------------------------------------------------
	def _save_as_update(self):
		self.data['pk_encounter_to_bill'] = self._PRW_encounter.GetData()
		self.data['raw_date_to_bill'] = self._PRW_date.GetData()
		converted, self.data['unit_count'] = gmTools.input2decimal(self._TCTRL_count.GetValue())
		converted, self.data['net_amount_per_unit'] = gmTools.input2decimal(self._TCTRL_amount.GetValue())
		converted, self.data['amount_multiplier'] = gmTools.input2decimal(self._TCTRL_factor.GetValue())
		self.data['item_detail'] = self._TCTRL_comment.GetValue().strip()
		return self.data.save()
	#----------------------------------------------------------------
	def _refresh_as_new(self):
		self._PRW_billable.SetText()
		self._PRW_encounter.set_from_instance(gmPerson.gmCurrentPatient().emr.active_encounter)
		self._PRW_date.SetData()
		self._TCTRL_count.SetValue(u'1')
		self._TCTRL_amount.SetValue(u'')
		self._LBL_currency.SetLabel(_("EUR"))
		self._TCTRL_factor.SetValue(u'1')
		self._TCTRL_comment.SetValue(u'')

		self._PRW_billable.Enable()
		self._PRW_billable.SetFocus()
	#----------------------------------------------------------------
	def _refresh_as_new_from_existing(self):
		self._PRW_billable.SetText()
		self._TCTRL_count.SetValue(u'1')
		self._TCTRL_amount.SetValue(u'')
		self._TCTRL_comment.SetValue(u'')

		self._PRW_billable.Enable()
		self._PRW_billable.SetFocus()
	#----------------------------------------------------------------
	def _refresh_from_existing(self):
		self._PRW_billable.set_from_pk(self.data['pk_billable'])
		self._PRW_encounter.set_from_instance(gmPerson.gmCurrentPatient().emr.active_encounter)
		self._PRW_date.SetData(data = self.data['raw_date_to_bill'])
		self._TCTRL_count.SetValue(u'%s' % self.data['unit_count'])
		self._TCTRL_amount.SetValue(u'%s' % self.data['net_amount_per_unit'])
		self._LBL_currency.SetLabel(self.data['currency'])
		self._TCTRL_factor.SetValue(u'%s' % self.data['amount_multiplier'])
		self._TCTRL_comment.SetValue(gmTools.coalesce(self.data['item_detail'], u''))

		self._PRW_billable.Disable()
		self._PRW_date.SetFocus()
	#----------------------------------------------------------------
	def _on_billable_selected(self, item):
		if item is None:
			return
		if self._TCTRL_amount.GetValue().strip() != u'':
			return
		val = u'%s' % self._PRW_billable.GetData(as_instance = True)['raw_amount']
		wx.CallAfter(self._TCTRL_amount.SetValue, val)

#============================================================
from Gnumed.wxGladeWidgets import wxgBillingPluginPnl

class cBillingPluginPnl(wxgBillingPluginPnl.wxgBillingPluginPnl, gmRegetMixin.cRegetOnPaintMixin):
	def __init__(self, *args, **kwargs):

		wxgBillingPluginPnl.wxgBillingPluginPnl.__init__(self, *args, **kwargs)
		gmRegetMixin.cRegetOnPaintMixin.__init__(self)
		self.__register_interests()
	#-----------------------------------------------------
	def __reset_ui(self):
		self._PNL_bill_items.identity = None
		self._CHBOX_show_non_invoiced_only.SetValue(1)
		self._PRW_billable.SetText(u'', None)
		self._TCTRL_factor.SetValue(u'1.0')
		self._TCTRL_factor.Disable()
		self._TCTRL_details.SetValue(u'')
		self._TCTRL_details.Disable()
	#-----------------------------------------------------
	# event handling
	#-----------------------------------------------------
	def __register_interests(self):
		gmDispatcher.connect(signal = u'pre_patient_selection', receiver = self._on_pre_patient_selection)
		gmDispatcher.connect(signal = u'post_patient_selection', receiver = self._on_post_patient_selection)

		gmDispatcher.connect(signal = u'bill_item_mod_db', receiver = self._on_bill_item_modified)

		self._PRW_billable.add_callback_on_selection(self._on_billable_selected_in_prw)
	#-----------------------------------------------------
	def _on_pre_patient_selection(self):
		wx.CallAfter(self.__reset_ui)
	#-----------------------------------------------------
	def _on_post_patient_selection(self):
		wx.CallAfter(self._schedule_data_reget)
	#-----------------------------------------------------
	def _on_bill_item_modified(self):
		wx.CallAfter(self._schedule_data_reget)
	#-----------------------------------------------------
	def _on_non_invoiced_only_checkbox_toggled(self, event):
		self._PNL_bill_items.show_non_invoiced_only = self._CHBOX_show_non_invoiced_only.GetValue()
	#--------------------------------------------------------
	def _on_insert_bill_item_button_pressed(self, event):
		val = self._TCTRL_factor.GetValue().strip()
		if val == u'':
			factor = 1.0
		else:
			converted, factor = gmTools.input2decimal(val)
			if not converted:
				gmGuiHelpers.gm_show_warning (
					_('"Factor" must be a number\n\nCannot insert bill item.'),
					_('Inserting bill item')
				)
				return False
		bill_item = gmBilling.create_bill_item (
			pk_encounter = gmPerson.gmCurrentPatient().emr.active_encounter['pk_encounter'],
			pk_billable = self._PRW_billable.GetData(),
			pk_staff = gmStaff.gmCurrentProvider()['pk_staff']
		)
		bill_item['amount_multiplier'] = factor
		bill_item['item_detail'] = self._TCTRL_details.GetValue()
		bill_item.save()

		self._TCTRL_details.SetValue(u'')

		return True
	#--------------------------------------------------------
	def _on_billable_selected_in_prw(self, billable):
		if billable is None:
			self._TCTRL_factor.Disable()
			self._TCTRL_details.Disable()
			self._BTN_insert_item.Disable()
		else:
			self._TCTRL_factor.Enable()
			self._TCTRL_details.Enable()
			self._BTN_insert_item.Enable()
	#-----------------------------------------------------
	# reget-on-paint mixin API
	#-----------------------------------------------------
	def _populate_with_data(self):
		self._PNL_bill_items.identity = gmPerson.gmCurrentPatient()
		return True
#============================================================
# main
#------------------------------------------------------------
if __name__ == '__main__':

	if len(sys.argv) < 2:
		sys.exit()

	if sys.argv[1] != 'test':
		sys.exit()

	from Gnumed.pycommon import gmI18N
	gmI18N.activate_locale()
	gmI18N.install_domain(domain = 'gnumed')

	#----------------------------------------
	app = wx.PyWidgetTester(size = (600, 600))
	#app.SetWidget(cATCPhraseWheel, -1)
	app.SetWidget(cSubstancePhraseWheel, -1)
	app.MainLoop()