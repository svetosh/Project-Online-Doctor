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

#from . import libspinter as spinter # SWI-Prolog interface
class ache():
	category = ''
	sympt_num = 0
	def __init__(self, cat, num):
		self.category = cat
		sympt_num = num

class Dclass():
	name = ''
	aches = []
	def __init__(self, name = '', vec[]):
		self.name = name
		self.aches = vec[:]
	def __eq__(self, other):
		return self.name==other.name
	def get_aches(self):
		return self.aches
	def add_ache(self, cat, num):
		self.aches.append(ache(cat, num))
	def remove_ache(self, pos):
		self.aches.pop(pos)
	
class Doctor():
	name = ''
	dclasses = [] # daclasses id from all_dclasses
	def __init__(self, name = '', vec = []):
		self.name = name
		self.dclasses = vec[:]
	def __eq__(self, other):
		return self.name==other.name
	def get_dclasses(self):
		return self.dclasses
	def add_dclass(self, dclass_id):
		self.dclasses.append(dclass_id)
	def remove_dclass(self, pos):
		self.dclasses.pop(pos)

class DataBase():
	sympt_lists = dict() # {'category':['list', ..., 'list'], ...}
	all_dclasses = []
	all_doctors = []
	def add_category_to_db(self, name):
		if cat not in self.sympt_lists:
			self.sympt_lists[cat] = []
	def add_sympt_to_db(self, cat, name):
		if cat in self.sympt_lists:
			self.sympt_lists[cat].append(name)
		else:
			print('Error')
			
	def add_dclass_to_db(self, name):
		newDclass = Dclass(name)
		if newDclass not in self.all_dclasses:
			self.all_dclasses.append(newDclass)
	def add_doctor_to_db(self, name):
		newDoctor = Doctor(name)
		if newDoctor not in self.all_doctors:
			self.all_doctors.append()
