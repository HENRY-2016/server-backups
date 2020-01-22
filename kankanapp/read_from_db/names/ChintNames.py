
from main_file import *
import json
names_db_connection = create_engine('sqlite:///data_bases/names/chint_names.db')


@app.route('/read_mcb1p_names',methods=['GET','POST'])
def read_mcb1p_names ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    sql_cmd = session_query.query(MCB1P).all ()

    key_list = []
    value_list = []
    for names in sql_cmd:
        key_list.insert(0,names.ITEM_NAME)
        value_list.insert(0,names.ITEM_NAME)

    py_dictionry =dict(zip(key_list,value_list))	
    js_dictionary = json.dumps(py_dictionry)
    return allow_cross_origin(js_dictionary)

@app.route('/read_mcb2p_names',methods=['GET','POST'])
def read_mcb2p_names ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    sql_cmd = session_query.query(MCB2P).all ()

    key_list = []
    value_list = []
    for names in sql_cmd:
        key_list.insert(0,names.ITEM_NAME)
        value_list.insert(0,names.ITEM_NAME)

    py_dictionry =dict(zip(key_list,value_list))	
    js_dictionary = json.dumps(py_dictionry)
    return allow_cross_origin(js_dictionary)

@app.route('/read_mcb3p_names',methods=['GET','POST'])
def read_mcb3p_names ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    sql_cmd = session_query.query(MCB3P).all ()

    key_list = []
    value_list = []
    for names in sql_cmd:
        key_list.insert(0,names.ITEM_NAME)
        value_list.insert(0,names.ITEM_NAME)

    py_dictionry =dict(zip(key_list,value_list))	
    js_dictionary = json.dumps(py_dictionry)
    return allow_cross_origin(js_dictionary)


@app.route('/read_mcb4p_names',methods=['GET','POST'])
def read_mcb4p_names ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    sql_cmd = session_query.query(MCB4P).all ()

    key_list = []
    value_list = []
    for names in sql_cmd:
        key_list.insert(0,names.ITEM_NAME)
        value_list.insert(0,names.ITEM_NAME)

    py_dictionry =dict(zip(key_list,value_list))	
    js_dictionary = json.dumps(py_dictionry)
    return allow_cross_origin(js_dictionary)

@app.route('/read_led_bulbs_names',methods=['GET','POST'])
def read_led_bulbs_names ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    sql_cmd = session_query.query(LED_BULBS).all ()

    key_list = []
    value_list = []
    for names in sql_cmd:
        key_list.insert(0,names.ITEM_NAME)
        value_list.insert(0,names.ITEM_NAME)

    py_dictionry =dict(zip(key_list,value_list))	
    js_dictionary = json.dumps(py_dictionry)
    return allow_cross_origin(js_dictionary)



@app.route('/read_led_flood_names',methods=['GET','POST'])
def read_led_flood_names ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    sql_cmd = session_query.query(LED_FLOOD).all ()

    key_list = []
    value_list = []
    for names in sql_cmd:
        key_list.insert(0,names.ITEM_NAME)
        value_list.insert(0,names.ITEM_NAME)

    py_dictionry =dict(zip(key_list,value_list))	
    js_dictionary = json.dumps(py_dictionry)
    return allow_cross_origin(js_dictionary)



@app.route('/read_led_ceiling_names',methods=['GET','POST'])
def read_led_ceiling_names ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    sql_cmd = session_query.query(LED_CEILING).all ()

    key_list = []
    value_list = []
    for names in sql_cmd:
        key_list.insert(0,names.ITEM_NAME)
        value_list.insert(0,names.ITEM_NAME)

    py_dictionry =dict(zip(key_list,value_list))	
    js_dictionary = json.dumps(py_dictionry)
    return allow_cross_origin(js_dictionary)


@app.route('/read_led_panel_names',methods=['GET','POST'])
def read_led_panel_names ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    sql_cmd = session_query.query(LED_PANEL).all ()

    key_list = []
    value_list = []
    for names in sql_cmd:
        key_list.insert(0,names.ITEM_NAME)
        value_list.insert(0,names.ITEM_NAME)

    py_dictionry =dict(zip(key_list,value_list))	
    js_dictionary = json.dumps(py_dictionry)
    return allow_cross_origin(js_dictionary)


@app.route('/read_mccb_names',methods=['GET','POST'])
def read_mccb_names ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    sql_cmd = session_query.query(MCCB).all ()

    key_list = []
    value_list = []
    for names in sql_cmd:
        key_list.insert(0,names.ITEM_NAME)
        value_list.insert(0,names.ITEM_NAME)

    py_dictionry =dict(zip(key_list,value_list))	
    js_dictionary = json.dumps(py_dictionry)
    return allow_cross_origin(js_dictionary)

@app.route('/read_main_switch_names',methods=['GET','POST'])
def read_main_switch_names ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    sql_cmd = session_query.query(MAIN_SWITCH).all ()

    key_list = []
    value_list = []
    for names in sql_cmd:
        key_list.insert(0,names.ITEM_NAME)
        value_list.insert(0,names.ITEM_NAME)

    py_dictionry =dict(zip(key_list,value_list))	
    js_dictionary = json.dumps(py_dictionry)
    return allow_cross_origin(js_dictionary)



@app.route('/read_cables_names',methods=['GET','POST'])
def read_cables_names ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    sql_cmd = session_query.query(CABLES).all ()

    key_list = []
    value_list = []
    for names in sql_cmd:
        key_list.insert(0,names.ITEM_NAME)
        value_list.insert(0,names.ITEM_NAME)

    py_dictionry =dict(zip(key_list,value_list))	
    js_dictionary = json.dumps(py_dictionry)
    return allow_cross_origin(js_dictionary)


@app.route('/read_contactor_names',methods=['GET','POST'])
def read_contactor_names ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    sql_cmd = session_query.query(CONTACTOR).all ()

    key_list = []
    value_list = []
    for names in sql_cmd:
        key_list.insert(0,names.ITEM_NAME)
        value_list.insert(0,names.ITEM_NAME)

    py_dictionry =dict(zip(key_list,value_list))	
    js_dictionary = json.dumps(py_dictionry)
    return allow_cross_origin(js_dictionary)


@app.route('/read_industrial_switch_names',methods=['GET','POST'])
def read_industrial_switch_names ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    sql_cmd = session_query.query(INDUSTRIAL_SWITCH).all ()

    key_list = []
    value_list = []
    for names in sql_cmd:
        key_list.insert(0,names.ITEM_NAME)
        value_list.insert(0,names.ITEM_NAME)

    py_dictionry =dict(zip(key_list,value_list))	
    js_dictionary = json.dumps(py_dictionry)
    return allow_cross_origin(js_dictionary)


@app.route('/read_industrial_socket_names',methods=['GET','POST'])
def read_industrial_socket_names ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    sql_cmd = session_query.query(INDUSTRIAL_SOCKET).all ()

    key_list = []
    value_list = []
    for names in sql_cmd:
        key_list.insert(0,names.ITEM_NAME)
        value_list.insert(0,names.ITEM_NAME)

    py_dictionry =dict(zip(key_list,value_list))	
    js_dictionary = json.dumps(py_dictionry)
    return allow_cross_origin(js_dictionary)



@app.route('/read_gold_switch_names',methods=['GET','POST'])
def read_gold_switch_names ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    sql_cmd = session_query.query(GOLD_SWITCH).all ()

    key_list = []
    value_list = []
    for names in sql_cmd:
        key_list.insert(0,names.ITEM_NAME)
        value_list.insert(0,names.ITEM_NAME)

    py_dictionry =dict(zip(key_list,value_list))	
    js_dictionary = json.dumps(py_dictionry)
    return allow_cross_origin(js_dictionary)


@app.route('/read_gold_socket_names',methods=['GET','POST'])
def read_gold_socket_names ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    sql_cmd = session_query.query(GOLD_SOCKET).all ()

    key_list = []
    value_list = []
    for names in sql_cmd:
        key_list.insert(0,names.ITEM_NAME)
        value_list.insert(0,names.ITEM_NAME)

    py_dictionry =dict(zip(key_list,value_list))	
    js_dictionary = json.dumps(py_dictionry)
    return allow_cross_origin(js_dictionary)


@app.route('/read_white_switch_names',methods=['GET','POST'])
def read_white_switch_names ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    sql_cmd = session_query.query(WHITE_SWITCH).all ()

    key_list = []
    value_list = []
    for names in sql_cmd:
        key_list.insert(0,names.ITEM_NAME)
        value_list.insert(0,names.ITEM_NAME)

    py_dictionry =dict(zip(key_list,value_list))	
    js_dictionary = json.dumps(py_dictionry)
    return allow_cross_origin(js_dictionary)

@app.route('/read_white_socket_names',methods=['GET','POST'])
def read_white_socket_names ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    sql_cmd = session_query.query(WHITE_SOCKET).all ()

    key_list = []
    value_list = []
    for names in sql_cmd:
        key_list.insert(0,names.ITEM_NAME)
        value_list.insert(0,names.ITEM_NAME)

    py_dictionry =dict(zip(key_list,value_list))	
    js_dictionary = json.dumps(py_dictionry)
    return allow_cross_origin(js_dictionary)


@app.route('/read_silver_switch_names',methods=['GET','POST'])
def read_silver_switch_names ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    sql_cmd = session_query.query(SILVER_SWITCH).all ()

    key_list = []
    value_list = []
    for names in sql_cmd:
        key_list.insert(0,names.ITEM_NAME)
        value_list.insert(0,names.ITEM_NAME)

    py_dictionry =dict(zip(key_list,value_list))	
    js_dictionary = json.dumps(py_dictionry)
    return allow_cross_origin(js_dictionary)

@app.route('/read_silver_socket_names',methods=['GET','POST'])
def read_silver_socket_names ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    sql_cmd = session_query.query(SILVER_SOCKET).all ()

    key_list = []
    value_list = []
    for names in sql_cmd:
        key_list.insert(0,names.ITEM_NAME)
        value_list.insert(0,names.ITEM_NAME)

    py_dictionry =dict(zip(key_list,value_list))	
    js_dictionary = json.dumps(py_dictionry)
    return allow_cross_origin(js_dictionary)
