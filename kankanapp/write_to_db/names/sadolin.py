

from main_file import *

names_db_connection = create_engine('sqlite:///data_bases/names/sadolin.db')

"""
    EMULSIONS NAMES
    ===============
"""
@app.route('/emulsion_record_new_names',methods=['POST','GET'])
def emulsion_names ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    if request.method == 'POST':
        new_name = request.form['emulsion_names']
        name = Budget_emulsion (new_name)
        session_query.add(name)
        session_query.commit() 
    return "<center>Budget emulsion  Name <br> Added Well ....</center>"


"""
    GLOSE NAMES
    ===========
"""
@app.route('/glose_record_new_names',methods=['POST','GET'])
def glose_names ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    if request.method == 'POST':
        new_name = request.form['glose_names']
        name = Budget_glose (new_name)
        session_query.add(name)
        session_query.commit() 
    return "<center>Budget glose  Name <br> Added Well ....</center>"

"""
    ROOD MARKING NAMES
    ==================
"""
@app.route('/roodmarking_record_new_names',methods=['POST','GET'])
def roodmarking_names ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    if request.method == 'POST':
        new_name = request.form['roodmarking_names']
        name = Roodmarking (new_name)
        session_query.add(name)
        session_query.commit() 
    return "<center>Rood marking  Name <br> Added Well ....</center>"

"""
    ROOF GUARD NAMES
    =================
"""
@app.route('/roofguard_record_new_names',methods=['POST','GET'])
def roofguard_names ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    if request.method == 'POST':
        new_name = request.form['roofguard_names']
        name = Roofguard (new_name)
        session_query.add(name)
        session_query.commit() 
    return "<center>Roofguard  Name <br> Added Well ....</center>"

"""
    BASES NAMES
    ===========
"""
@app.route('/base_record_new_names',methods=['POST','GET'])
def base_names ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    if request.method == 'POST':
        new_name = request.form['base_names']
        name = Sadolin_bases (new_name)
        session_query.add(name)
        session_query.commit() 
    return "<center>Base <br> Added Well ....</center>"

"""
    SILK NAMES
    ==========
"""
@app.route('/silk_record_new_names',methods=['POST','GET'])
def silk_names ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    if request.method == 'POST':
        new_name = request.form['silk_names']
        name = Silk_vinyl (new_name)
        session_query.add(name)
        session_query.commit() 
    return "<center>Silk Vinyl Name <br> Added Well ....</center>"


"""
    SUPER GLOSE NAMES
    =================
"""
@app.route('/super_record_new_names',methods=['POST','GET'])
def super_names ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    if request.method == 'POST':
        new_name = request.form['super_names']
        name = Super_Glose (new_name)
        session_query.add(name)
        session_query.commit() 
    return "<center>Super Glose Name <br>Added Well ....</center>"

"""
    THENNER GUARD NAMES
    ==================
"""
@app.route('/thinner_record_new_names',methods=['POST','GET'])
def thinner_names ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    if request.method == 'POST':
        new_name = request.form['thinner_names']
        name = Thinner (new_name)
        session_query.add(name)
        session_query.commit() 
    return "<center>Thinner Name <br>Added Well ....</center>"


"""
    WEATHER GUARD NAMES
    ==================
"""
@app.route('/weather_record_new_names',methods=['POST','GET'])
def weather_names ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    if request.method == 'POST':
        new_name = request.form['weather_names']
        name = Weather_guard (new_name)
        session_query.add(name)
        session_query.commit() 
    return "<center>Weather Guard Name <br> Added Well ....</center>"
