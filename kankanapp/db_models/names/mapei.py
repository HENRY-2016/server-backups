



from db_headers import *

# declaring a Mapper 
Base = declarative_base()


"""
			MAPEI NAMES
			===========
"""
class Keracolor (Base):
	__tablename__ = 'keracolor'
	key = Column ('key', Integer, primary_key = True, autoincrement = True)
	ITEM_NAME = Column('ITEM_NAME',String(120))
	def __init__(self,ITEM_NAME):
		self.ITEM_NAME = ITEM_NAME
	def __str__():
		return "<Keracolor(ITEM_NAME= '%s')>"%(self.ITEM_NAME)

db_connection = create_engine('sqlite:///data_bases/names/mapei.db')
if not db_connection:
	print("\t \t ERROR :: No Connection To Mapei Names Database")
else:
	print("\t \t SUCCESS :: Mapei Names Database Connected Well ")

# save tables
Base.metadata.create_all(db_connection)
