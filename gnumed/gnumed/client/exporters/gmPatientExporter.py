"""GnuMed simple ASCII EMR export tool.

TODO:
- GUI mode:
  - post-0.1 !
  - allow user to select patient
  - allow user to pick episodes/encounters/etc from list
- output modes:
  - HTML - post-0.1 !
"""
#============================================================
# $Source: /home/ncq/Projekte/cvs2git/vcs-mirror/gnumed/gnumed/client/exporters/gmPatientExporter.py,v $
# $Id: gmPatientExporter.py,v 1.19 2004-07-03 17:15:59 ncq Exp $
__version__ = "$Revision: 1.19 $"
__author__ = "Carlos Moro"
__license__ = 'GPL'

import sys, traceback, string, types

from Gnumed.pycommon import gmLog, gmPG, gmI18N, gmCLI, gmCfg, gmExceptions
from Gnumed.business import gmClinicalRecord, gmPatient, gmAllergy, gmVaccination, gmPathLab, gmMedDoc
from Gnumed.pycommon.gmPyCompat import *

# 3rd party
import mx.DateTime.Parser as mxParser

if __name__ == "__main__":
	gmLog.gmDefLog.SetAllLogLevels(gmLog.lData)

_log = gmLog.gmDefLog
_log.Log(gmLog.lInfo, __version__)
_cfg = gmCfg.gmDefCfgFile
#============================================================
def prompted_input(prompt, default=None):
	usr_input = raw_input(prompt)
	if usr_input == '':
		return default
	return usr_input
#--------------------------------------------------------
class cEmrExport:
	def __init__(self, constraints = None):
		"""Default constructor.

		constraints - Exporter constraints for filtering clinical items
		"""
		if constraints is None:
		    # default constraints to None for complete emr dump
			self.__constraints = {
				'since': None,
				'until': None,
				'encounters': None,
				'episodes': None,
				'issues': None
			}
		else:
			self.__constraints = constraints
		self.__patient = None
		self.lab_new_encounter = True
	#--------------------------------------------------------
	def set_constraints(self, constraints = None):
		"""Sets exporter constraints.

		constraints - Exporter constraints for filtering clinical items
		"""
		if constraints is None:
		    # default constraints to None for complete emr dump
			self.__constraints = {
				'since': None,
				'until': None,
				'encounters': None,
				'episodes': None,
				'issues': None
			}
		else:
			self.__constraints = constraints
		return True
	#--------------------------------------------------------
	def get_constraints(self):
	    """
        Retrieve exporter constraints
	    """
	    return self.__constraints
	#--------------------------------------------------------
	def set_patient(self, patient=None):
	    """
            Sets exporter patient
            
            patient - Patient whose data are to be dumped
	    """
	    if patient is None:
	        _log.Log(gmLog.lErr, "can't set None patient for exporter")
	        return
	    self.__patient = patient
	#--------------------------------------------------------
	def get_patient():
	    """
            Retrieves patient whose data are to be dumped
	    """
	    return self.__patient
	#--------------------------------------------------------
	def cleanup(self):
		"""
            Exporter class cleanup code
		"""
		pass
	#--------------------------------------------------------
	def get_vaccination_for_cell(self, vaccs, date, field, text = None):
		"""
		Checks if a cell matchs a pair vaccination indication - date. It it happends, returns the appropiate text to display
		vaccs - list of vaccination items
		date  - date to check
		text  - text to display in the cell if there's a match vaccination indication - date
		field - name of the field in vaccination item that contains the adecuate date		
		"""
		for a_vacc in vaccs:
			if  a_vacc[field].Format('%Y-%m-%d') == date:
				if text == None:
					return a_vacc['batch_no']
				if text == 'DUE':
				    if a_vacc['overdue'] == True:
				        text = 'OVERDUE  '
				    else:
				        text = 'DUE      '
				return text
		return None				
	#--------------------------------------------------------
	def get_vacc_table(self,emr):
		"""
		Retrieves string containg ASCII vaccination table
		emr - patient's electronic medical record
		"""		
		# Retrieve all patient vaccination items
		vaccinations = []
		vaccinations.extend(emr.get_vaccinations())
		due_vaccs = emr.get_missing_vaccinations()
		vaccinations.extend(due_vaccs['due'])
		vaccinations.extend(due_vaccs['boosters'])
		#print "Total vaccination items : %i" % len(vaccinations)
		
		# Retrieve all vaccination indications
		vacc_indications = []
		status, v_indications = gmVaccination.get_indications_from_vaccinations(vaccinations)
		for v_ind in v_indications:
			if v_ind[0] not in vacc_indications:
				vacc_indications.append(v_ind[0])
				#print v_ind[0]
		vacc_indications.sort()
		#print "Total vaccination indications : %i " % len(vacc_indications)
		#print ""
		
		# Get list of vaccination dates
		#print "Dates: "
		total_vacc_dates = []
		for a_vacc in vaccinations:
			try:
				a_date = a_vacc['date'].Format('%Y-%m-%d')
			except:
				a_date = a_vacc['latest_due'].Format('%Y-%m-%d')
			if not a_date in total_vacc_dates:
				total_vacc_dates.append(a_date)
				#print a_date
		total_vacc_dates.sort()
		#print "Total vaccination dates : %i " % len(total_vacc_dates)
		#print ""
		
		# Number of partial tables to display, depending on the number of dates (columns)
		table_count = int(len(total_vacc_dates) / 5)
		if len(total_vacc_dates) % 5 > 0:
			table_count += 1
		#print "Number of tables to display: %i " % table_count
		
		txt = ''
		for cont in range(table_count):
			start = cont*5
			end = (cont+1)*5
			if end > len(total_vacc_dates):
				end = len(total_vacc_dates)
			vacc_dates = total_vacc_dates[start:end]
			# Get max indication str length
			max_indication_length = -1
			for an_indication in vacc_indications:
				if len(an_indication) > max_indication_length:
					max_indication_length = len(an_indication)
			max_indication_length +=3
			# Get date field length
			column_length = len(vacc_dates[0]) 
			# Print table header (column dates)
			txt += '\n\n'
			txt += ' '*max_indication_length + '|'
			for a_date in vacc_dates:
				txt+= str(a_date) + "\t|"
			txt += '\n'
			# Print rows
			for an_indication in vacc_indications:
				row_column = 0
				txt+= an_indication + " "*(max_indication_length-len(an_indication)) + "|"
				for a_date in vacc_dates:
					cell_txt = self.get_vaccination_for_cell(emr.get_vaccinations(indications = [an_indication]), a_date, 'date')
					if cell_txt is None:
						cell_txt = self.get_vaccination_for_cell(emr.get_missing_vaccinations(indications = [an_indication])['due'], a_date, 'latest_due', 'DUE')
					if cell_txt is None:
						cell_txt = self.get_vaccination_for_cell(emr.get_missing_vaccinations(indications = [an_indication])['boosters'], a_date, 'latest_due', '*DUE    ')					
					if cell_txt is not None:
						txt += cell_txt + '\t|'									
					else:
						txt+= ' '*column_length + '\t|'
				txt += '\t\n'    		
					
		return txt
    #--------------------------------------------------------
	def get_encounters_for_items(self, emr, items):
	    """
            Extracts and retrieves encounters for a list of items
            emr - Patient's electronic clinical record
            items - Items whose  encounters are to be obtained
	    """
	    encounter_ids = []
	    for an_item in items:
	        try :
	            encounter_ids.append(an_item['pk_encounter'])
	        except:
	            encounter_ids.append(an_item['pk_encounter'])
	    return emr.get_encounters(id_list = encounter_ids)
	#--------------------------------------------------------
	def dump_item_fields(self, offset, item, field_list):
	    """
            Dump information related to the fields of a clinical item
            offset - Number of left blank spaces
            item - Item of the field to dump
            fields - Fields to dump
	    """
	    txt = ''
	    for a_field in field_list:
	        txt += offset*' ' + a_field + (20-len(a_field))*' ' + ':\t' + str(item[a_field]) + '\n'
	    return txt
	#--------------------------------------------------------
	def get_allergy_output(self, allergy):
	    """
            Dumps allergy item data
            allergy - Allergy item to dump
	    """
	    txt = ''
	    txt += 12*' ' + 'Allergy: \n'
	    txt += self.dump_item_fields(15, allergy, ['allergene', 'substance', 'generic_specific','l10n_type', 'definite', 'reaction'])
	    return txt
	#--------------------------------------------------------
	def get_vaccination_output(self, vaccination):
	    """
            Dumps vaccination item data
            vaccination - Vaccination item to dump
	    """
	    txt = ''
	    txt += 12*' ' + 'Vaccination: \n'
	    txt += self.dump_item_fields(15, vaccination, ['l10n_indication', 'vaccine', 'batch_no', 'site', 'narrative'])	    
	    return txt
	#--------------------------------------------------------
	def get_lab_result_output(self, lab_result):
	    """
            Dumps lab result item data
            lab_request - Lab request item to dump
	    """
	    txt = ''
	    if self.lab_new_encounter:
	        txt += 12*' ' + 'Lab result: \n'
	    txt += 15*' ' + lab_result['unified_name'] + (20-len(lab_result['unified_name']))*' ' + ':\t' + lab_result['unified_val']+ ' ' + lab_result['val_unit'] + '(' + lab_result['material'] + ')' + '\n'
	    return txt
	#--------------------------------------------------------
	def get_item_output(self, item):
	    """
            Obtains formatted clinical item output dump
            item - The clinical item to dump
	    """
	    txt = ''
	    if isinstance(item, gmAllergy.cAllergy):
	        txt += self.get_allergy_output(item)
	    elif isinstance(item, gmVaccination.cVaccination):
	        txt += self.get_vaccination_output(item)
	    elif isinstance(item, gmPathLab.cLabResult):
	        txt += self.get_lab_result_output(item)
	        self.lab_new_encounter = False
	    return txt
	#--------------------------------------------------------
	def get_filtered_items(self, emr = None):
		"""
            Retrieve patient clinical items filtered by multiple constraints
            
            emr - patient's electronic medical record
		"""
		filtered_items = []
		filtered_items.extend(emr.get_allergies(
			since=self.__constraints['since'],
			until=self.__constraints['until'],
			encounters=self.__constraints['encounters'],
			episodes=self.__constraints['episodes'],
			issues=self.__constraints['issues']))
		filtered_items.extend(emr.get_vaccinations(
			since=self.__constraints['since'],
			until=self.__constraints['until'],
			encounters=self.__constraints['encounters'],
			episodes=self.__constraints['episodes'],
			issues=self.__constraints['issues']))
		filtered_items.extend(emr.get_lab_results(
			since=self.__constraints['since'],
			until=self.__constraints['until'],
            encounters=self.__constraints['encounters'],
			episodes=self.__constraints['episodes'],
			issues=self.__constraints['issues']))
		return filtered_items
	#--------------------------------------------------------
	def get_set_for_field(self, list_values, field):
	    """
            Extract set of unique values of a desired field from list
            
            list_values - List of items to iterate
            field - Field for which each unique value must be extracted
	    """
	    set_values = []
	    for a_value in list_values:
	        if a_value[field] not in set_values:
	            set_values.append(a_value[field])
	    return set_values
	#--------------------------------------------------------
	def get_historical_tree(self, emr = None):
	    """
	    Dumps patient's historical in form of a tree of health issues
	                                                    -> episodes
	                                                       -> encounters
	                                                          -> clinical items
	                                                          
	    emr - patient's electronic medical record
	    """
	    
	    # Let's fetch all items compliant with constraints
	    filtered_items = self.get_filtered_items(emr)
	    # Extract from considered items related health issues
	    filtered_issues = self.get_set_for_field(filtered_items, 'pk_health_issue')
	    # Extract from considered items related episodes
	    filtered_episodes = self.get_set_for_field(filtered_items, 'pk_episode')
	    # Extract from considered items related encounters
	    filtered_encounters = self.get_set_for_field(filtered_items, 'pk_encounter')
	    
	    # All values fetched and filtered, we can begin with the tree
	    txt = ''
	    h_issues = emr.get_health_issues(id_list = filtered_issues)
	    for h_issue in h_issues:
	        txt += '\n' + 3*' ' + 'Health Issue: ' + h_issue['description'] + '\n'
	        for an_episode in emr.get_episodes(id_list=filtered_episodes, issues = [h_issue['id']]):
	           txt += '\n' + 6*' ' + 'Episode: ' + an_episode['description'] + '\n'
	           items =  filter(lambda item: item['pk_episode'] in [an_episode['pk_episode']], filtered_items)
	           encounters = self.get_encounters_for_items(emr, items)
	           for an_encounter in encounters:
                    self.lab_new_encounter = True
                    txt += '\n' + 9*' ' + 'Encounter, ' + an_encounter['l10n_type'] + ': ' + an_encounter['started'].Format('%Y-%m-%d') + ' to ' + \
                    an_encounter['last_affirmed'].Format('%Y-%m-%d') + ' ' + \
                    '"' + an_encounter['description'] + '"\n'
                    for an_item  in items:
                        if an_item['pk_encounter'] == an_encounter['pk_encounter']:
                            txt += self.get_item_output(an_item)
	    return txt
	#--------------------------------------------------------
	def dump_clinical_record(self):
		"""
		Dumps in ASCII format patient's clinical record
		
		"""
		emr = self.__patient.get_clinical_record()
		if emr is None:
			_log.Log(gmLog.lErr, 'cannot get EMR text dump')
			print(_(
				'An error occurred while retrieving a text\n'
				'dump of the EMR for the active patient.\n\n'
				'Please check the log file for details.'
			))
			return None
		txt ='\n'
		txt += 'Overview\n'
		txt += '--------\n'
		
		txt += "1) Allergy status (for details, see below):\n\n"
		for allergy in 	emr.get_allergies():
			txt += "   " + allergy['descriptor'] + "\n"
		txt += "\n"
		
		txt += "2) Vaccination status (* indicates booster):\n"
		txt += self.get_vacc_table(emr)
		
		txt += "\n3) Historical:\n\n"
		txt += self.get_historical_tree(emr)

		try:
			emr.cleanup()
		except:
			print "error cleaning up EMR"
			
		return txt	    
	#--------------------------------------------------------
	def dump_med_docs(self):
	    """
            Dumps patient stored medical documents

	    """
	    doc_folder = self.__patient.get_document_folder()
	    doc_ids = doc_folder.get_doc_list()
	    txt = '\n'
	    txt += '4) Medical documents: (date) reference - type "comment"\n'
	    txt += '                         object - comment'
	    for doc_id in doc_ids:
	        med_doc = gmMedDoc.gmMedDoc(aPKey = doc_id)
	        doc_metadata = med_doc.get_metadata()
	        txt += '\n\n' + 3*' ' + \
	        '(' + doc_metadata['date'].Format('%Y-%m-%d') + ') ' + doc_metadata['reference'] +\
	        ' - ' + doc_metadata['type']+ ' "' + doc_metadata['comment'] + '"'
	        for objKey in doc_metadata['objects'].keys():
	            txt += '\n' + 6*' ' + str(doc_metadata['objects'][objKey]['index']) + '-' +\
	            doc_metadata['objects'][objKey]['comment']
	    txt += '\n\n'
	    return txt
	#--------------------------------------------------------    
	def dump_demographic_record(self, all = False):
		"""
            Dumps in ASCII format some basic patient's demographic data
            
		"""
		demo = self.__patient.get_demographic_record()
		dump = demo.export_demographics(all)
		if demo is None:
			_log.Log(gmLog.lErr, 'cannot get Demographic export')
			print(_(
				'An error occurred while Demographic record export\n'
				'Please check the log file for details.'
			))
			return None

		txt = '\n\n\nDemographics'
		txt += '\n------------\n'
		txt += '   Id: ' + str(dump['id']) + '\n'
		for name in dump['names']:
			if dump['names'].index(name) == 0:
				txt += '   Name (Active): ' + name['first'] + ', ' + name['last'] + '\n'
			else:
				txt += '   Name ' + dump['names'].index(name) + ': ' + name['first'] + ', ' +  name['last'] + '\n'
		txt += '   Gender: ' + dump['gender'] + '\n'
		txt += '   Title: ' + dump['title'] + '\n'
		txt += '   Dob: ' + dump['dob'] + '\n'
		txt += '   Medical age: ' + dump['mage'] + '\n'
		addr_types = dump['addresses'].keys()
		for addr_t in addr_types:
			addr_lst = dump['addresses'][addr_t]
			for address in addr_lst:
				txt += '   Address (' + addr_t + '): ' + address + '\n'
		return txt
	#--------------------------------------------------------    
	def dump_constraints(self):
	    """
            Dumps exporter filtering constraints
	    """
	    txt = ''
	    self.__first_constraint = True
	    
	    if not self.__constraints['since'] is None:
	        txt += self.dump_constraints_header()
	        txt += '\nSince: %s' % self.__constraints['since'].Format('%Y-%m-%d')
	    
	    if not self.__constraints['until'] is None:
	        txt += self.dump_constraints_header()
	        txt += '\nUntil: %s' % self.__constraints['until'].Format('%Y-%m-%d')
	    
	    if not self.__constraints['encounters'] is None:
	        txt += self.dump_constraints_header()
	        txt += '\nEncounters: '
	        for enc in self.__constraints['encounters']:
	            txt += str(enc) + ' '
	    
	    if not self.__constraints['episodes'] is None:
	        txt += self.dump_constraints_header()
	        txt += '\nEpisodes: '
	        for epi in self.__constraints['episodes']:
	            txt += str(epi) + ' '
	    
	    if not self.__constraints['issues'] is None:
	        txt += self.dump_constraints_header()
	        txt += '\nIssues: '
	        for iss in self.__constraints['issues']:
	            txt += str(iss) + ' '
	    
	    return txt
	#--------------------------------------------------------    
	def dump_constraints_header(self):
	    """
            Dumps constraints header
	    """
	    head_txt = ''
	    if self.__first_constraint == True:
	        head_txt = '\nClinical items dump constraints\n'
	        head_txt += '-'*(len(head_txt)-2)
	        self.__first_constraint = False
	    return head_txt
#============================================================
# main
#------------------------------------------------------------
def usage():
	"""
        Prints application usage options to stdout.
	"""
	print 'usage: python gmPatientExporter [--fileout=<outputfilename>] [--conf-file=<file>]'
	sys.exit(0)
#------------------------------------------------------------
def parse_constraints():
    """
        Obtains, parses and normalizes config file options
    """
    
    # Check conf file was defined
    if not gmCLI.has_arg('--conf-file'):
        usage()
        
    # Retrieve options
    cfg_group = 'constraints'
    constraints = {
        'since': _cfg.get(cfg_group, 'since'),
        'until': _cfg.get(cfg_group, 'until'),
        'encounters': _cfg.get(cfg_group, 'encounters'),
        'episodes': _cfg.get(cfg_group, 'episodes'),
        'issues': _cfg.get(cfg_group, 'issues')
    }

    # Normalice null constraints (None is interpreted as non existing constraint along all methods)
    for a_constraint in constraints.keys():
        if len(constraints[a_constraint]) == 0:
            constraints[a_constraint] = None
    
    # Cast existing constraints to correct type
    if not constraints['since'] is None:
        constraints['since'] = mxParser.DateFromString(constraints['since'], formats= ['iso'])
    if not constraints['until'] is None:
        constraints['until'] = mxParser.DateFromString(constraints['until'], formats= ['iso'])
    if not constraints['encounters'] is None:
        constraints['encounters'] = map(lambda encounter: int(encounter), constraints['encounters'])
    if not constraints['episodes'] is None:
        constraints['episodes'] = map(lambda episode: int(episode), constraints['episodes'])
    if not constraints['issues'] is None:
        constraints['issues'] = map(lambda issue: int(issue), constraints['issues'])
    
    return constraints
#------------------------------------------------------------		        
def run():
	"""
        Main module application execution loop.
	"""
	# Check that output file name is defined and create an instance of exporter
	if gmCLI.has_arg('--fileout'):
		outFile = open(gmCLI.arg['--fileout'], 'wb')
	else:
		usage()
	export_tool = cEmrExport(parse_constraints())
	
	# More variable initializations
	patient = None
	patient_id = None
	patient_term = None
	pat_searcher = gmPatient.cPatientSearcher_SQL()

	# App execution loop
	while patient_term != 'bye':
	    
		# Ask patient to dump and set in exporter object
		patient_term = prompted_input("\nPatient search term (or 'bye' to exit) (eg. Kirk): ")
		if patient_term == 'bye':
			break
		search_ids = pat_searcher.get_patient_ids(search_term = patient_term)
		if search_ids is None or len(search_ids) == 0:
			prompted_input("No patient matches the query term. Press any key to continue.")
			continue
		elif len(search_ids) > 1:
			prompted_input("Various patients match the query term. Press any key to continue.")
			continue
		patient_id = search_ids[0]
		patient = gmPatient.gmCurrentPatient(patient_id)
		export_tool.set_patient(patient)
		
		# Dump patient EMR sections
		chunk = ''
		chunk = export_tool.dump_constraints()
		print chunk
		outFile.write('\n' + chunk)
		
		chunk = export_tool.dump_demographic_record(True)
		print chunk
		outFile.write('\n' + chunk)
		
		chunk = export_tool.dump_clinical_record()
		print chunk
		outFile.write('\n' + chunk)
		
		chunk = export_tool.dump_med_docs()
		print chunk
		outFile.write('\n' + chunk)

	# Clean ups
	outFile.close()
	export_tool.cleanup()
	if patient is not None:
		try:
			patient.cleanup()
		except:
			print "error cleaning up patient"
			
#------------------------------------------------------------
if __name__ == "__main__":
    
	print "\n\nGnumed Simple EMR ASCII Export Tool"
	print "==================================="

	if gmCLI.has_arg('--help'):
		usage()

	gmPG.set_default_client_encoding('latin1')
	# make sure we have a connection
	pool = gmPG.ConnectionPool()
	# run main loop
	try:
		run()
	except StandardError:
		_log.LogException('unhandled exception caught', sys.exc_info(), verbose=1)
	try:
		pool.StopListeners()
	except:
		_log.LogException('unhandled exception caught', sys.exc_info(), verbose=1)
#============================================================
# $Log: gmPatientExporter.py,v $
# Revision 1.19  2004-07-03 17:15:59  ncq
# - decouple contraint/patient/outfile handling
#
# Revision 1.18  2004/07/02 00:54:04  ncq
# - constraints passing cleanup by Carlos
#
# Revision 1.17  2004/06/30 12:52:36  ncq
# - cleanup
#
# Revision 1.16  2004/06/30 12:43:10  ncq
# - read opts from config file, cleanup
#
# Revision 1.15  2004/06/29 08:16:35  ncq
# - take output file from command line
# - *search* for patients, don't require knowledge of their ID
#
# Revision 1.14  2004/06/28 16:15:56  ncq
# - still more faulty id_ found
#
# Revision 1.13  2004/06/28 15:52:00  ncq
# - some comments
#
# Revision 1.12  2004/06/28 12:18:52  ncq
# - more id_* -> fk_*
#
# Revision 1.11  2004/06/26 23:45:50  ncq
# - cleanup, id_* -> fk/pk_*
#
# Revision 1.10  2004/06/26 06:53:25  ncq
# - id_episode -> pk_episode
# - constrained by date range from Carlos
# - dump documents folder, too, by Carlos
#
# Revision 1.9  2004/06/23 22:06:48  ncq
# - cleaner error handling
# - fit for further work by Carlos on UI interface/dumping to file
# - nice stuff !
#
# Revision 1.8  2004/06/20 18:50:53  ncq
# - some exception catching, needs more cleanup
#
# Revision 1.7  2004/06/20 18:35:07  ncq
# - more work from Carlos
#
# Revision 1.6  2004/05/12 14:34:41  ncq
# - now displays nice vaccination tables
# - work by Carlos Moro
#
# Revision 1.5  2004/04/27 18:54:54  ncq
# - adapt to gmClinicalRecord
#
# Revision 1.4  2004/04/24 13:35:33  ncq
# - vacc table update
#
# Revision 1.3  2004/04/24 12:57:30  ncq
# - stop db listeners on exit
#
# Revision 1.2  2004/04/20 13:00:22  ncq
# - recent changes by Carlos to use VO API
#
# Revision 1.1  2004/03/25 23:10:02  ncq
# - gmEmrExport -> gmPatientExporter by Carlos' suggestion
#
# Revision 1.2  2004/03/25 09:53:30  ncq
# - added log keyword
#
