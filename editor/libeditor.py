################################################################################
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
	symp_categories = Term('категории_симптомов().')
	symp_lists = [] # a list of Term-s
	symp2dis_terms = []
	dis2doct_terms = []
	registry = ComplexTerm('назначить_raw(Симптомы,Врачи):-')

	def write_db(self):
		
		
		ofile = open (database_name+'.slc.pl')
		symp_categories.write(ofile) 
		ofile.close()
		
		ofile = open (database_name+'.csl.pl')
		for i in self.symp_lists:
			i.write(ofile)
		ofile.close()
		
		ofile = open (database_name+'.s2d.pl')
		for i in self.symp2dis_terms:
			i.write(ofile)
		ofile.close()
		
		ofile = open (database_name+'.d2d.pl')
		for i in self.dis2doct_terms:
			i.write(ofile)
		ofile.close()
		
		ofile = open (database_name+'.reg.pl')
		registry.write(ofile)
		ofile.close()
		
	def read_db(self):
		
