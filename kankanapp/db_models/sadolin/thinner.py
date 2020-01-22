
# from db_includes import *
from db_headers import *

# declaring a Mapper 
Base = declarative_base() 

class Thinner_new_stock (Base):
	__tablename__ = 'stock_new'
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
		return "<Thinner_new_stock(UNAME= '%s', ITEM_NAME= '%s', SIZE= '%s', INVOICE= '%s', QUANTITY = '%s',DATE='%s',MONTH='%s')>"%(self.UNAME, self.ITEM_NAME, self.SIZE, self.INVOICE, self.QUANTITY, self.DATE,self.MONTH)

class Thinner_stock_flow (Base):
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
		return "<Thinner_stock_flow(UNAME= '%s', ITEM_NAME= '%s', SIZE= '%s', QUANTITY = '%s',DATE='%s',MONTH='%s')>"%(self.UNAME, self.ITEM_NAME, self.SIZE, self.INVOICE, self.QUANTITY, self.DATE,self.MONTH)

class Thinner_stock_status (Base):
	__tablename__ = 'stock_status'
	key = Column ('key', Integer, primary_key = True, autoincrement = True)
	ITEM_NAME = Column('ITEM_NAME',String(120))
	FIVE_LTR = Column('FIVE_LTR',Integer)
	ONE_LTR = Column('ONE_LTR',Integer)	
	
	def __init__(self, ITEM_NAME, FIVE_LTR, ONE_LTR):
		self.ITEM_NAME = ITEM_NAME
		self.FIVE_LTR = FIVE_LTR 
		self.ONE_LTR = ONE_LTR
		
	def __str__():
		return "<Thinner_stock_status(ITEM_NAME= '%s', FIVE_LTR= '%s', ONE_LTR = '%s')>"%(self.ITEM_NAME,self.FIVE_LTR, self.ONE_LTR)


#  connect dispesary.db
db_connection = create_engine('sqlite:///data_bases/sadolin/thinner.db')
if not db_connection:
	print("\t \t ERROR :: No connection to Thinner database")
else:
	# db_connection.echo = True
	print("\t \t SUCCESS :: Thinner database connected well ")

# save tables
Base.metadata.create_all(db_connection)
