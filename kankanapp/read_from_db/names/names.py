

from main_file import *
import json
names_db_connection = create_engine('sqlite:///data_bases/names/names.db')

"""
    AGENCY STAFFS
    ============
"""
@app.route('/agency_staff_names',methods=['GET','POST'])
def agency_staffs ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    sql_cmd = session_query.query(Agency_staff).all ()
    key_list = []
    value_list = []
    for names in sql_cmd:
        key_list.insert(0,names.ITEM_NAME)
        value_list.insert(0,names.ITEM_NAME)

    py_dictionry =dict(zip(key_list,value_list))	
    js_dictionary = json.dumps(py_dictionry)
    return allow_cross_origin(js_dictionary)

"""
    MAPEI NAMES
    ===========
"""
@app.route('/keracolor_names',methods=['GET','POST'])
def keracolor_names ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    sql_cmd = session_query.query(Keracolor).all ()

    key_list = []
    value_list = []
    for names in sql_cmd:
        key_list.insert(0,names.ITEM_NAME)
        value_list.insert(0,names.ITEM_NAME)

    py_dictionry =dict(zip(key_list,value_list))	
    js_dictionary = json.dumps(py_dictionry)
    return allow_cross_origin(js_dictionary)



"""
    SADOLIN STAFFS
    ==============
"""
@app.route('/sadolin_staff_names',methods=['GET','POST'])
def sadolin_staffs ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    sql_cmd = session_query.query(Sadolin_staff).all ()

    key_list = []
    value_list = []
    for names in sql_cmd:
        key_list.insert(0,names.ITEM_NAME)
        value_list.insert(0,names.ITEM_NAME)

    py_dictionry =dict(zip(key_list,value_list))	
    js_dictionary = json.dumps(py_dictionry)
    return allow_cross_origin(js_dictionary)



"""
    EMULSION NAMES
    ==============
"""
@app.route('/emulsion_names',methods=['GET','POST'])
def send_emulsion_names ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    sql_cmd = session_query.query(Budget_emulsion).all ()
    key_list = []
    value_list = []
    for names in sql_cmd:
        key_list.insert(0,names.ITEM_NAME)
        value_list.insert(0,names.ITEM_NAME)

    py_dictionry =dict(zip(key_list,value_list))	
    js_dictionary = json.dumps(py_dictionry)
    return allow_cross_origin(js_dictionary)

"""
    THENNER GUARD NAMES
    ==================
"""
@app.route('/thinner_names',methods=['GET','POST'])
def send_thinner_names ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    sql_cmd = session_query.query(Thinner).all ()
    key_list = []
    value_list = []
    for names in sql_cmd:
        key_list.insert(0,names.ITEM_NAME)
        value_list.insert(0,names.ITEM_NAME)

    py_dictionry =dict(zip(key_list,value_list))	
    js_dictionary = json.dumps(py_dictionry)
    return allow_cross_origin(js_dictionary)

"""
    ROOF GUARD NAMES
    ===============
"""
@app.route('/roofguard_names',methods=['GET','POST'])
def send_roofguard_names ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    sql_cmd = session_query.query(Roofguard).all ()
    key_list = []
    value_list = []
    for names in sql_cmd:
        key_list.insert(0,names.ITEM_NAME)
        value_list.insert(0,names.ITEM_NAME)

    py_dictionry =dict(zip(key_list,value_list))	
    js_dictionary = json.dumps(py_dictionry)
    return allow_cross_origin(js_dictionary)

"""
    ROOD MARKING NAMES
    ==================
"""
@app.route('/roodmarking_names',methods=['GET','POST'])
def send_roodmarking_names ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    sql_cmd = session_query.query(Roodmarking).all ()
    key_list = []
    value_list = []
    for names in sql_cmd:
        key_list.insert(0,names.ITEM_NAME)
        value_list.insert(0,names.ITEM_NAME)

    py_dictionry =dict(zip(key_list,value_list))	
    js_dictionary = json.dumps(py_dictionry)
    return allow_cross_origin(js_dictionary)

"""
    BASES NAMES
    ===============
"""
@app.route('/bases_names',methods=['GET','POST'])
def send_bases_names ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    sql_cmd = session_query.query(Sadolin_bases).all ()
    key_list = []
    value_list = []
    for names in sql_cmd:
        key_list.insert(0,names.ITEM_NAME)
        value_list.insert(0,names.ITEM_NAME)

    py_dictionry =dict(zip(key_list,value_list))	
    js_dictionary = json.dumps(py_dictionry)
    return allow_cross_origin(js_dictionary)


"""
    GLOSE NAMES
    ===========
"""
@app.route('/glose_names',methods=['GET','POST'])
def send_glose_names ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    sql_cmd = session_query.query(Budget_glose).all ()
    key_list = []
    value_list = []
    for names in sql_cmd:
        key_list.insert(0,names.ITEM_NAME)
        value_list.insert(0,names.ITEM_NAME)

    py_dictionry =dict(zip(key_list,value_list))	
    js_dictionary = json.dumps(py_dictionry)
    return allow_cross_origin(js_dictionary)
"""
    SILK NAMES
    ==========
"""
@app.route('/silk_names',methods=['GET','POST'])
def send_silk_names ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    sql_cmd = session_query.query(Silk_vinyl).all ()
    key_list = []
    value_list = []
    for names in sql_cmd:
        key_list.insert(0,names.ITEM_NAME)
        value_list.insert(0,names.ITEM_NAME)

    py_dictionry =dict(zip(key_list,value_list))	
    js_dictionary = json.dumps(py_dictionry)
    return allow_cross_origin(js_dictionary)
"""
    SUPER NAMES
    ===========
"""
@app.route('/super_names',methods=['GET','POST'])
def send_super_names ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    sql_cmd = session_query.query(Super_Glose).all ()
    key_list = []
    value_list = []
    for names in sql_cmd:
        key_list.insert(0,names.ITEM_NAME)
        value_list.insert(0,names.ITEM_NAME)

    py_dictionry =dict(zip(key_list,value_list))	
    js_dictionary = json.dumps(py_dictionry)
    return allow_cross_origin(js_dictionary)
"""
    WEATHER NAMES
    ===========
"""
@app.route('/weather_names',methods=['GET','POST'])
def send_weather_names ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    sql_cmd = session_query.query(Weather_guard).all ()
    key_list = []
    value_list = []
    for names in sql_cmd:
        key_list.insert(0,names.ITEM_NAME)
        value_list.insert(0,names.ITEM_NAME)

    py_dictionry =dict(zip(key_list,value_list))	
    js_dictionary = json.dumps(py_dictionry)
    return allow_cross_origin(js_dictionary)

@app.route('/all_bases',methods=['GET','POST'])
def send_all_bases ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    sql_cmd = session_query.query(Sadolin_bases).all ()
    key_list = []
    value_list = []
    for bases in sql_cmd:
        key_list.insert(0,bases.ITEM_NAME)
        value_list.insert(0,bases.ITEM_NAME)

    py_dictionry =dict(zip(key_list,value_list))	
    js_dictionary = json.dumps(py_dictionry)
    return allow_cross_origin(js_dictionary)