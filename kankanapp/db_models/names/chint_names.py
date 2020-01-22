



from db_headers import *

# declaring a Mapper 
Base = declarative_base()


"""
			CHINT NAMES
			============
"""

class MCB1P (Base):
	__tablename__ = 'mcb1p'
	key = Column ('key', Integer, primary_key = True, autoincrement = True)
	ITEM_NAME = Column('ITEM_NAME',String(120))
	def __init__(self,ITEM_NAME):
		self.ITEM_NAME = ITEM_NAME
	def __str__():
		return "<MCB1P(ITEM_NAME= '%s')>"%(self.ITEM_NAME)

class MCB2P (Base):
	__tablename__ = 'mcb2p'
	key = Column ('key', Integer, primary_key = True, autoincrement = True)
	ITEM_NAME = Column('ITEM_NAME',String(120))
	def __init__(self,ITEM_NAME):
		self.ITEM_NAME = ITEM_NAME
	def __str__():
		return "<MCB2P(ITEM_NAME= '%s')>"%(self.ITEM_NAME)

class MCB3P (Base):
	__tablename__ = 'mcb3p'
	key = Column ('key', Integer, primary_key = True, autoincrement = True)
	ITEM_NAME = Column('ITEM_NAME',String(120))
	def __init__(self,ITEM_NAME):
		self.ITEM_NAME = ITEM_NAME
	def __str__():
		return "<MCB3P(ITEM_NAME= '%s')>"%(self.ITEM_NAME)


class MCB4P (Base):
	__tablename__ = 'mcb4p'
	key = Column ('key', Integer, primary_key = True, autoincrement = True)
	ITEM_NAME = Column('ITEM_NAME',String(120))
	def __init__(self,ITEM_NAME):
		self.ITEM_NAME = ITEM_NAME
	def __str__():
		return "<MCB4P(ITEM_NAME= '%s')>"%(self.ITEM_NAME)

class LED_BULBS (Base):
	__tablename__ = 'led_bulbs'
	key = Column ('key', Integer, primary_key = True, autoincrement = True)
	ITEM_NAME = Column('ITEM_NAME',String(120))
	def __init__(self,ITEM_NAME):
		self.ITEM_NAME = ITEM_NAME
	def __str__():
		return "<LED_BULBS(ITEM_NAME= '%s')>"%(self.ITEM_NAME)

class LED_CEILING (Base):
	__tablename__ = 'led_ceiling'
	key = Column ('key', Integer, primary_key = True, autoincrement = True)
	ITEM_NAME = Column('ITEM_NAME',String(120))
	def __init__(self,ITEM_NAME):
		self.ITEM_NAME = ITEM_NAME
	def __str__():
		return "<LED_CEILING(ITEM_NAME= '%s')>"%(self.ITEM_NAME)

class LED_FLOOD (Base):
	__tablename__ = 'led_flood'
	key = Column ('key', Integer, primary_key = True, autoincrement = True)
	ITEM_NAME = Column('ITEM_NAME',String(120))
	def __init__(self,ITEM_NAME):
		self.ITEM_NAME = ITEM_NAME
	def __str__():
		return "<LED_FLOOD(ITEM_NAME= '%s')>"%(self.ITEM_NAME)

class LED_PANEL (Base):
	__tablename__ = 'led_panel'
	key = Column ('key', Integer, primary_key = True, autoincrement = True)
	ITEM_NAME = Column('ITEM_NAME',String(120))
	def __init__(self,ITEM_NAME):
		self.ITEM_NAME = ITEM_NAME
	def __str__():
		return "<LED_PANEL(ITEM_NAME= '%s')>"%(self.ITEM_NAME)

class MCCB (Base):
	__tablename__ = 'mccb'
	key = Column ('key', Integer, primary_key = True, autoincrement = True)
	ITEM_NAME = Column('ITEM_NAME',String(120))
	def __init__(self,ITEM_NAME):
		self.ITEM_NAME = ITEM_NAME
	def __str__():
		return "<LED_MCCB(ITEM_NAME= '%s')>"%(self.ITEM_NAME)

class MAIN_SWITCH (Base):
	__tablename__ = 'main_switch'
	key = Column ('key', Integer, primary_key = True, autoincrement = True)
	ITEM_NAME = Column('ITEM_NAME',String(120))
	def __init__(self,ITEM_NAME):
		self.ITEM_NAME = ITEM_NAME
	def __str__():
		return "<MAIN_SWITCH(ITEM_NAME= '%s')>"%(self.ITEM_NAME)

class CABLES (Base):
	__tablename__ = 'cables'
	key = Column ('key', Integer, primary_key = True, autoincrement = True)
	ITEM_NAME = Column('ITEM_NAME',String(120))
	def __init__(self,ITEM_NAME):
		self.ITEM_NAME = ITEM_NAME
	def __str__():
		return "<CABLES(ITEM_NAME= '%s')>"%(self.ITEM_NAME)

class CONTACTOR (Base):
	__tablename__ = 'contactor'
	key = Column ('key', Integer, primary_key = True, autoincrement = True)
	ITEM_NAME = Column('ITEM_NAME',String(120))
	def __init__(self,ITEM_NAME):
		self.ITEM_NAME = ITEM_NAME
	def __str__():
		return "<CONTACTOR(ITEM_NAME= '%s')>"%(self.ITEM_NAME)

class INDUSTRIAL_SWITCH (Base):
	__tablename__ = 'industrial_switch'
	key = Column ('key', Integer, primary_key = True, autoincrement = True)
	ITEM_NAME = Column('ITEM_NAME',String(120))
	def __init__(self,ITEM_NAME):
		self.ITEM_NAME = ITEM_NAME
	def __str__():
		return "<INDUSTRIAL_SWITCH(ITEM_NAME= '%s')>"%(self.ITEM_NAME)

class INDUSTRIAL_SOCKET (Base):
	__tablename__ = 'industrial_socket'
	key = Column ('key', Integer, primary_key = True, autoincrement = True)
	ITEM_NAME = Column('ITEM_NAME',String(120))
	def __init__(self,ITEM_NAME):
		self.ITEM_NAME = ITEM_NAME
	def __str__():
		return "<INDUSTRIAL_SOCKET(ITEM_NAME= '%s')>"%(self.ITEM_NAME)


class GOLD_SWITCH (Base):
	__tablename__ = 'gold_switch'
	key = Column ('key', Integer, primary_key = True, autoincrement = True)
	ITEM_NAME = Column('ITEM_NAME',String(120))
	def __init__(self,ITEM_NAME):
		self.ITEM_NAME = ITEM_NAME
	def __str__():
		return "<GOLD_SWITCH(ITEM_NAME= '%s')>"%(self.ITEM_NAME)

class GOLD_SOCKET (Base):
	__tablename__ = 'gold_socket'
	key = Column ('key', Integer, primary_key = True, autoincrement = True)
	ITEM_NAME = Column('ITEM_NAME',String(120))
	def __init__(self,ITEM_NAME):
		self.ITEM_NAME = ITEM_NAME
	def __str__():
		return "<GOLD_SOCKET(ITEM_NAME= '%s')>"%(self.ITEM_NAME)

class WHITE_SWITCH (Base):
	__tablename__ = 'white_switch'
	key = Column ('key', Integer, primary_key = True, autoincrement = True)
	ITEM_NAME = Column('ITEM_NAME',String(120))
	def __init__(self,ITEM_NAME):
		self.ITEM_NAME = ITEM_NAME
	def __str__():
		return "<WHITE_SWITCH(ITEM_NAME= '%s')>"%(self.ITEM_NAME)

class WHITE_SOCKET (Base):
	__tablename__ = 'white_socket'
	key = Column ('key', Integer, primary_key = True, autoincrement = True)
	ITEM_NAME = Column('ITEM_NAME',String(120))
	def __init__(self,ITEM_NAME):
		self.ITEM_NAME = ITEM_NAME
	def __str__():
		return "<WHITE_SOCKET(ITEM_NAME= '%s')>"%(self.ITEM_NAME)


class SILVER_SWITCH (Base):
	__tablename__ = 'silver_switch'
	key = Column ('key', Integer, primary_key = True, autoincrement = True)
	ITEM_NAME = Column('ITEM_NAME',String(120))
	def __init__(self,ITEM_NAME):
		self.ITEM_NAME = ITEM_NAME
	def __str__():
		return "<SILVER_SWITCH(ITEM_NAME= '%s')>"%(self.ITEM_NAME)

class SILVER_SOCKET (Base):
	__tablename__ = 'silver_socket'
	key = Column ('key', Integer, primary_key = True, autoincrement = True)
	ITEM_NAME = Column('ITEM_NAME',String(120))
	def __init__(self,ITEM_NAME):
		self.ITEM_NAME = ITEM_NAME
	def __str__():
		return "<SILVER_SOCKET(ITEM_NAME= '%s')>"%(self.ITEM_NAME)





#  connect dispesary.db
db_connection = create_engine('sqlite:///data_bases/names/chint_names.db')
if not db_connection:
	print("\t \t ERROR :: No connection to Names database")
else:
	print("\t \t SUCCESS :: Names database connected well ")

# save tables
Base.metadata.create_all(db_connection)
