#
#	"kantoku" in Japanese means supervisor, manager, director and etc.
#	

from . import libspinter as spinter # SWI-Prolog interface

class PrologDatabase():
	database_name = 'Database'
	symp2dis_terms = []
	dis2doct_terms = []
	registry = ComplexTerm('назначить_raw(Симптомы,Врачи):-')

	def write_db(self):
		ofile = open (database_name+'.s2d.pl')
		for i in self.symp2dis_terms:
			i.write(ofile)
		ofile.close()
		
		ofile = open (database_name+'.d2d.pl')
		for i in self.dis2doct_terms:
			i.write(ofile)
		registry.write(ofile)
		ofile.close()
		

	def read_db(self):
		b=9
