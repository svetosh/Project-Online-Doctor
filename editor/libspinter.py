################################################################################
#
#	An interface library.
#
#	Codename:		Kankei (Connection)
# 	Version: 		0.1
# 	Description:	SWI-Prolog interface
#
################################################################################
class Fact():
	logic_op_begin = '' 
	predicate = ''
	parameters = []
	logic_op_end = ''
	
	def __init__(self, string = ''):
		if string != '':
			self.read(string)

	def write(self, ofile):
		todo = True
		
	def read(self, string):
		if string != '':
			closing_p = string.find(')')
			opening_p = string.rfind('(')
			self.parameters = string[opening_p + 1:closing_p].split(', ')
			i = 0
			while not(string[i].isalpha()):
				i+=1 
			self.predicate = string[i:opening_p]
			self.logic_op_begin = string[:i]
			self.logic_op_end = string[closing_p + 1:]
			print (self.logic_op_begin, self.predicate, self.parameters, self.logic_op_end)

class Rule():
	first_line = ''
	conditions = []
	
	def __init__(self, first_line, conditions = []):
		self.first_line = Fact(first_line)
		for i in conditions:
			self.conditions.append(Fact(i))
	def write(self, ofile):
		todo = True
	def read(self, ifile):
		todo = True
	def clear(self):
		first_line = ''
		conditions = []


