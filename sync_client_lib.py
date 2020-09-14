import  ftplib

class BinaryBuffer:
	####################################################################
	#
	# internal class
	# внутренний класс
	#
	####################################################################
	BinaryData=bytes()
	
	def Write(self,BinaryData):
		self.BinaryData=bytes(BinaryData)
		
	def SaveToFile(self,FileName):
		savefile = open(FileName,'wb')
		savefile.write(self.BinaryData)
		savefile.close()

class FTPConnection:
	####################################################################
	#
	# Класс для работы с ftplib (стандартный модуль)
	#
	####################################################################
	Server=''
	Login=''
	Password=''
	Connection=""
	BinBuf=BinaryBuffer()
	
	def __init__(self,Login='',Password='',Server='localhost'): 
		# Инициализации класса 
		self.Login = Login
		self.Password = Password
		self.Server = Server # сервер по умолчанию - localhost
		
	def Connect(self):
		# открытие соединения (подключение к серверу)
		try: 
			try: # тут попытка обойти возможные ошибки при подключении
				self.Connection=ftplib.FTP(self.Server,self.Login,self.Password)
				return 0
			except ftplib.error_perm:
				print ("Error in user data.")
				return 7
		except ConnectionRefusedError:
			print("Can't connect, check server data.")
			
	def Disconnect(self): 
		# закрытие соединения (отключение от сервера)
		self.Connection.quit() 
		print("Disconnected.")
		
	def ListDir(self):
		# вывод содержимого директории 
		return self.Connection.retrlines('LIST')
		
	def ChangeDir(self,WantedDir):
		# Смена директории директорию
		self.Connection.cwd(WantedDir)
		
	def GetFile(self, FileName):
		# Получение файла
		self.Connection.retrbinary('RETR '+FileName, self.BinBuf.Write)
