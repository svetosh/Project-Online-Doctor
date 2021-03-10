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

class PrologFile():
	filename = ''
	header = []  # a list of facts not visible for a user
	rules = []
	
	def read(self):
		ifile = open (filename + '.pl')
		
		header_len = ifile.readline().strip()[1:]
		for i in range(header_len):
			header.append(Fact(ifile.readline().strip()))  # reading header
			
		line = ifile.readline().strip()
		buffer_rule = Rule()
		while line!='':
			buffer_fact = Fact(line)
			if buffer_fact.log_op_end == '-:':
				buffer_rule.first_line = buffer_fact
			else:
				buffer_rule.conditions.append(buffer_fact)  # reading rules
				if buffer_fact.log_op_end == '.':
					rules.append(buffer_rule)
					buffer_rule.clear()
			line = ifile.readline().strip()
		
		ifile.close()
		
	def write(self):
		ofile = open (filename + 'test.pl','w')
		ofile.write('%'+len(self.header))
		for i in header:
			i.write(ofile)
		for i in rules:
			i.write(ofile)
		ofile.close()

class PrologDatabase():
	symp_lists = SymBase()
	dis_classes = DisBase()  # these should be derived classes from PrologFile
	doc_register = DocBase()

	def write_db(self):
		todo = True
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
