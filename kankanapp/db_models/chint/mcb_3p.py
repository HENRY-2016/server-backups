
"""
Tables
		++++++
			|---> MCB3P_NEW_STOCK_TABLE
			|	  	 Records New items brought to the store
			|			||--->  UNAME | ITEM_NAME | QUANTITY | DATE 
			|																			
			|---> MCB3P_STOCK_FLOW_TABLE
			|		 Records stock being taken from the store and the remaining
			|				||---> NAME | | USED 
		|								    |
		|									|---> UPDATED when item is being taken out (new + old)
		|                                  
			|									
			|
			|---> MCB3P_STATUS_TABLE
			|		 Records stock being taken out 
			|				
			|               ||--->  UNAME | ITEM_NAME | QUANTITY | DATE
"""

# from db_includes import *
from db_headers import *




# declaring a Mapper 
Base = declarative_base()

class MCB3P_NEW_STOCK_TABLE (Base):
	__tablename__ = 'New_items'
	key = Column ('key', Integer, primary_key = True, autoincrement = True)
	UNAME = Column('UNAME',String(120))
	ITEM_NAME = Column('ITEM_NAME',String(120))
	QUANTITY = Column('QUANTITY',String(120))
	DATE = Column('DATE',String(120))
	MONTH = Column('MONTH',String(50))
	

	def __init__(self, UNAME, ITEM_NAME, QUANTITY , DATE,MONTH):
		self.UNAME = UNAME 
		self.ITEM_NAME = ITEM_NAME
		self.QUANTITY = QUANTITY
		self.DATE = DATE
		self.MONTH = MONTH
		
	def __str__():
		return "<MCB3P_NEW_STOCK_TABLE(UNAME= '%s', ITEM_NAME= '%s',QUANTITY = '%s',DATE='%s',MONTH='%s')>"%(self.UNAME, self.ITEM_NAME, self.SIZE,self.QUANTITY, self.DATE,self.MONTH)

class MCB3P_STOCK_FLOW_TABLE (Base):
	__tablename__ = 'stock_flow'
	key = Column ('key', Integer, primary_key = True, autoincrement = True)
	UNAME = Column('UNAME',String(120))
	ITEM_NAME = Column('ITEM_NAME',String(120))
	QUANTITY = Column('QUANTITY',String(120))
	DATE = Column('DATE',String(120))
	MONTH = Column('MONTH',String(50))

	

	def __init__(self, UNAME, ITEM_NAME, QUANTITY , DATE,MONTH):
		self.UNAME = UNAME 
		self.ITEM_NAME = ITEM_NAME
		self.QUANTITY = QUANTITY
		self.DATE = DATE
		self.MONTH = MONTH
		
	def __str__():
		return "<MCB3P_STOCK_FLOW_TABLE(UNAME= '%s', ITEM_NAME= '%s', SIZE= '%s', QUANTITY = '%s',DATE='%s',MONTH='%s')>"%(self.UNAME, self.ITEM_NAME, self.SIZE,self.QUANTITY, self.DATE,self.MONTH)

class MCB3P_STATUS_TABLE (Base):
	__tablename__ = 'status_table'
	key = Column ('key', Integer, primary_key = True, autoincrement = True)
	ITEM_NAME = Column('ITEM_NAME',String(120))
	QUANTITY = Column('QUANTITY',Integer)
	
	def __init__(self, ITEM_NAME,QUANTITY):
		self.ITEM_NAME = ITEM_NAME
		self.QUANTITY = QUANTITY
		
	def __str__():
		return "<MCB3P_STOCK_FLOW_TABLE(ITEM_NAME= '%s',QUANTITY='%s')>"%(self.ITEM_NAME, self.QUANTITY)


#  connect dispesary.db
db_connection = create_engine('sqlite:///data_bases/chint/mcb_3p.db')
if not db_connection:
	print("\t \t ERROR :: No connection to MCB3P database")
else:
	print("\t \t SUCCESS :: MCB3P database connected well ")

# save tables
Base.metadata.create_all(db_connection)

