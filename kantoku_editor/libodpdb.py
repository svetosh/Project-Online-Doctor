class PTermInput():
	variables = []
	def __init__(self, string = ''):
		self.variables = string.split(',')
		
class Term():
	logic_op_0 = '' 
	predicate = ''
	pinput = ''
	logic_op_1 = ''
	def __init__(self, string = ''):
		if string != '':
			closing_p = string.find(')')
			opening_p = string.rfind('(')
			self.pinput = PTermInput(string[opening_p + 1:closing_p])
			i = 0
			while not(string[i].isalpha()):
				i+=1 
			self.predicate = string[i:opening_p]
			self.logic_op_0 = string[:i]
			self.logic_op_1 = string[closing_p + 1:]
			print (self.logic_op_0, self.predicate, self.pinput.variables, self.logic_op_1)
			

class ComplexTerm():
	first_line = ''
	conditions = []
	
	def __init__(self, first_line_term, conditions = []):
		self.first_line = Term(first_line_term)
		for i in conditions:
			self.conditions.append(Term(i))
			

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


fcking_term = ComplexTerm('назначить_raw(Симптомы,Врачи):-', ['знa(птоы,и);','\+наw(Сим,ачи).'])
