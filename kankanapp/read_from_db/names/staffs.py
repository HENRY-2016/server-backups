

from main_file import *
import json
names_db_connection = create_engine('sqlite:///data_bases/names/staffs.db')

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

