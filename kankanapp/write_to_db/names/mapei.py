


from main_file import *

names_db_connection = create_engine('sqlite:///data_bases/names/mapei.db')

"""
    MAPEI NAMES
    ============
"""
@app.route('/keracolor_record_new_name',methods=['POST','GET'])
def keracolor_name ():
    DBsession = sessionmaker(bind=names_db_connection)
    session_query = DBsession()
    if request.method == 'POST':
        new_name = request.form['keracolor_name']
        name = Keracolor (new_name)
        session_query.add(name)
        session_query.commit() 
    return "<center> Mapei keracolor name <br>Added Well ...."
