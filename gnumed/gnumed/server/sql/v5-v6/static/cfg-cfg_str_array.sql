-- ==============================================================
-- GNUmed database schema change script
--
-- Source database version: v5
-- Target database version: v6
--
-- License: GPL
-- Author: Karsten Hilbert
-- 
-- ==============================================================
-- $Id: cfg-cfg_str_array.sql,v 1.2 2007-04-06 23:19:31 ncq Exp $
-- $Revision: 1.2 $

-- --------------------------------------------------------------
\set ON_ERROR_STOP 1

-- --------------------------------------------------------------
insert into cfg.cfg_str_array
	(fk_item, value)
values (
	(select pk from cfg.cfg_item where workplace = 'GNUmed Standard'),
	'{"gmProviderInboxPlugin","gmNotebookedPatientEditionPlugin","gmEMRBrowserPlugin","gmNotebookedProgressNoteInputPlugin","gmEMRJournalPlugin","gmShowMedDocs","gmScanIdxMedDocsPlugin","gmDataMiningPlugin","gmXdtViewer","gmManual","gmConfigRegistry"}'
);

-- --------------------------------------------------------------
select public.log_script_insertion('$RCSfile: cfg-cfg_str_array.sql,v $', '$Revision: 1.2 $');

-- ==============================================================
-- $Log: cfg-cfg_str_array.sql,v $
-- Revision 1.2  2007-04-06 23:19:31  ncq
-- - include data mining panel
--
-- Revision 1.1  2007/04/02 14:16:44  ncq
-- - added
--
--