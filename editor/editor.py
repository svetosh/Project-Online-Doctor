#!/bin/python3
##############
#	Codename: Kantoku
#
#	This program manages the database for the project Online Doctor
#
import tkinter as tk
from . import libeditor as db

class Kantoku():
	main_window = tk.Tk()
	
	
	def mainloop(self):
		self.main_window.mainloop()

def test():
	a = Kantoku()
	a.mainloop()
