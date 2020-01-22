"""
Tables
		++++++
			|---> Agency_New_day
			|	  	 Records balancing of the day
			|			||--->  UNAME | DATE | AIRTEL | MTN | CENTENARY | DFCU | DTB | EQUITY | STANBIC | BARCLAYS | CASH | DRAWINGS | BANKS
			|																			

"""

# from db_includes import *
from db_headers import *

# declaring a Mapper 
Base = declarative_base() 

class Agency_New_day (Base):
	__tablename__ = 'new_day'
	key = Column ('key', Integer, primary_key = True, autoincrement = True)
	MONTH = Column('MONTH', Integer)
	UNAME = Column('UNAME',String(120))
	DATE = Column ('DATE',String(100))
	AIRTEL = Column ('AIRTEL',Integer)
	MTN = Column ('MTN',Integer)
	CENTENARY = Column('CENTENARY', Integer)
	DFCU = Column ('DFCU',Integer)
	DTB = Column ('DTB',Integer)
	EQUITY = Column('EQUITY',Integer)
	STANBIC = Column('STANBIC',Integer)
	BARCLAYS = Column('BARCLAYS',Integer)
	CASH = Column('CASH',Integer)
	DRAWINGS = Column('DRAWINGS',Integer)
	BANKS = Column ('BANKS',Integer)
	FLOAT = Column('FLOAT', Integer)


	def __init__(self,MONTH,UNAME,DATE,AIRTEL,MTN,CENTENARY,DFCU,DTB,EQUITY,STANBIC,BARCLAYS,CASH,DRAWINGS,BANKS,FLOAT):
		self.MONTH = MONTH
		self.UNAME = UNAME 
		self.DATE = DATE 
		self.AIRTEL = AIRTEL 
		self.MTN = MTN 
		self.CENTENARY = CENTENARY 
		self.DFCU = DFCU 
		self.DTB = DTB 
		self.EQUITY = EQUITY 
		self.STANBIC = STANBIC 
		self.BARCLAYS =  BARCLAYS 
		self.CASH = CASH 
		self.DRAWINGS = DRAWINGS
		self.BANKS = BANKS
		self.FLOAT = FLOAT
		
	def __str__():
		return "<Agency_New_day(MONTH='%s',UNAME='%s',DATE='%s',AIRTEL='%s',MTN='%s',CENTENARY='%s',DFCU='%s',DTB='%s',EQUITY='%s',STANBIC='%s',BARCLAYS='%s',CASH='%s',DRAWINGS='%s',BANKS='%s',FLOAT='%s')>"%(self.MONTH, self.UNAME,self.DATE,self.AIRTEL,self.MTN,self.CENTENARY,self.DFCU,self.DTB,self.EQUITY,self.STANBIC,self.BARCLAYS,self.CASH,self.DRAWINGS,self.BANKS,self.FLOAT)
	

#  connect dispesary.db
db_connection = create_engine('sqlite:///data_bases/agency/agency.db')
if not db_connection:
	print("\t \t ERROR :: No connection to Agnecy database")
else:
	# db_connection.echo = True
	print("\t \t SUCCESS :: Agency database connected well ")

# save tables
Base.metadata.create_all(db_connection)
