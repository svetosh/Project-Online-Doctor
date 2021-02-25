################################################################################
#
#	A library for the editor.
#
#	Codename:		Kikai
#	Version:		0.1
#	Description:	This is a module (an 'instrument') to manage the DB.
#
#	Short note:
#	"kikai" means machine, mechanism, instrument and etc.
#	
################################################################################

from . import libspinter as spinter # SWI-Prolog interface

class PrologDatabase():
	database_name = 'Database'
	symp_lists = dict()		# a dictionary of Term-s
	symp2dis_terms = []
	dis2doct_terms = []

	def write_db(self):
		ofile = open (database_name+'.slc.pl')
		
		ofile.close()

	def read_db(self):
		todo = True
#####################################
	def add_sl_category(self):
		todo = True

	def del_sl_category(self):
		todo = True

	def add_symptom_to_list(self):
		todo = True

	def del_symptom_from_list(self):
		todo = True
#####################################
	def add_dis_class_to_s2d(self):
		todo = True

	def del_dis_class_from_s2d(self):
		todo = True

	def add_symptom_to_class(self):
		todo = True

	def del_symptom_from_class(self):
		todo = True
#####################################
	def add_doctor_to_d2d(self):
		todo = True

	def del_doctor_from_d2d(self):
		todo = True
		
	def add_dis_class_to_doctor(self):
		todo = True

	def del_dis_class_from_doctor(self):
		todo = True
######################################

#	def (self):
#		todo = True
#
#	def (self):
#		todo = True
