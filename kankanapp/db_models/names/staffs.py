
from db_headers import *

# declaring a Mapper 
Base = declarative_base()

"""
			AGENCY NAMES
			============
"""


class Agency_staff (Base):
	__tablename__ = 'agency_table'
	key = Column ('key', Integer, primary_key = True, autoincrement = True)
	ITEM_NAME = Column('ITEM_NAME',String(120))
	def __init__(self,ITEM_NAME):
		self.ITEM_NAME = ITEM_NAME
	def __str__():
		return "<Agency_staff(ITEM_NAME= '%s')>"%(self.ITEM_NAME)

"""
			SADOLIN NAMES
			=============
"""

class Sadolin_staff (Base):
	__tablename__ = 'sadolin_staff'
	key = Column ('key', Integer, primary_key = True, autoincrement = True)
	ITEM_NAME = Column('ITEM_NAME',String(120))
	def __init__(self,ITEM_NAME):
		self.ITEM_NAME = ITEM_NAME
	def __str__():
		return "<Sadolin_staff(ITEM_NAME= '%s')>"%(self.ITEM_NAME)


#  connect dispesary.db
db_connection = create_engine('sqlite:///data_bases/names/staffs.db')
if not db_connection:
	print("\t \t ERROR :: No Connection To Staff Names Database")
else:
	print("\t \t SUCCESS :: Staff Names Database Connected Well ")

# save tables
Base.metadata.create_all(db_connection)
