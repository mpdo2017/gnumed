-- Projekt GNUmed
-- Impfkalender der Hersteller von Typhus-Impfstoffen

-- Quellen: Beipackzettel

-- author: Karsten Hilbert <Karsten.Hilbert@gmx.net>
-- license: GPL
-- $Source: /home/ncq/Projekte/cvs2git/vcs-mirror/gnumed/gnumed/server/sql/country.specific/de/Impfplan-Typhus.sql,v $
-- $Id: Impfplan-Typhus.sql,v 1.1 2006-02-27 17:31:30 ncq Exp $
-- =============================================
-- force terminate + exit(3) on errors if non-interactive
\set ON_ERROR_STOP 1

-- Impfplan erstellen
insert into clin.vacc_regime
	(fk_recommended_by, fk_indication, name)
values (
	-1,
	(select id from clin.vacc_indication where description='salmonella typhi'),
	'Typhusimpfung (Hersteller)'
);

-- Impfzeitpunkte definieren
insert into clin.vacc_def
	(fk_regime, seq_no, min_age_due, comment)
values (
	currval('clin.vacc_regime_id_seq'),
	1,
	'2 years'::interval,
	'unter 2 Jahren nur bei konkretem Infektionsrisiko oder einer Epidemie impfen'
);

insert into clin.vacc_def
	(fk_regime, seq_no, min_age_due, is_booster, min_interval)
values (
	currval('clin.vacc_regime_id_seq'),
	null,
	'5 years'::interval,
	true,
	'3 years'::interval
);

-- =============================================
select log_script_insertion('$RCSfile: Impfplan-Typhus.sql,v $', '$Revision: 1.1 $');

-- =============================================
-- $Log: Impfplan-Typhus.sql,v $
-- Revision 1.1  2006-02-27 17:31:30  ncq
-- - Typhus-Impfplan
--
--