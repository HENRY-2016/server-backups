"""
Tables
		++++++
			|---> Planiseal_grey_New_stock_table
			|	  	 Records New items brought to the store
			|			||--->  UNAME | ITEM_NAME | SIZE | INVOICE | QUANTITY | DATE 
			|																			
			|---> Planiseal_grey_stock_status_table
			|		 Records stock being taken from the store and the remaining
			|				||---> NAME | AT_HAND | USED 
			|									|	    |
			|									|		|---> UPDATED when item is being taken out (new + old)
            |                                   |
			|									|---> UPDATED When new items are being entered (new + old)
			|
			|---> Planiseal_grey_stock_flow_table
			|		 Records stock being taken out 
			|				
			|               ||--->  UNAME | ITEM_NAME | INVOICE | QUANTITY  | SIZE | DATE
"""

# from db_includes import *
from db_headers import *




# declaring a Mapper 
Base = declarative_base()

class Planiseal_grey_New_stock_table (Base):
	__tablename__ = 'New_items'
	key = Column ('key', Integer, primary_key = True, autoincrement = True)
	UNAME = Column('UNAME',String(120))
	ITEM_NAME = Column('ITEM_NAME',String(120))
	SIZE = Column('SIZE',String(120))
	QUANTITY = Column('QUANTITY',String(120))
	DATE = Column('DATE',String(120))
	MONTH = Column('MONTH',String(50))
	

	def __init__(self, UNAME, ITEM_NAME, SIZE, QUANTITY , DATE,MONTH):
		self.UNAME = UNAME 
		self.ITEM_NAME = ITEM_NAME
		self.SIZE = SIZE 
		self.QUANTITY = QUANTITY
		self.DATE = DATE
		self.MONTH = MONTH
		
	def __str__():
		return "<Planiseal_grey_New_stock_table(UNAME= '%s', ITEM_NAME= '%s', SIZE= '%s',QUANTITY = '%s',DATE='%s',MONTH='%s')>"%(self.UNAME, self.ITEM_NAME, self.SIZE,self.QUANTITY, self.DATE,self.MONTH)

class Planiseal_grey_stock_flow_table (Base):
	__tablename__ = 'stock_flow'
	key = Column ('key', Integer, primary_key = True, autoincrement = True)
	UNAME = Column('UNAME',String(120))
	ITEM_NAME = Column('ITEM_NAME',String(120))
	SIZE = Column('SIZE',String(120))
	QUANTITY = Column('QUANTITY',String(120))
	DATE = Column('DATE',String(120))
	MONTH = Column('MONTH',String(50))

	

	def __init__(self, UNAME, ITEM_NAME, SIZE, QUANTITY , DATE,MONTH):
		self.UNAME = UNAME 
		self.ITEM_NAME = ITEM_NAME
		self.SIZE = SIZE 
		self.QUANTITY = QUANTITY
		self.DATE = DATE
		self.MONTH = MONTH
		
	def __str__():
		return "<Planiseal_grey_stock_flow_table(UNAME= '%s', ITEM_NAME= '%s', SIZE= '%s', QUANTITY = '%s',DATE='%s',MONTH='%s')>"%(self.UNAME, self.ITEM_NAME, self.SIZE, self.QUANTITY, self.DATE,self.MONTH)

class Planiseal_grey_status_table (Base):
	__tablename__ = 'status_table'
	key = Column ('key', Integer, primary_key = True, autoincrement = True)
	ITEM_NAME = Column('ITEM_NAME',String(120))
	QUANTITY = Column('QUANTITY',Integer)
	
	

	def __init__(self, ITEM_NAME,QUANTITY):
		self.ITEM_NAME = ITEM_NAME
		self.QUANTITY = QUANTITY
		
	def __str__():
		return "<Planiseal_grey_status_table(ITEM_NAME= '%s',QUANTITY='%s')>"%(self.ITEM_NAME, self.QUANTITY)


#  connect dispesary.db
db_connection = create_engine('sqlite:///data_bases/mapei/planiseal_grey.db')
if not db_connection:
	print("\t \t ERROR :: No connection to Planiseal_grey database")
else:
	print("\t \t SUCCESS :: Planiseal_grey database connected well ")

# save tables
Base.metadata.create_all(db_connection)
