# -*- coding: latin-1 -*-
"""GNUmed provider inbox middleware.

This should eventually end up in a class cPractice.
"""
#============================================================
# $Source: /home/ncq/Projekte/cvs2git/vcs-mirror/gnumed/gnumed/client/business/gmProviderInbox.py,v $
# $Id: gmProviderInbox.py,v 1.3 2006-05-12 13:48:27 ncq Exp $
__license__ = "GPL"
__version__ = "$Revision: 1.3 $"
__author__ = "K.Hilbert <Karsten.Hilbert@gmx.net>"

from Gnumed.pycommon import gmPG

#============================================================
class cProviderInbox:
	def __init__(self, provider_id=None):
		if provider_id is None:
			from Gnumed.business import gmPerson
			self.__provider_id = gmPerson.gmCurrentProvider['pk_staff']
		else:
			self.__provider_id = provider_id
	#--------------------------------------------------------
	def get_messages(self):
		cmd = """
select
	importance,
	l10n_category,
	l10n_type,
	comment,
	type,
	category,
	pk_context,
	data
from dem.v_provider_inbox vpi
where pk_staff = %s
order by importance desc"""
		rows = gmPG.run_ro_query('demographics', cmd, None, self.__provider_id)
		if rows is None:
			return [[1, _('error'), _('error'), _('unable to get provider inbox messages from database')]]
		return rows

#============================================================
if __name__ == '__main__':
	inbox = cProviderInbox()
	for msg in inbox.get_messages():
		print msg

#============================================================
# $Log: gmProviderInbox.py,v $
# Revision 1.3  2006-05-12 13:48:27  ncq
# - properly import gmPerson
#
# Revision 1.2  2006/05/12 12:04:30  ncq
# - use gmCurrentProvider
# - load more fields from inbox for later use
#
# Revision 1.1  2006/01/22 18:10:21  ncq
# - class for provider inbox
#
#