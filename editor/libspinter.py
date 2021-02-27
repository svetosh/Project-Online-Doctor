################################################################################
#
#	An interface library.
#
#	Codename:		Kankei (Connection)
# 	Version: 		0.1
# 	Description:	SWI-Prolog interface
#
################################################################################
INDENT = '    '
ENDL = '\n'

class PParameters():  # parameters with autoparsing
	raw_sring = ''
	plist = []
	def __init__(self, string = ''):
		self.parse(string)  # an unnesessary thing, but maybe I'll need this
	def parse(self, string):  # ~some lite hardcoding was used~
		if string != '':
			self.raw_str = string
			self.plist = string[opening_p + 1:closing_p].split(',')
		else:
			raw_sring = ''
			tdict = dict()

class Fact():
	logic_op_begin = '' 
	predicate = ''
	parameters = PParameters()
	logic_op_end = ''
	
	def __init__(self, string = ''):
		self.read(string)
		
	def read(self, string):
		if string != '':
			closing_p = string.find(')')
			opening_p = string.rfind('(')
			parameters.parse(string)
			i = 0
			while not(string[i].isalpha()):
				i+=1 
			self.predicate = string[i:opening_p]
			self.logic_op_begin = string[:i]
			self.logic_op_end = string[closing_p + 1:]
			print (self.logic_op_begin, self.predicate, self.parameters, self.logic_op_end)
			
	def write(self, ofile):
		ofile.write(self.logic_op_begin + ' ')
		ofile.write(self.predicate + '(')
		parameters.write(ofile)
		ofile.write(')'+self.logic_op_end + ENDL)
		
		
class Rule():
	first_line = ''
	conditions = []
	
	def __init__(self, first_line, conditions = []):
		self.first_line = Fact(first_line)
		for i in conditions:
			self.conditions.append(Fact(i))

	def write(self, ofile):
		first_line.write(ofile)
		for i in conditions:
			ofile.write(INDENT)
			i.write(ofile)
		
	def read(self, ifile):
		todo = True

	def clear(self):
		first_line = ''
		conditions = []


