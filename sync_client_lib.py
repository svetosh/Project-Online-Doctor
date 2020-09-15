import  ftplib

class BinaryBuffer:
	# internal class
	BinaryData=bytes()
	
	def Write(self,BinaryData):
		self.BinaryData=bytes(BinaryData)
		
	def SaveToFile(self,FileName):
		savefile = open(FileName,'wb')
		savefile.write(self.BinaryData)
		savefile.close()

class FTPConnection:
	
	Server=''
	Login=''
	Password=''
	Connection=""
	BinBuf=[] # BinaryBuffer()
	# Функции для:
	def __init__(self,Login='',Password='',Server='localhost'): 
		# Инициализации класса 
		self.Login = Login
		self.Password = Password
		self.Server = Server # сервер по умолчанию - localhost
		
	def Connect(self):
		# Открытия соединения (подключение к серверу)
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
		# Закрытие соединения (отключение от сервера)
		self.Connection.quit() 
		print("Disconnected.")
		
	def ListDir(self):
		# Показать директорию 
		return self.Connection.retrlines('LIST')
		
	def ChangeDir(self,WantedDir):
		# Сменить директорию
		self.Connection.cwd(WantedDir)
		
	def GetFile(self, FileName, SaveToggle=True): 
		# Получение файла
		# если SaveToggle = False, то функция просто возвращает байты
		BinBufObj = BinaryBuffer()
		self.Connection.retrbinary('RETR '+FileName, BinBufObj.Write)
		
		if SaveToggle == True:
			BinBufObj.SaveToFile(FileName)
			return BinBufObj
		else:
			return BinBufObj
	
	def GetMultiple(self, FileNameList, SaveToggle=True):
		# получение нескольких файлов
		for FileName in FileNameList:
			BinBufObj = self.GetFile(FileName,SaveToggle)
			if SaveToggle == False: # Если ложь,
				self.BinBuf.append(BinBufObj) # то кешируем файл в ОЗУ
