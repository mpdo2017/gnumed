-- ==============================================================
-- GNUmed database schema change script
--
-- License: GPL
-- Author: karsten.hilbert@gmx.net
-- 
-- ==============================================================
\set ON_ERROR_STOP 1

-- --------------------------------------------------------------
create schema staging authorization "gm-dbo";

-- --------------------------------------------------------------
CREATE TABLE staging.lab_request (
    pk integer primary key,
    fk_incoming_data_unmatched integer,
    fk_test_org integer,
    request_id text,
    fk_requestor integer,
    orig_requestor text,
    lab_request_id text,
    lab_rxd_when timestamp with time zone,
    results_reported_when timestamp with time zone,
    request_status text,
    is_pending boolean,
    diagnostic_service_section text,
    ordered_service text
) INHERITS (clin.clin_root_item);

-- --------------------------------------------------------------
CREATE TABLE staging.test_result (
    pk integer primary key,
    fk_type integer,
    fk_request integer,
    val_num numeric,
    val_alpha text,
    val_unit text,
    val_normal_min numeric,
    val_normal_max numeric,
    val_normal_range text,
    val_target_min numeric,
    val_target_max numeric,
    val_target_range text,
    abnormality_indicator text,
    norm_ref_group text,
    note_test_org text,
    material text,
    material_detail text,
    fk_intended_reviewer integer,
    orig_intended_reviewer text
) INHERITS (clin.clin_root_item);

-- --------------------------------------------------------------
select gm.log_script_insertion('v15-staging-hl7-static.sql', 'Revision: 1.1');
