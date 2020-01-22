

from main_file import *

names_db_connection = create_engine('sqlite:///data_bases/names/staffs.db')



"""
    AGENCY NAMES
    ============
"""
@app.route('/agency_record_new_staff',methods=['POST','GET'])
def agency_staff ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    if request.method == 'POST':
        new_name = request.form['agency_staff']
        print new_name
        name = Agency_staff (new_name)
        session_query.add(name)
        session_query.commit() 
    return "<center> Agency Staff <br>Added Well ...."

"""
    SADOLIN NAMES
    =============
"""
@app.route('/sadolin_record_new_staff',methods=['POST','GET'])
def sadolin_staff ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    if request.method == 'POST':
        new_name = request.form['sadolin_staff']
        name = Sadolin_staff (new_name)
        session_query.add(name)
        session_query.commit() 
    return "<center>Sadolin Staff <br>Added Well ....</center>"

