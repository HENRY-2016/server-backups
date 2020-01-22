from main_file import *

names_db_connection = create_engine('sqlite:///data_bases/names/chint_names.db')

"""

    CHINT :::::: WRITTE NAMES
    =========================
    
"""

@app.route('/record_mcb1p_name',methods=['POST','GET'])
def mcb1p ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    if request.method == 'POST':
        input_name = request.form['mcb1p']
        name = MCB1P(input_name)
        session_query.add(name)
        session_query.commit() 
    return "<center> MCB 1P <br>Added Well ...."


@app.route('/record_mcb2p_name',methods=['POST','GET'])
def mcb2p ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    if request.method == 'POST':
        input_name = request.form['mcb2p']
        name = MCB2P(input_name)
        session_query.add(name)
        session_query.commit() 
    return "<center> MCB 2P <br>Added Well ...."

@app.route('/record_mcb3p_name',methods=['POST','GET'])
def mcb3p ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    if request.method == 'POST':
        input_name = request.form['mcb3p']
        name = MCB3P(input_name)
        session_query.add(name)
        session_query.commit() 
    return "<center> MCB 3P <br>Added Well ...."

@app.route('/record_mcb4p_name',methods=['POST','GET'])
def mcb4p ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    if request.method == 'POST':
        input_name = request.form['mcb4p']
        name = MCB4P(input_name)
        session_query.add(name)
        session_query.commit() 
    return "<center> MCB 4P <br>Added Well ...."

@app.route('/record_mccb_name',methods=['POST','GET'])
def mccb ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    if request.method == 'POST':
        input_name = request.form['mccb']
        name = MCCB(input_name)
        session_query.add(name)
        session_query.commit() 
    return "<center> MCCB  <br>Added Well ...."

@app.route('/record_led_bulbs_name',methods=['POST','GET'])
def led_bulbs ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    if request.method == 'POST':
        input_name = request.form['led_bulbs']
        name = LED_BULBS(input_name)
        session_query.add(name)
        session_query.commit() 
    return "<center> led_bulbs  <br>Added Well ...."

@app.route('/record_led_flood_name',methods=['POST','GET'])
def led_flood ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    if request.method == 'POST':
        input_name = request.form['led_flood']
        name = LED_FLOOD(input_name)
        session_query.add(name)
        session_query.commit() 
    return "<center> led_flood  <br>Added Well ...."


@app.route('/record_led_ceiling_name',methods=['POST','GET'])
def led_ceiling ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    if request.method == 'POST':
        input_name = request.form['led_ceiling']
        name = LED_CEILING(input_name)
        session_query.add(name)
        session_query.commit() 
    return "<center> led_ceiling  <br>Added Well ...."


@app.route('/record_led_panel_name',methods=['POST','GET'])
def led_panel ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    if request.method == 'POST':
        input_name = request.form['led_panel']
        name = LED_PANEL(input_name)
        session_query.add(name)
        session_query.commit() 
    return "<center> led_panel  <br>Added Well ...."

@app.route('/record_main_switch_name',methods=['POST','GET'])
def main_switch ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    if request.method == 'POST':
        input_name = request.form['main_switch']
        name = MAIN_SWITCH(input_name)
        session_query.add(name)
        session_query.commit() 
    return "<center> main_switch  <br>Added Well ...."


@app.route('/record_cables_name',methods=['POST','GET'])
def cables ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    if request.method == 'POST':
        input_name = request.form['cables']
        name = CABLES(input_name)
        session_query.add(name)
        session_query.commit() 
    return "<center> cables  <br>Added Well ...."


@app.route('/record_contactor_name',methods=['POST','GET'])
def contactor ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    if request.method == 'POST':
        input_name = request.form['contactor']
        name = CONTACTOR(input_name)
        session_query.add(name)
        session_query.commit() 
    return "<center> contactor  <br>Added Well ...."


@app.route('/record_gold_switch_name',methods=['POST','GET'])
def gold_switch ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    if request.method == 'POST':
        input_name = request.form['gold_switch']
        name = GOLD_SWITCH(input_name)
        session_query.add(name)
        session_query.commit() 
    return "<center> gold switch   <br>Added Well ...."


@app.route('/record_gold_socket_name',methods=['POST','GET'])
def gold_socket ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    if request.method == 'POST':
        input_name = request.form['gold_socket']
        name = GOLD_SOCKET(input_name)
        session_query.add(name)
        session_query.commit() 
    return "<center> gold socket   <br>Added Well ...."

@app.route('/record_industrial_switch_name',methods=['POST','GET'])
def industrial_switch ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    if request.method == 'POST':
        input_name = request.form['industrial_switch']
        name = INDUSTRIAL_SWITCH(input_name)
        session_query.add(name)
        session_query.commit() 
    return "<center> industrial switch   <br>Added Well ...."


@app.route('/record_industrial_socket_name',methods=['POST','GET'])
def industrial_socket ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    if request.method == 'POST':
        input_name = request.form['industrial_socket']
        name = INDUSTRIAL_SOCKET(input_name)
        session_query.add(name)
        session_query.commit() 
    return "<center> industrial socket   <br>Added Well ...."


@app.route('/record_white_switch_name',methods=['POST','GET'])
def white_switch ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    if request.method == 'POST':
        input_name = request.form['white_switch']
        name = WHITE_SWITCH(input_name)
        session_query.add(name)
        session_query.commit() 
    return "<center> white switch   <br>Added Well ...."


@app.route('/record_white_socket_name',methods=['POST','GET'])
def white_socket ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    if request.method == 'POST':
        input_name = request.form['white_socket']
        name = WHITE_SOCKET(input_name)
        session_query.add(name)
        session_query.commit() 
    return "<center> white socket   <br>Added Well ...."





@app.route('/record_silver_switch_name',methods=['POST','GET'])
def silver_switch ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    if request.method == 'POST':
        input_name = request.form['silver_switch']
        name = SILVER_SWITCH(input_name)
        session_query.add(name)
        session_query.commit() 
    return "<center> silver switch   <br>Added Well ...."


@app.route('/record_silver_socket_name',methods=['POST','GET'])
def silver_socket ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    if request.method == 'POST':
        input_name = request.form['silver_socket']
        name = SILVER_SOCKET(input_name)
        session_query.add(name)
        session_query.commit() 
    return "<center> silver socket   <br>Added Well ...."



"""

    CHINT :::::: READ NAMES
    ========================
    
"""










