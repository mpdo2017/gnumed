-- Project: GnuMed
-- ===================================================================
-- $Source: /home/ncq/Projekte/cvs2git/vcs-mirror/gnumed/gnumed/server/sql/gmclinical.sql,v $
-- $Revision: 1.70 $
-- license: GPL
-- author: Ian Haywood, Horst Herb, Karsten Hilbert

-- ===================================================================
-- force terminate + exit(3) on errors if non-interactive
\set ON_ERROR_STOP 1

-- ===================================================================
-- generic EMR structure
-- -------------------------------------------------------------------
create table clin_health_issue (
	id serial primary key,
	id_patient integer not null,
	description varchar(128) default '__default__',
	unique (id_patient, description)
) inherits (audit_fields);

select add_table_for_audit('clin_health_issue');

comment on table clin_health_issue is
	'long-ranging, underlying health issue such as "mild immunodeficiency", "diabetes type 2"';
comment on column clin_health_issue.id_patient is
 	'id of patient this health issue relates to, should
	 be reference but might be outside our own database';
comment on column clin_health_issue.description is
	'descriptive name of this health issue, may change over time';

-- -------------------------------------------------------------------
-- episode related tables
-- -------------------------------------------------------------------
create table clin_episode (
	id serial primary key,
	id_health_issue integer not null references clin_health_issue(id),
	description varchar(128) default '__default__',
	unique (id_health_issue, description)
) inherits (audit_fields);

select add_table_for_audit('clin_episode');

comment on table clin_episode is
	'clinical episodes such as "recurrent Otitis media", "traffic accident 7/99", "Hepatitis B"';
comment on column clin_episode.id_health_issue is
	'health issue this episode is part of';
comment on column clin_episode.description is
	'descriptive name of this episode, may change over time; if
	 "__default__" applications should display the most recently
	 associated diagnosis/month/year plus some marker for "default"';

-- unique names (descriptions) for episodes per health issue (e.g. per patient),
-- about the only reason for this table to exist is the description field such
-- as to allow arbitrary names for episodes, another reason is that explicit
-- recording of episodes removes the ambiguity that results from basing them
-- on start/end dates of bouts of care,

create table last_act_episode (
	id serial primary key,
	id_episode integer not null references clin_episode(id),
	id_patient integer unique not null
);

comment on table last_act_episode is
	'records the most recently active episode per patient,
	 upon instantiation of a patient object it should read
	 the most recently active episode from this table,
	 upon deletion of the object, the last active episode
	 should be recorded here,
	 do *not* rely on the content of this table *during*
	 the life time of a patient object as the value can
	 change from under us';

-- -------------------------------------------------------------------
-- encounter related tables
-- -------------------------------------------------------------------
create table _enum_encounter_type (
	id serial primary key,
	description varchar(32) unique not null
);

comment on TABLE _enum_encounter_type is
	'these are the types of encounter';

-- -------------------------------------------------------------------
create table clin_encounter (
	id serial primary key,
	fk_patient integer not null,
	fk_location integer,
	fk_provider integer,
	fk_type integer not null references _enum_encounter_type(id) default 1,
	description varchar(128) default '__default__'
);

-- remote foreign keys
select add_x_db_fk_def('clin_encounter', 'fk_patient', 'personalia', 'identity', 'id');
select add_x_db_fk_def('clin_encounter', 'fk_location', 'personalia', 'org', 'id');

comment on table clin_encounter is
	'a clinical encounter between a person and the health care system';
comment on COLUMN clin_encounter.fk_patient is
	'PK of subject of care, should be PUPIC, actually';
comment on COLUMN clin_encounter.fk_location is
	'ID of location *of care*, e.g. where the provider is at';
comment on COLUMN clin_encounter.fk_provider is
	'ID of (main) provider of care';
comment on COLUMN clin_encounter.fk_type is
	'ID of encounter type of this encounter';
comment on column clin_encounter.description is
	'descriptive name of this encounter, may change over time; if
	 "__default__" applications should display "<date> (<provider>)"
	 plus some marker for "default"';

-- about the only reason for this table to exist is the id_type
-- field, otherwise one could just store the data in clin_root_item

create table curr_encounter (
	id serial primary key,
	id_encounter integer not null references clin_encounter(id),
	started timestamp with time zone not null default CURRENT_TIMESTAMP,
	last_affirmed timestamp with time zone not null default CURRENT_TIMESTAMP,
	"comment" varchar(128) default 'affirmed'
);

comment on table curr_encounter is
	'currently ongoing encounters are stored in this table,
	 clients are supposed to check this table or create a
	 new encounter if appropriate';
comment on column curr_encounter.last_affirmed is
	'clients are supposed to update this field when appropriate
	 such that the encounter detection heuristics in other clients
	 has something to work with';
comment on column curr_encounter."comment" is
	'clients may save an arbitrary comment here when
	 updating last_affirmed, useful for later perusal';

-- ===================================================================
-- EMR item root with narrative aggregation
-- -------------------------------------------------------------------
create table clin_root_item (
	pk_item serial primary key,
	clin_when timestamp with time zone not null default CURRENT_TIMESTAMP,
	id_encounter integer not null references clin_encounter(id),
	id_episode integer not null references clin_episode(id),
	narrative text
) inherits (audit_fields);

comment on TABLE clin_root_item is
	'ancestor table for clinical items of any kind, basic
	 unit of clinical information, do *not* store data in
	 here directly, use child tables,
	 contains all the clinical narrative aggregated for full
	 text search, ancestor for all tables that want to store
	 clinical free text';
comment on COLUMN clin_root_item.pk_item is
	'the primary key, not named "id" as usual since child tables
	 will have "id" primary keys already';
comment on column clin_root_item.clin_when is
	'when this clinical item became known, can be different from
	 when it was entered into the system (= audit_fields.modified_when)';
comment on COLUMN clin_root_item.id_encounter is
	'the encounter this item belongs to';
comment on COLUMN clin_root_item.id_episode is
	'the episode this item belongs to';
comment on column clin_root_item.narrative is
	'each clinical item by default inherits a free text field for clinical narrative';

-- ============================================
-- specific EMR content tables: SOAP++
-- --------------------------------------------
create table clin_note (
	id serial primary key
) inherits (clin_root_item);

select add_table_for_audit('clin_note');

comment on TABLE clin_note is
	'Used to store clinical free text.';

-- --------------------------------------------
create table clin_aux_note (
	id serial primary key
) inherits (clin_root_item);

select add_table_for_audit('clin_aux_note');

comment on TABLE clin_aux_note is
	'Other tables link here if they need more free text fields.';

-- --------------------------------------------
create table _enum_hx_type (
	id serial primary key,
	description varchar(128) unique not null
);

comment on TABLE _enum_hx_type is
	'types of history taken during a clinical encounter';

-- --------------------------------------------
create table _enum_hx_source (
	id serial primary key,
	description varchar(128) unique not null
);

comment on table _enum_hx_source is
	'sources of clinical information: patient, relative, notes, correspondence';

-- --------------------------------------------
create table clin_history (
	id serial primary key,
	id_type integer not null references _enum_hx_type(id),
	id_source integer REFERENCES _enum_hx_source(id)
) inherits (clin_root_item);

-- narrative provided by clin_root_item

comment on TABLE clin_history is
	'narrative details of history taken during a clinical encounter';
comment on COLUMN clin_history.id_type is
	'the type of history taken';
comment on COLUMN clin_history.id_source is
	'who provided the details of this entry';

-- --------------------------------------------
create table clin_physical (
	id serial primary key
) inherits (clin_root_item);

-- narrative provided by clin_root_item

comment on TABLE clin_physical is
	'narrative details of physical exam during a clinical encounter';

-- ============================================
-- vaccination tables
-- ============================================
create table vacc_indication (
	id serial primary key,
	description text unique not null
) inherits (audit_fields);

select add_table_for_audit('vacc_indication');
select add_table_for_scoring('vacc_indication');

comment on table vacc_indication is
	'definition of indications for vaccinations';
comment on column vacc_indication.description is
	'description of indication, eg "Measles"';

-- --------------------------------------------
create table lnk_vacc_ind2code (
	id serial primary key,
	fk_indication integer not null references vacc_indication(id),
	code text not null,
	coding_system text not null,
	unique (fk_indication, code, coding_system)
);

-- remote foreign keys
select add_x_db_fk_def('lnk_vacc_ind2code', 'coding_system', 'reference', 'ref_source', 'name_short');

comment on table lnk_vacc_ind2code is
	'links vaccination indications to disease codes,
	 useful for cross-checking whether a patient
	 should be considered immune against a disease,
	 multiple codes from multiple coding systems can
	 be linked against one vaccination indication';

-- --------------------------------------------
create table vacc_route (
	id serial primary key,
	abbreviation text unique not null,
	description text unique not null
) inherits (audit_fields);

select add_table_for_audit('vacc_route');

comment on table vacc_route is
	'definition of route via which vaccine is given,
	 currently i.m. and p.o. only but may include
	 "via genetically engineered food" etc in the
	 future';

-- --------------------------------------------
-- maybe this table belongs into "service"
-- "inventory"/"stock" or something one day
create table vaccine (
	id serial primary key,
	id_route integer not null references vacc_route(id) default 1,
	trade_name text unique not null,
	short_name text unique not null,
	is_live boolean not null default false,
	is_licensed boolean not null default true,
	min_age interval not null,
	max_age interval default null,
	last_batch_no text default null,
	comment text
) inherits (audit_fields);

select add_table_for_audit('vaccine');

comment on table vaccine is
	'definition of a vaccine as available on the market';
comment on column vaccine.id_route is
	'route this vaccine is given';
comment on column vaccine.trade_name is
	'full name the vaccine is traded under';
comment on column vaccine.short_name is
	'common, maybe practice-specific shorthand name
	 for referring to this vaccine';
comment on column vaccine.is_live is
	'whether this is a live vaccine';
comment on column vaccine.is_licensed is
	'whether this vaccine is currently licensed
	 for use in your jurisdiction';
comment on column vaccine.min_age is
	'minimum age this vaccine is licensed for';
comment on column vaccine.max_age is
	'maximum age this vaccine is licensed for';
comment on column vaccine.last_batch_no is
	'serial # of most recently used batch, for
	 rapid data input purposes';

-- --------------------------------------------
create table lnk_vaccine2inds (
	id serial primary key,
	fk_vaccine integer not null references vaccine(id),
	fk_indication integer not null references vacc_indication(id),
	unique (fk_vaccine, fk_indication)
);

comment on table lnk_vaccine2inds is
	'links vaccines to their indications';

-- --------------------------------------------
create table vacc_def (
	id serial primary key,
	fk_indication integer not null references vacc_indication(id),
	-- FIXME: specific constraint: null if (is_booster == true) else > 0
	is_booster boolean not null default false,
	seq_no integer not null,
	min_age_due interval not null,
	max_age_due interval not null,
	min_interval interval not null,
	comment text,
	unique(fk_indication, seq_no)
) inherits (audit_fields);

select add_table_for_audit('vacc_def');

comment on table vacc_def is
	'defines a given vaccination event';
comment on column vacc_def.fk_indication is
	'indication for which this vaccination
	 event is scheduled';
comment on column vacc_def.is_booster is
	'does this definition represent a booster';
comment on column vacc_def.seq_no is
	'sequence number for this vaccination event
	 within a particular schedule/regime,
	 meaningless if (is_booster == true)';
comment on column vacc_def.min_age_due is
	'minimum age at which this shot is due';
comment on column vacc_def.max_age_due is
	'maximum age at which this shot is due,
	 if max_age_due = -1: no maximum age';
comment on column vacc_def.min_interval is
	'if (is_booster == true):
		recommended interval for boostering
	 id (is_booster == false):
	 	minimum interval after previous vaccination,
		meaningless if seq_no == 1';

-- --------------------------------------------
create table vaccination (
	id serial primary key,
	fk_patient integer not null,
	fk_provider integer not null,
	fk_vaccine integer references vaccine(id),
	-- we need a constraint on fk_vacc_def to only
	-- allow sequential vacc_def.seq_no inserts
	fk_vacc_def integer references vacc_def(id),
	site text default 'not recorded',
	batch_no text not null default 'not recorded',
	unique (fk_patient, fk_vaccine, clin_when)
) inherits (audit_fields, clin_root_item);

-- Richard tells us that "refused" should go into progress note

select add_table_for_audit('vaccination');

-- remote foreign keys:
select add_x_db_fk_def('vaccination', 'fk_patient', 'personalia', 'identity', 'id');
select add_x_db_fk_def('vaccination', 'fk_provider', 'personalia', 'identity', 'id');

comment on table vaccination is
	'holds vaccinations actually given';
comment on column vaccination.fk_vacc_def is
	'the vaccination event this particular
	 vaccination is supposed to cover, allows to
	 link out-of-band vaccinations into regimes';

-- --------------------------------------------
create table vacc_regime (
	id serial primary key,
	fk_recommended_by integer,
	fk_indication integer not null references vacc_indication(id),
	description text unique not null
) inherits (audit_fields);

select add_table_for_audit('vacc_regime');
select add_table_for_scoring('vacc_regime');

-- remote foreign keys:
select add_x_db_fk_def('vacc_regime', 'fk_recommended_by', 'reference', 'ref_source', 'id');

comment on table vacc_regime is
	'holds vaccination schedules/regimes/target diseases';
comment on column vacc_regime.fk_recommended_by is
	'organization recommending this vaccination';
comment on column vacc_regime.fk_indication is
	'vaccination indication this regime is targeted at';

-- ============================================
create table lnk_vacc_def2regime (
	id serial primary key,
	fk_vacc_def integer unique not null references vacc_def(id),
	fk_regime integer not null references vacc_regime(id)
);

-- ============================================
-- allergies tables
create table allergy_state (
	id serial primary key,
	id_patient integer unique not null,
	has_allergy integer default null check (has_allergy in (null, -1, 0, 1))
) inherits (audit_fields);

select add_table_for_audit('allergy_state');

comment on column allergy_state.has_allergy is
	'patient allergenic state:
	 - null: unknown, not asked, no data available
	 - -1: unknown, asked, no data obtained
	 - 0:  known, asked, has no allergies
	 - 1:  known, asked, does have allergies
	';

-- --------------------------------------------
create table _enum_allergy_type (
	id serial primary key,
	value varchar(32) unique not null
);

-- --------------------------------------------
create table allergy (
	id serial primary key,
	substance varchar(128) not null,
	substance_code varchar(256) default null,
	generics varchar(256) default null,
	allergene varchar(256) default null,
	atc_code varchar(32) default null,
	id_type integer not null references _enum_allergy_type(id),
	reaction text default '',
	generic_specific boolean default false,
	definite boolean default false
) inherits (clin_root_item);

select add_table_for_audit('allergy');

-- narrative provided by clin_root_item

comment on table allergy is
	'patient allergy details';
comment on column allergy.substance is
	'real-world name of substance the patient reacted to, brand name if drug';
comment on column allergy.substance_code is
	'data source specific opaque product code; must provide a link
	 to a unique product/substance in the database in use; should follow
	 the parseable convention of "<source>::<source version>::<identifier>",
	 e.g. "MIMS::2003-1::190" for Zantac; it is left as an exercise to the
	 application to know what to do with this information';
comment on column allergy.generics is
	'names of generic compounds if drug; brand names change/disappear, generic names do not';
comment on column allergy.allergene is
	'name of allergenic ingredient in substance if known';
comment on column allergy.atc_code is
	'ATC code of allergene or substance if approprate, applicable for penicilline, not so for cat fur';
comment on column allergy.id_type is
	'allergy/sensitivity';
comment on column allergy.reaction is
	'description of reaction such as "difficulty breathing, "skin rash", "diarrhea" etc.';
comment on column allergy.generic_specific is
	'only meaningful for *drug*/*generic* reactions:
	 1) true: applies to one in "generics" forming "substance",
			  if more than one generic listed in "generics" then
			  "allergene" *must* contain the generic in question;
	 2) false: applies to drug class of "substance";';
comment on column allergy.definite is
	'true: definite, false: not definite';

-- ===================================================================
-- following tables not yet converted to EMR structure ...
-- -------------------------------------------------------------------
create table clin_diagnosis (
	id serial primary key,
	approximate_start text default null,
	code text not null,
	id_coding_systems integer not null
) inherits (clin_root_item);

comment on TABLE clin_diagnosis is
	'Coded clinical diagnoses assigned to patient, in addition to history';
comment on column clin_diagnosis.approximate_start is
	'around the time at which this diagnosis was made';
comment on column clin_diagnosis.code is
	'the code';
comment on column clin_diagnosis.id_coding_systems is
	'the coding system used to code the diagnosis';

-- -------------------------------------------------------------------
create table enum_confidentiality_level (
	id SERIAL primary key,
	description text
);

comment on table enum_confidentiality_level is
	'Various levels of confidentialoty of a coded diagnosis, such as public, clinical staff, treating doctor, etc.';

-- -------------------------------------------------------------------
create table clin_diagnosis_extra (
	id serial primary key,
	id_clin_diagnosis int REFERENCES clin_diagnosis (id),
	id_enum_confidentiality_level int REFERENCES enum_confidentiality_level (id)
);

comment on table clin_diagnosis_extra is
'Extra information about a diagnosis, just the confidentiality level at present.';

-- ============================================
-- Drug related tables

-- These tables are pasted from gmdrugs.sql, how do we otherwise
-- deal with this?

create table drug_units (
	id serial primary key,
	unit varchar(30)
);
comment on table drug_units is
'(SI) units used to quantify/measure drugs';
comment on column drug_units.unit is
'(SI) units used to quantify/measure drugs like "mg", "ml"';


create table drug_formulations(
	id serial primary key,
	description varchar(60),
	comment text
);
comment on table drug_formulations is
'presentations or formulations of drugs like "tablet", "capsule" ...';
comment on column drug_formulations.description is
'the formulation of the drug, such as "tablet", "cream", "suspension"';


create table drug_routes (
	id serial primary key,
	description varchar(60),
	abbreviation varchar(10),
	comment text
);
comment on table drug_routes is
'administration routes of drugs';
comment on column drug_routes.description is
'administration route of a drug like "oral", "sublingual", "intravenous" ...';

-- --------------------------------------------
-- IMHO this needs considerably more thought
create table curr_medication (
	id serial primary key,
	-- administrative data
	started date not null,
	last_prescribed date not null,
	-- medical data
	brandname text default 'GENERIC',
	adjuvant text,
	db_xref varchar (128) not null,
	atc_code varchar (32),
	fluid_amount float,
	amount_unit integer references drug_units (id),
	packsize integer,
	id_route integer references drug_routes (id) not null,
	id_form integer references drug_formulations (id) not null,
	directions text,
	prn boolean,
	weekly float,
	mane float,
	midi float,
	vesper float,
	nocte float
) inherits (clin_root_item);
-- needs to be audited when stabilized

comment on table curr_medication is
'Representing what the patient is taking *now*, not a simple log
of prescriptions. The forms engine will record each script and all its fields
The audit mechanism will record all changes to this table.
 
Note the multiple redundancy of the stored drug data.
Applications should try in this order:
- internal database code
- brandname
- ATC code
- generic name(s) (in constituents)
';
comment on column curr_medication.started is
	'- when did patient start to take this medication
	 - in most cases the date of the first prescription
	   but not always
	 - for newly prescribed drugs identical to last_prescribed';
comment on column curr_medication.last_prescribed is
	'date last script written, for compliance checking';
comment on column curr_medication.fluid_amount is
	'for fluid drugs, the amount of fluid in each bottle/tube,
	 etc. Otherwise 1.0. The total amount dispensed is always
	 fluid_amount*packsize';
comment on column curr_medication.prn is 'true if "pro re nata" (= as required)';
comment on column curr_medication.directions is 'free text for directions, such as ''with food'' etc';
comment on column curr_medication.adjuvant is 'free text describing adjuvants, such as ''orange-flavoured'' etc.';
comment on column curr_medication.weekly is 'for drugs taken one/tweice a twice, such as bisphosphonates, metotrexate, etc., NULL otherwise. If non-NULL, overrides other dosing fields.';
comment on column curr_medication.mane is 'amount taken in the morning.';
comment on column curr_medication.midi is 'midday';
comment on column curr_medication.vesper is 'evening';
comment on column curr_medication.nocte is 'nighttime';

-- --------------------------------------------
-- IMHO this does not belong in here
create table constituents
(
	id serial primary key,
	genericname varchar (100),
	dose float,
	dose_unit integer references drug_units (id),
	id_drug integer references curr_medication (id)
);

comment on table constituents is
'the constituent substances of the various drugs (normalised out to support compound drugs like Augmentin)';
--comment on column constituents.name is
--'the English IUPHARM standard name, as a base, with no adjuvant, in capitals. So MORPHINE. not Morphine, not MORPHINE SULPHATE, not MORPHINIUM';
comment on column constituents.dose is
'the amount of drug (if salt, the amount of active base substance, in a unit (see amount_unit above)';
 
-- =============================================

create table enum_immunities
(
	id serial primary key,
	name text
);

comment on table enum_immunities is
'list of diseases to which patients may have immunity. Same table must exist in gmdrugs';


-- =============================================
create table clin_history_editarea(
                                id serial primary key,
                                id_clin_history integer references clin_history on delete cascade,
                                condition text,
                                age varchar(20),
                                "year" varchar(20),
                                "left" integer,
                                "right" integer, "both" integer, "none" integer,
                                active integer,
                                significant integer,
                                confidential integer,
                                operation integer,
                                notes1 text, notes2 text , progress text);

comment on table clin_history_editarea is 
'ui specific field storage, to avoid parsing of data when using past history editarea ui for clin_history';


-- =============================================
GRANT SELECT ON
	"clin_root_item",
	"clin_health_issue",
	"clin_episode",
	"last_act_episode",
	"_enum_encounter_type",
	"clin_encounter",
	"curr_encounter",
	"clin_note",
	"clin_aux_note",
	"_enum_hx_type",
	"_enum_hx_source",
	"clin_history",
	"clin_physical",
	"_enum_allergy_type",
	"allergy",
	vaccination,
	vaccine,
	vacc_def,
	clin_history_editarea
TO GROUP "gm-doctors";

GRANT SELECT, INSERT, UPDATE, DELETE
	"clin_root_item",
	"clin_root_item_pk_item_seq",
	"clin_health_issue",
	"clin_health_issue_id_seq",
	"clin_episode",
	"clin_episode_id_seq",
	"last_act_episode",
	"last_act_episode_id_seq",
	"_enum_encounter_type",
	"_enum_encounter_type_id_seq",
	"clin_encounter",
	"clin_encounter_id_seq",
	"curr_encounter",
	"curr_encounter_id_seq",
	"clin_note",
	"clin_note_id_seq",
	"clin_aux_note",
	"clin_aux_note_id_seq",
	"_enum_hx_type",
	"_enum_hx_type_id_seq",
	"_enum_hx_source",
	"_enum_hx_source_id_seq",
	"clin_history",
	"clin_history_id_seq",
	"clin_physical",
	"clin_physical_id_seq",
	"_enum_allergy_type",
	"_enum_allergy_type_id_seq",
	"allergy",
	"allergy_id_seq",
	vaccination,
	vaccination_id_seq,
	vaccine,
	vaccine_id_seq,
	vacc_def,
	vacc_def_id_seq,
	clin_history_editarea,  
	id_clin_history_editarea_seq 
TO GROUP "_gm-doctors";

-- =============================================
-- do simple schema revision tracking
INSERT INTO gm_schema_revision (filename, version) VALUES('$RCSfile: gmclinical.sql,v $', '$Revision: 1.70 $');

-- =============================================
-- $Log: gmclinical.sql,v $
-- Revision 1.70  2003-11-17 20:14:45  ncq
-- - cleanup grants, make primary key serial data type
--
-- Revision 1.69  2003/11/17 11:14:53  sjtan
--
-- (perhaps temporary) extra referencing table for past history.
--
-- Revision 1.68  2003/11/16 19:32:17  ncq
-- - clin_when in clin_root_item
--
-- Revision 1.67  2003/11/13 09:45:54  ncq
-- - add clin_date, clin_time to clin_root_item
--
-- Revision 1.66  2003/11/04 00:23:58  ncq
-- - some grants
--
-- Revision 1.65  2003/10/31 23:29:38  ncq
-- - cleanup, id_ -> fk_
--
-- Revision 1.64  2003/10/26 09:41:03  ncq
-- - truncate -> delete from
--
-- Revision 1.63  2003/10/20 22:01:01  ncq
-- - removed use of array type in FKs as per Syan's suggestion
--
-- Revision 1.62  2003/10/19 15:43:00  ncq
-- - even better vaccination tables
--
-- Revision 1.61  2003/10/07 22:29:10  ncq
-- - better comments on vacc_*
--
-- Revision 1.60  2003/10/01 15:44:24  ncq
-- - add vaccination tables, use auditing record table
--
-- Revision 1.59  2003/08/27 00:35:32  ncq
-- - add vaccination tables
--
-- Revision 1.58  2003/08/17 00:25:38  ncq
-- - remove log_ tables, they are now auto-created
--
-- Revision 1.57  2003/08/13 14:30:29  ncq
-- - drugchart -> curr_medication
-- - cleanup
--
-- Revision 1.56  2003/08/10 07:43:11  ihaywood
-- new drug tables
--
-- Revision 1.55  2003/07/27 22:01:05  ncq
-- - coding_systems moved to gmReference
-- - start work on clin_diagnosis, drug* tables pending
--
-- Revision 1.54  2003/06/29 15:25:30  ncq
-- - adapt to audit_fields split-off
-- - make clin_root_item inherit audit_fields but NOT audit_mark, hehe
--
-- Revision 1.53  2003/06/23 21:56:52  ncq
-- - grants on curr_encounter
--
-- Revision 1.52  2003/06/22 16:22:37  ncq
-- - add curr_encounter for tracking active encounters
-- - split clin_aux_note from clin_note so we can cleanly separate
--   deliberate free text from referenced free text (when building EHR
--   views, that is)
-- - grants
--
-- Revision 1.51  2003/06/03 13:49:50  ncq
-- - last_active_episode -> last_act_episode + grants on it
--
-- Revision 1.50  2003/06/02 21:03:41  ncq
-- - last_active_episode: unique on id_patient, not composite(patient/episode)
--
-- Revision 1.49  2003/06/01 11:38:12  ncq
-- - fix spelling of definate -> definite
--
-- Revision 1.48  2003/06/01 10:07:32  sjtan
--
-- change?
--
-- Revision 1.47  2003/05/22 12:56:12  ncq
-- - add "last_active_episode"
-- - adapt to audit_log -> audit_trail
--
-- Revision 1.46  2003/05/14 22:06:27  ncq
-- - merge clin_narrative and clin_item
-- - clin_item -> clin_root_item, general cleanup
-- - set up a few more audits
-- - set up dummy tables for audit trail table inheritance
-- - appropriate grants
--
-- Revision 1.45  2003/05/13 14:49:10  ncq
-- - warning on clin_narrative to not use directly
-- - make allergy the only audited table for now, add audit table for it
--
-- Revision 1.44  2003/05/12 19:29:45  ncq
-- - first stab at real auditing
--
-- Revision 1.43  2003/05/12 12:43:39  ncq
-- - gmI18N, gmServices and gmSchemaRevision are imported globally at the
--   database level now, don't include them in individual schema file anymore
--
-- Revision 1.42  2003/05/06 13:06:25  ncq
-- - pkey_ -> pk_
--
-- Revision 1.41  2003/05/05 12:40:03  ncq
-- - name is not a field of constituents anymore
--
-- Revision 1.40  2003/05/05 12:26:31  ncq
-- - remove comment on xref_id in script_drug, xref_id does not exist
--
-- Revision 1.39  2003/05/05 11:58:51  ncq
-- - audit_clinical -> clin_audit + use it
-- - clin_narrative now ancestor table + use it (as discussed with Ian)
--
-- Revision 1.38  2003/05/05 10:02:10  ihaywood
-- minor updates
--
-- Revision 1.37  2003/05/04 23:35:59  ncq
-- - major reworking to follow the formal EMR structure writeup
--
-- Revision 1.36  2003/05/03 00:44:40  ncq
-- - remove had_hypo from allergies table
--
-- Revision 1.35  2003/05/02 15:08:55  ncq
-- - episodes must have unique names (==description) per health issue
-- - remove cruft
-- - add not null to id_type in clin_encounter
-- - default id_comment in allergy to null
--
-- Revision 1.34  2003/05/01 15:06:29  ncq
-- - allergy.id_substance -> allergy.substance_code
--
-- Revision 1.33  2003/04/30 23:30:29  ncq
-- - v_i18n_patient_allergies
-- - new_allergy -> allergy_new
--
-- Revision 1.32  2003/04/29 12:38:32  ncq
-- - add not null to referencing constraints in episode/transactions
--
-- Revision 1.31  2003/04/28 21:40:40  ncq
-- - better indices
--
-- Revision 1.30  2003/04/28 20:56:16  ncq
-- - unclash "allergy" in hx type and type of allergic reaction + translations
-- - some useful indices
--
-- Revision 1.29  2003/04/25 12:43:52  ncq
-- - add grants
--
-- Revision 1.28  2003/04/25 12:32:39  ncq
-- - view on encounter types needs "as description"
--
-- Revision 1.27  2003/04/18 13:30:35  ncq
-- - add doc types
-- - update comment on allergy.id_substance
--
-- Revision 1.26  2003/04/17 20:20:11  ncq
-- - add source specific opaque substance/product identifier in table allergy
--
-- Revision 1.25  2003/04/12 15:34:49  ncq
-- - include the concept of aggregated clinical narrative
-- - consolidate history/physical exam tables
--
-- Revision 1.24  2003/04/09 14:47:17  ncq
-- - further tweaks on allergies tables
--
-- Revision 1.23  2003/04/09 13:50:29  ncq
-- - typos
--
-- Revision 1.22  2003/04/09 13:10:13  ncq
-- - _clinical_ -> _clin_
-- - streamlined episode/encounter/transaction
--
-- Revision 1.21  2003/04/07 12:28:24  ncq
-- - allergies table updated according to comments on resmed-de and gm-dev
--
-- Revision 1.20  2003/04/06 15:18:21  ncq
-- - can't reference _()ed fields in a view since it can't find the unique constraint in the underlying table
--
-- Revision 1.19  2003/04/06 15:10:05  ncq
-- - added some missing unique constraints
--
-- Revision 1.18  2003/04/06 14:51:40  ncq
-- - more cleanly separated data and schema
-- - first draft of allergies table
--
-- Revision 1.17  2003/04/02 13:37:56  ncq
-- - fixed a few more missing "primary key" on referenced "id serial"s
--
-- Revision 1.16  2003/04/02 12:31:07  ncq
-- - PostgreSQL 7.3 complained about referenced key enum_info_sources.id not being unique()d
-- -> make it primary key as it should be
--
-- Revision 1.15  2003/03/27 21:14:49  ncq
-- - cleanup, started work on Dutch structure
--
-- Revision 1.14  2003/01/20 20:10:12  ncq
-- - adapted to new i18n
--
-- Revision 1.13  2003/01/13 10:07:52  ihaywood
-- add free comment strings to script.
-- Start vaccination Hx tables
--
-- Revision 1.12  2003/01/05 13:05:51  ncq
-- - schema_revision -> gm_schema_revision
--
-- Revision 1.11  2002/12/22 01:26:16  ncq
-- - id_doctor -> id_provider + comment, typo fix
--
-- Revision 1.10  2002/12/14 08:55:17  ihaywood
-- new prescription tables -- fixed typos
--
-- Revision 1.9  2002/12/14 08:12:22  ihaywood
-- New prescription tables in gmclinical.sql
--
-- Revision 1.8  2002/12/06 08:50:51  ihaywood
-- SQL internationalisation, gmclinical.sql now internationalised.
--
-- Revision 1.7  2002/12/05 12:45:43  ncq
-- - added episode table, fixed typo
--
-- Revision 1.6  2002/12/01 13:53:09  ncq
-- - missing ; at end of schema tracking line
--
-- Revision 1.5  2002/11/23 13:18:09  ncq
-- - add "proper" metadata handling and schema revision tracking
--
