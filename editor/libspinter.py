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
Symptoms = '$Symptoms$'	# The only variable which will be present 
						# in changeable files except their headers 

class PParameters():  # parameters with autoparsing ##TODO
	plist = []
	
	def __init__(self, string = ''):
		self.parse(string)
	def parse(self, string):
		print(string)
		if string != '':
			self.plist = list(eval(string))
	def __str__(self):
		return str(self.plist).replace("'",'"').replace('"$','').replace('$"','')[1:-1]
	

class Fact():
	logic_op_from_begin = '' 
	predicate = ''
	params = [] ##PParameters()
	logic_op_from_end = ''
	
	def __init__(self, string = ''):
		self.logic_op_from_begin = '' 
		self.predicate = ''
		self.logic_op_from_end = ''
		self.params = PParameters('"nothing"')
		self.read(string)
		
	def read(self, string):
		if string != '':
			closing_p = string.find(')')
			opening_p = string.rfind('(')
			self.params.parse(string[opening_p + 1: closing_p])

			i = 0
			while not(string[i].isalpha()):
				i+=1 
			self.predicate = string[i:opening_p]
			self.logic_op_from_begin = string[:i]
			self.logic_op_from_end = string[closing_p + 1:]
					
	def __str__(self):
		return f"{self.logic_op_from_begin}{self.predicate}({self.params}){self.logic_op_from_end}"	
		
		
class Rule():
	first_line = ''
	conditions = []
	
	def __init__(self, first_line = '', conditions = []):
		self.conditions = conditions[:]
		if first_line != '':
			self.first_line = Fact(first_line)

	def __str__(self):
		string = str(self.first_line)
		for i in self.conditions:
			string += ENDL + INDENT
			string += str(i)
		return string
		
	def read(self, ifile):
		line = ''
		while line=='' or line.startswith('%'):
			line = ifile.readline().strip()
		fact = Fact(line)
		self.first_line = fact
		while (fact.logic_op_from_end != '.'):
			line = ''
			while line=='' or line.startswith('%'):
				line = ifile.readline().strip()
			fact = Fact(line)
			self.conditions.append(fact)

	def clear(self):
		self.first_line = ''
		self.conditions = []

# Testing
def test():
	r1 = Rule()
	r0 = Rule()
	ifile = open ('kbase_deseases.pl')
	l = ifile.readline()
	l = ifile.readline()
	l = ifile.readline()
	l = ifile.readline()
	r0.read(ifile)
	print(r0)
	r1.read(ifile)
	print(r1)
	print(r0)
	print(r1)
	r0.clear()
	print(r0)
	r1.clear()
	print(r1)
