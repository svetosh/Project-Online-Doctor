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
class ache(): # Deprecated
	category = ''
	sympt_num = 0
	def __init__(self, cat, num):
		self.category = cat
		sympt_num = num

class Dclass(): # Deprecated
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
	
class Doctor(): # Deprecated
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
	# will use sqlite3 database in RAM
	TODO = True
