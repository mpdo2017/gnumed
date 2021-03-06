-- ==============================================================
-- GNUmed database schema change script
--
-- License: GPL v2 or later
-- Author: Karsten Hilbert
-- 
-- ==============================================================
-- $Id: v11-clin-v_narrative4search-fixup.sql,v 1.2 2009-09-15 15:19:31 ncq Exp $
-- $Revision: 1.2 $

-- --------------------------------------------------------------
\unset ON_ERROR_STOP
drop view clin.v_narrative4search cascade;
\set ON_ERROR_STOP 1

-- --------------------------------------------------------------
create view clin.v_narrative4search as


select	-- clin.clin_root_items
	vpi.pk_patient as pk_patient,
	vpi.soap_cat as soap_cat,
	vpi.narrative as narrative,
	vpi.pk_encounter as pk_encounter,
	vpi.pk_episode as pk_episode,
	vpi.pk_health_issue as pk_health_issue,
	vpi.pk_item as src_pk,
	vpi.src_table as src_table
from
	clin.v_pat_items vpi
where
	src_table not in ('allergy', 'test_result') and
	trim(coalesce(vpi.narrative, '')) != ''


union all	-- test results
select
	(select fk_patient from clin.encounter where pk = ctr.fk_encounter)
		as pk_patient,
	ctr.soap_cat
		as soap_cat,
	coalesce(ctr.narrative, ' ')
		|| coalesce(ctr.val_alpha, ' ')
		|| coalesce(ctr.val_unit, ' ')
		|| coalesce(ctr.val_normal_range, ' ')
		|| coalesce(ctr.val_target_range, ' ')
		|| coalesce(ctr.norm_ref_group, ' ')
		|| coalesce(ctr.note_test_org, ' ')
		|| coalesce(ctr.material, ' ')
		|| coalesce(ctr.material_detail, ' ')
		as narrative,
	ctr.fk_encounter
		as pk_encounter,
	ctr.fk_episode
		as pk_episode,
	(select fk_health_issue from clin.episode where pk = ctr.fk_episode)
		as pk_health_issue,
	ctr.pk
		as src_pk,
	'clin.test_result'
		as src_table
from
	clin.test_result ctr


union all	-- test result reviews
select
	(select fk_patient from clin.encounter where pk =
		(select fk_encounter from clin.test_result where clin.test_result.pk = crtr.fk_reviewed_row)
	)
		as pk_patient,
	'o'::text
		as soap_cat,
	crtr.comment
		as narrative,
	(select fk_encounter from clin.test_result where clin.test_result.pk = crtr.fk_reviewed_row)
		as pk_encounter,
	(select fk_episode from clin.test_result where clin.test_result.pk = crtr.fk_reviewed_row)
		as pk_episode,
	(select fk_health_issue from clin.episode where pk =
		(select fk_episode from clin.test_result where clin.test_result.pk = crtr.fk_reviewed_row)
	)
		as pk_health_issue,
	crtr.pk
		as src_pk,
	'clin.reviewed_test_results'
		as src_table
from
	clin.reviewed_test_results crtr
where
	trim(coalesce(crtr.comment, '')) != ''


union all -- allergy state
select
	(select fk_patient from clin.encounter where pk = cas.fk_encounter)
		as pk_patient,
	'o'::text
		as soap_cat,
	cas.comment
		as narrative,
	cas.fk_encounter
		as pk_encounter,
	null
		as pk_episode,
	null
		as pk_health_issue,
	cas.pk
		as src_pk,
	'clin.allergy_state'
		as src_table
from
	clin.allergy_state cas
where
	trim(coalesce(cas.comment, '')) != ''


union all -- allergies
select
	(select fk_patient from clin.encounter where pk = ca.fk_encounter)
		as pk_patient,
	ca.soap_cat
		as soap_cat,
	coalesce(narrative, ' ')
		|| coalesce(substance, ' ')
		|| coalesce(substance_code, ' ')
		|| coalesce(generics, ' ')
		|| coalesce(allergene, ' ')
		|| coalesce(atc_code, ' ')
		as narrative,
	ca.fk_encounter
		as pk_encounter,
	ca.fk_episode
		as pk_episode,
	(select fk_health_issue from clin.episode where pk = ca.fk_episode)
		as pk_health_issue,
	ca.pk
		as src_pk,
	'clin.allergy'
		as src_table
from
	clin.allergy ca


union all	-- health issues
select
	(select fk_patient from clin.encounter where pk = chi.fk_encounter)
		as pk_patient,
	'a' as soap_cat,
	chi.description
		as narrative,
	chi.fk_encounter
		as pk_encounter,
	null
		as pk_episode,
	chi.pk
		as pk_health_issue,
	chi.pk
		as src_pk,
	'clin.health_issue'
		as src_table
from
	clin.health_issue chi
where
	trim(coalesce(chi.description, '')) != ''


union all	-- encounters
select
	cenc.fk_patient as pk_patient,
	's' as soap_cat,
	(coalesce(cenc.reason_for_encounter, '') || '  ' ||
	 coalesce(cenc.assessment_of_encounter, '')
	) as narrative,
	cenc.pk as pk_encounter,
	null as pk_episode,
	null as pk_health_issue,
	cenc.pk as src_pk,
	'clin.encounter' as src_table
from
	clin.encounter cenc
where
	trim(coalesce(cenc.reason_for_encounter, '')) != '' or
	trim(coalesce(cenc.assessment_of_encounter, '')) != ''


union all	-- episodes
select
	(select fk_patient from clin.encounter where pk = cep.fk_encounter)
		as pk_patient,
	's' as soap_cat,
	cep.description
		as narrative,
	cep.fk_encounter
		as pk_encounter,
	cep.pk
		as pk_episode,
	cep.fk_health_issue
		as pk_health_issue,
	cep.pk
		as src_pk,
	'clin.episode'
		as src_table
from
	clin.episode cep
where
	trim(coalesce(cep.description, '')) != ''


union all	-- family history
select
	vhxf.pk_patient as pk_patient,
	vhxf.soap_cat as soap_cat,
	(_(vhxf.relationship) || ' (' ||
	 vhxf.relationship || ') ' ||
	 vhxf.name_relative || ': ' ||
	 vhxf.condition
	) as narrative,
	vhxf.pk_encounter as pk_encounter,
	vhxf.pk_episode as pk_episode,
	vhxf.pk_health_issue as pk_health_issue,
	vhxf.pk_hx_family_item as src_pk,
	'clin.hx_family_item' as src_table
from
	clin.v_hx_family vhxf


union all	-- documents
select
	vdm.pk_patient as pk_patient,
	'o' as soap_cat,
	(vdm.l10n_type || ' ' ||
	 coalesce(vdm.ext_ref, '') || ' ' ||
	 coalesce(vdm.comment, '')
	) as narrative,
	vdm.pk_encounter as pk_encounter,
	vdm.pk_episode as pk_episode,
	vdm.pk_health_issue as pk_health_issue,
	vdm.pk_doc as src_pk,
	'blobs.doc_med' as src_table
from
	blobs.v_doc_med vdm


union all	-- document objects
select
	vo4d.pk_patient as pk_patient,
	'o' as soap_cat,
	vo4d.obj_comment as narrative,
	vo4d.pk_encounter as pk_encounter,
	vo4d.pk_episode as pk_episode,
	vo4d.pk_health_issue as pk_health_issue,
	vo4d.pk_obj as src_pk,
	'blobs.doc_obj' as src_table
from
	blobs.v_obj4doc_no_data vo4d
where
	trim(coalesce(vo4d.obj_comment, '')) != ''


union all	-- document descriptions
select
	vdd.pk_patient as pk_patient,
	'o' as soap_cat,
	vdd.description as narrative,
	vdd.pk_encounter as pk_encounter,
	vdd.pk_episode as pk_episode,
	vdd.pk_health_issue as pk_health_issue,
	vdd.pk_doc_desc as src_pk,
	'blobs.doc_desc' as src_table
from
	blobs.v_doc_desc vdd
where
	trim(coalesce(vdd.description, '')) != ''


union all	-- reviewed documents
select
	vrdo.pk_patient as pk_patient,
	's' as soap_cat,
	vrdo.comment as narrative,
	null as pk_encounter,
	vrdo.pk_episode as pk_episode,
	vrdo.pk_health_issue as pk_health_issue,
	vrdo.pk_review_root as src_pk,
	'blobs.v_reviewed_doc_objects' as src_table
from
	blobs.v_reviewed_doc_objects vrdo
where
	trim(coalesce(vrdo.comment, '')) != ''

;

-- --------------------------------------------------------------
comment on view clin.v_narrative4search is
	'unformatted *complete* narrative for patients
	 including health issue/episode/encounter descriptions,
	 mainly for searching the narrative in context';

-- --------------------------------------------------------------
grant select on clin.v_narrative4search to group "gm-doctors";

-- --------------------------------------------------------------
select gm.log_script_insertion('$RCSfile: v11-clin-v_narrative4search-fixup.sql,v $', '$Revision: 1.2 $');

-- ==============================================================
-- $Log: v11-clin-v_narrative4search-fixup.sql,v $
-- Revision 1.2  2009-09-15 15:19:31  ncq
-- - forgotten view in v11
--
--