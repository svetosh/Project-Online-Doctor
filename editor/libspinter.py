################################################################################
#
#	An interface library. (TBD)
#
#	Codename:		Kankei (Connection)
# 	Version: 		0.1
# 	Description:	SWI-Prolog interface
#
################################################################################
INDENT = '    '
ENDL = '\n'
Symptoms = 'Symptoms'

class PParameters():  # parameters with autoparsing ##TODO
	plist = []
	
	def __init__(self, string = ''):
		self.parse(string)
	def parse(self, string):
		print(string)
		if string != '':
			self.plist = list(eval(string))
	def __str__(self):
		return str(self.plist).replace("'",'"')[1:-1]
	

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
			if ']' not in string: # some hardcoding was used
				self.params.parse(string[opening_p + 1:string.rfind('"') + 1])
			else:
				self.params.parse(string[opening_p + 1:string.rfind(']') + 1])

			i = 0
			while not(string[i].isalpha()):
				i+=1 
			self.predicate = string[i:opening_p]
			self.logic_op_from_begin = string[:i]
			self.logic_op_from_end = string[closing_p + 1:]
			# ~ print (self.logic_op_from_begin, 
					# ~ self.predicate, 
					# ~ self.params, 
					# ~ self.logic_op_from_end)
					
	def __str__(self):
		return f"{self.logic_op_from_begin}{self.predicate}({self.params}){self.logic_op_from_end}"	
		
		
class Rule():
	first_line = ''
	conditions = []
	
	# ~ def __init__(self, first_line, conditions = []):
		# ~ self.first_line = Fact(first_line)
		# ~ for i in conditions:
			# ~ self.conditions.append(Fact(i))

	def write(self, ofile):
		first_line.write(ofile)
		for i in conditions:
			ofile.write(ENDL + INDENT)
			ofile.write(i)
		
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
		first_line = ''
		conditions = []


