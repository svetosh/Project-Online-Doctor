#!/bin/python3
##############
#	"kantoku" in Japanese means supervisor, manager, director and etc.
#	
#	This program manages the database for the project Online Doctor
#
import tkinter as tk
from . import libodpdb as mdb

class Kantoku():
	main_window = tk.Tk()
	
	
	def mainloop(self):
		self.main_window.mainloop()

def test():
	a = Kantoku()
	a.mainloop()
