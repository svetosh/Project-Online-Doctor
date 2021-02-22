################################################################################
#	An offline editor for the database.
#
#	Codename:		Kantoku
#	Version:		0.1
#	Description:	This offline program manages the database 
#					for the project Online Doctor.
#
#	Short note:
#	"kantoku" in Japanese means supervisor, manager, director and etc.		
#																			   
################################################################################

import tkinter as tk
from . import libeditor as db

class Kantoku():
	main_window = tk.Tk()
	
	
	def mainloop(self):
		self.main_window.mainloop()

def test():
	a = Kantoku()
	a.mainloop()
