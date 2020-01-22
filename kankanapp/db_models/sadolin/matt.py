
"""
Tables
		++++++
			|---> Matt_New_stock_table
			|	  	 Records New items brought to the store
			|			||--->  UNAME | ITEM_NAME | SIZE | INVOICE | QUANTITY | DATE 
			|																			
			|---> Matt_stock_status_table
			|		 Records stock being taken from the store and the remaining
			|				||---> NAME | AT_HAND | USED 
			|									|	    |
			|									|		|---> UPDATED when item is being taken out (new + old)
            |                                   |
			|									|---> UPDATED When new items are being entered (new + old)
			|
			|---> Matt_stock_flow_table
			|		 Records stock being taken out 
			|				
			|               ||--->  UNAME | ITEM_NAME | INVOICE | QUANTITY  | SIZE | DATE
"""

# from db_includes import *
from db_headers import *




# declaring a Mapper 
Base = declarative_base()

class Matt_New_stock_table (Base):
	__tablename__ = 'New_items'
	key = Column ('key', Integer, primary_key = True, autoincrement = True)
	UNAME = Column('UNAME',String(120))
	ITEM_NAME = Column('ITEM_NAME',String(120))
	SIZE = Column('SIZE',String(120))
	INVOICE = Column('INVOICE',Integer)
	QUANTITY = Column('QUANTITY',String(120))
	DATE = Column('DATE',String(120))
	MONTH = Column('MONTH',String(50))
	

	def __init__(self, UNAME, ITEM_NAME, SIZE, INVOICE, QUANTITY , DATE,MONTH):
		self.UNAME = UNAME 
		self.ITEM_NAME = ITEM_NAME
		self.SIZE = SIZE 
		self.INVOICE = INVOICE 
		self.QUANTITY = QUANTITY
		self.DATE = DATE
		self.MONTH = MONTH
		
	def __str__():
		return "<Matt_New_stock_table(UNAME= '%s', ITEM_NAME= '%s', SIZE= '%s', INVOICE= '%s', QUANTITY = '%s',DATE='%s',MONTH='%s')>"%(self.UNAME, self.ITEM_NAME, self.SIZE, self.INVOICE, self.QUANTITY, self.DATE,self.MONTH)

class Matt_stock_flow_table (Base):
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
		return "<Matt_stock_flow_table(UNAME= '%s', ITEM_NAME= '%s', SIZE= '%s', QUANTITY = '%s',DATE='%s',MONTH='%s')>"%(self.UNAME, self.ITEM_NAME, self.SIZE, self.INVOICE, self.QUANTITY, self.DATE,self.MONTH)

class Matt_status_table (Base):
    __tablename__ = 'status_table'
    key = Column ('key', Integer, primary_key = True, autoincrement = True)
    ITEM_NAME = Column('ITEM_NAME',String(120))
    TWENTY_LTR = Column('TWENTY_LTR',Integer)
    FOUR_LTR = Column('FOUR_LTR',Integer)
    ONE_LTR = Column ('ONE_LTR',Integer)


    def __init__(self, ITEM_NAME, TWENTY_LTR, FOUR_LTR,ONE_LTR):
        self.ITEM_NAME = ITEM_NAME
        self.TWENTY_LTR = TWENTY_LTR 
        self.FOUR_LTR = FOUR_LTR
        self.ONE_LTR = ONE_LTR

    def __str__():
        return "<Matt_status_table(ITEM_NAME= '%s', TWENTY_LTR= '%s', FOUR_LTR = '%s',ONE_LTR='%s')>"%(self.ITEM_NAME, self.TWENTY_LTR, self.FOUR_LTR,self.ONE_LTR)


#  connect dispesary.db
db_connection = create_engine('sqlite:///data_bases/sadolin/matt.db')
if not db_connection:
	print("\t \t ERROR :: No connection to Matt database")
else:
	print("\t \t SUCCESS :: Matt database connected well ")

# save tables
Base.metadata.create_all(db_connection)
