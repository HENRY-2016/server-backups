



from db_headers import *

# declaring a Mapper 
Base = declarative_base()

"""
			COLOUR NAMES
			============
"""


class Budget_glose (Base):
	__tablename__ = 'budget_Glose'
	key = Column ('key', Integer, primary_key = True, autoincrement = True)
	ITEM_NAME = Column('ITEM_NAME',String(120))
	def __init__(self,ITEM_NAME):
		self.ITEM_NAME = ITEM_NAME
	def __str__():
		return "<Budget_glose(ITEM_NAME= '%s')>"%(self.ITEM_NAME)

class Budget_emulsion (Base):
    __tablename__ = 'Budget_emulsion'
    key = Column ('key', Integer, primary_key = True, autoincrement = True)
    ITEM_NAME = Column('ITEM_NAME',String(120))
    def __init__(self, ITEM_NAME):
        self.ITEM_NAME = ITEM_NAME
    def __str__():
        return "<Budget_emulsion(ITEM_NAME= '%s')>"%(self.ITEM_NAME)

class Roodmarking (Base):
    __tablename__ = 'rood_marking'
    key = Column ('key', Integer, primary_key = True, autoincrement = True)
    ITEM_NAME = Column('ITEM_NAME',String(120))
    def __init__(self, ITEM_NAME):
        self.ITEM_NAME = ITEM_NAME
    def __str__():
        return "<Roodmarking(ITEM_NAME= '%s')>"%(self.ITEM_NAME)

class Sadolin_bases (Base):
    __tablename__ = 'bases'
    key = Column ('key', Integer, primary_key = True, autoincrement = True)
    ITEM_NAME = Column('ITEM_NAME',String(120))
    def __init__(self, ITEM_NAME):
        self.ITEM_NAME = ITEM_NAME
    def __str__():
        return "<Sadolin_bases(ITEM_NAME= '%s')>"%(self.ITEM_NAME)

class Roofguard (Base):
    __tablename__ = 'roof_guard'
    key = Column ('key', Integer, primary_key = True, autoincrement = True)
    ITEM_NAME = Column('ITEM_NAME',String(120))
    def __init__(self, ITEM_NAME):
        self.ITEM_NAME = ITEM_NAME
    def __str__():
        return "<Roofguard(ITEM_NAME= '%s')>"%(self.ITEM_NAME)

class Silk_vinyl (Base):
    __tablename__ = 'silk_vinyl'
    key = Column ('key', Integer, primary_key = True, autoincrement = True)
    ITEM_NAME = Column('ITEM_NAME',String(120))
    def __init__(self, ITEM_NAME):
        self.ITEM_NAME = ITEM_NAME
    def __str__():
        return "<Silk_vinyl(ITEM_NAME= '%s')>"%(self.ITEM_NAME)



class Super_Glose (Base):
    __tablename__ = 'super_Glose'
    key = Column ('key', Integer, primary_key = True, autoincrement = True)
    ITEM_NAME = Column('ITEM_NAME',String(120))
    def __init__(self, ITEM_NAME):
        self.ITEM_NAME = ITEM_NAME
    def __str__():
        return "<Super_Glose(ITEM_NAME= '%s')>"%(self.ITEM_NAME)



class Thinner (Base):
    __tablename__ = 'thinner'
    key = Column ('key', Integer, primary_key = True, autoincrement = True)
    ITEM_NAME = Column('ITEM_NAME',String(120))
    def __init__(self, ITEM_NAME):
        self.ITEM_NAME = ITEM_NAME
    def __str__():
        return "<Thinner(ITEM_NAME= '%s')>"%(self.ITEM_NAME)

class Weather_guard (Base):
    __tablename__ = 'weather_guard'
    key = Column ('key', Integer, primary_key = True, autoincrement = True)
    ITEM_NAME = Column('ITEM_NAME',String(120))
    def __init__(self, ITEM_NAME):
        self.ITEM_NAME = ITEM_NAME
    def __str__():
        return "<Weather_guard(ITEM_NAME= '%s')>"%(self.ITEM_NAME)


#  connect dispesary.db
db_connection = create_engine('sqlite:///data_bases/names/sadolin.db')
if not db_connection:
	print("\t \t ERROR :: No Connection To Sadoloin Names Database")
else:
	print("\t \t SUCCESS :: Sadolin Names Database Donnected Well ")

# save tables
Base.metadata.create_all(db_connection)
