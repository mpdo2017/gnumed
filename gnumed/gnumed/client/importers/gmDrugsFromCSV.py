# creates SQL to imports a list of mono-component drugs from a CSV file

import sys
import codecs


# GNUmed
if __name__ == '__main__':
	sys.path.insert(0, '../../')
from Gnumed.pycommon import gmLog2
from Gnumed.pycommon import gmTools


field_names = [u'substance', u'brand', u'form', u'company', u'strength_1', u'strength_2', u'strength_3', u'always_empty', u'unit']
non_empty_fields = [u'substance', u'brand', u'form', u'company', u'strength_1', u'unit']
numeric_fields = [u'strength_1', u'strength_2', u'strength_3']


SQL_start = u"""-- ---------------------------------------------------------
-- data pack install script example
--
-- add a description here: Mono-substance drugs as available in India
-- license: GPL v2 or later, manually transferred 3rd party data
-- provided by Vaibhav Banait
--
-- http://wiki.gnumed.de/bin/view/Gnumed/GmManualReferenceData
-- ---------------------------------------------------------
-- enable this if running locally via
-- psql -d gnumed_vXX -U gm-dbo -f install-data-pack.sql
--SET default_transaction_read_only TO OFF;

-- ---------------------------------------------------------
-- drop staging tables if needed
\\unset ON_ERROR_STOP
DROP TABLE staging.india_drugs CASCADE;
\set ON_ERROR_STOP 1

-- ---------------------------------------------------------
-- run everything else in one transaction
BEGIN;

-- create staging tables as needed --
CREATE TABLE staging.india_drugs (
	brand_name text,
	substance text,
	form text,
	strength numeric,
	unit text
);

-- ---------------------------------------------------------
-- insert data in staging table
"""


SQL_stage_drug = u"""INSERT INTO staging.india_drugs (brand_name, substance, form, strength, unit) SELECT
	'%(brand_name)s',
	'%(substance)s',
	'%(form)s',
	gm.nullify_empty_string('%(strength)s')::numeric,
	'%(unit)s'
WHERE NOT EXISTS (
	SELECT 1 FROM staging.india_drugs WHERE brand_name = '%(brand_name)s'
);
"""


SQL_end = u"""-- ---------------------------------------------------------
-- transfer data to real tables

-- substances
INSERT INTO ref.consumable_substance (description, amount, unit) SELECT
	DISTINCT ON (s_id.substance, s_id.strength, s_id.unit)
	s_id.substance, s_id.strength, s_id.unit
FROM 
	staging.india_drugs s_id
WHERE
	s_id.strength IS NOT NULL
		AND
	NOT EXISTS (
		SELECT 1 FROM ref.consumable_substance r_cs WHERE
			r_cs.description = s_id.substance
				AND
			r_cs.amount = s_id.strength
				AND
			r_cs.unit = s_id.unit
	)
;

-- brands
INSERT INTO ref.branded_drug (description, preparation) SELECT
	s_id.brand_name, s_id.form
FROM
	staging.india_drugs s_id
WHERE NOT EXISTS (
	SELECT 1 FROM ref.branded_drug r_bd WHERE
		r_bd.description = s_id.brand_name
			AND
		r_bd.preparation = s_id.form
);

-- link components
INSERT INTO ref.lnk_substance2brand (fk_brand, fk_substance) SELECT
	(SELECT pk FROM ref.branded_drug r_bd
	 WHERE
		r_bd.description = s_id.brand_name
			AND
		r_bd.preparation = s_id.form
	),
	(SELECT pk FROM ref.consumable_substance r_cs WHERE
		r_cs.description = s_id.substance
			AND
		r_cs.amount = s_id.strength
			AND
		r_cs.unit = s_id.unit
	)
FROM
	staging.india_drugs s_id
WHERE NOT EXISTS (
	SELECT 1 FROM ref.lnk_substance2brand WHERE
		fk_brand = (
			SELECT pk FROM ref.branded_drug WHERE
				description = s_id.brand_name
					AND
				preparation = s_id.form
		)
			AND
		fk_substance = (
			SELECT pk FROM ref.consumable_substance r_cs WHERE
				r_cs.description = s_id.substance
					AND
				r_cs.amount = s_id.strength
					AND
				r_cs.unit = s_id.unit
		)
);

-- ---------------------------------------------------------
-- drop staging tables again, if needed --
\\unset ON_ERROR_STOP
DROP TABLE staging.india_drugs CASCADE;
\set ON_ERROR_STOP 1

-- ---------------------------------------------------------

-- finalize transaction --
-- uncomment this once you are satisfied your script works:
COMMIT;
-- ---------------------------------------------------------
"""

#---------------------------------------------------------------------------------------------------
def create_sql(filename):

	csv_file = codecs.open(filename = filename, mode = 'rUb', encoding = u'utf8')

	csv_lines = gmTools.unicode_csv_reader (
		csv_file,
		fieldnames = field_names,
		delimiter = ';',
		quotechar = '"',
		dict = True
	)

	print SQL_start

	line_idx = 0
	skip_line = False
	for line in csv_lines:
		line_idx += 1
		print "-- line #%s" % line_idx
		# normalize field content
		for field in field_names:
			try:
				line[field] = line[field].strip().strip(u';,').strip().replace(u"'", u"''")
			except AttributeError:		# trailing fields are a list
				pass
		# verify required fields
		for field in non_empty_fields:
			if line[field] == u'':
				print "-- ignoring line: empty field [%s]" % field
				print "--", line
				print ""
				skip_line = True
				break
		if skip_line:
			skip_line = False
			continue
		# verify numeric fields
		for field in numeric_fields:
			if line[field] == u'':
				continue
			success, num_val = gmTools.input2decimal(initial = line[field])
			if not success:
				print "-- ignoring line: field [%s] not numeric: >>>%s<<<" % (field, line[field])
				print "--", line
				print ""
				skip_line = True
				break
			line[field] = num_val
		if skip_line:
			skip_line = False
			continue

		# actually create SQL
		# loop over strengths
		for field in numeric_fields:
			if line[field] == u'':
				continue
			line['brand_name'] = (u'%%(brand)s %%(%s)s (%%(company)s)' % field) % line
			line['strength'] = line[field]
			print SQL_stage_drug % line

	print SQL_end

#---------------------------------------------------------------------------------------------------

create_sql(sys.argv[1])