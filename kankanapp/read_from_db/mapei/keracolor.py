







from main_file import *
from datetime import datetime, timedelta
import datetime

keracolor_db_connection = create_engine('sqlite:///data_bases/mapei/keracolor.db')

"""
		@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
		@
		@		NEW STOCK 
		@
		@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

"""

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> ALL
@app.route ('/keracolor_stock_view_all',methods=['POST','GET'])
def keracolor_view_all ():
	DBsession = sessionmaker(bind=keracolor_db_connection)
	session_query = DBsession()
	data = []
	sql_cmd = session_query.query(Keracolor_New_stock_table).all()
	
	for re in sql_cmd: data.insert(0,(re.UNAME, re.ITEM_NAME, re.UNITS,re.QUANTITY, re.DATE)) 
	return allow_cross_origin(json.JSONEncoder().encode(data))



# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> BY NAME
@app.route ('/keracolor_stock_view_by_name',methods=['POST','GET'])
def keracolor_stock_view_by_name ():
	DBsession = sessionmaker(bind=keracolor_db_connection)
	session_query = DBsession()
	if request.method == 'POST':
		name = request.form['name']
		results = session_query.query(Keracolor_New_stock_table).filter(Keracolor_New_stock_table.ITEM_NAME == name)
		data = []
		for name in results: data.insert(0,(name.UNAME, name.ITEM_NAME, name.UNITS,name.QUANTITY,name.DATE)) 
		return allow_cross_origin(json.JSONEncoder().encode(data))


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> DATE
@app.route('/keracolor_stock_view_by_date_today', methods=['POST','GET'])
def keracolor_view_by_today ():
	DBsession = sessionmaker(bind=keracolor_db_connection)
	session_query = DBsession()
	data = []
	Today = datetime.date.today ()
	results = session_query.query(Keracolor_New_stock_table ).filter(Keracolor_New_stock_table .DATE == Today)
	for re in results: data.insert(0,(re.UNAME,re.ITEM_NAME, re.UNITS,re.QUANTITY,re.DATE)) 
	return allow_cross_origin(json.JSONEncoder().encode(data))


@app.route('/keracolor_stock_view_by_date_date', methods=['POST','GET'])
def keracolor_view_date_date ():
	DBsession = sessionmaker(bind=keracolor_db_connection)
	session_query = DBsession()
	data = []
	if request.method == 'POST':
		Date = request.form['date']
		results = session_query.query(Keracolor_New_stock_table ).filter(Keracolor_New_stock_table .DATE == Date)
		for re in results: data.insert(0,(re.UNAME,re.ITEM_NAME, re.UNITS,re.QUANTITY,re.DATE)) 
		return allow_cross_origin(json.JSONEncoder().encode(data))

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> FROM TO 
@app.route('/keracolor_from_to_all', methods=['POST','GET'])
def send_keracolor_from_to_all ():
	DBsession = sessionmaker(bind=keracolor_db_connection)
	session_query = DBsession()
	data = []
	sql_cmd = session_query.query(Keracolor_New_stock_table ).all()
	for re in sql_cmd: data.insert(0,(re.UNAME, re.ITEM_NAME, re.UNITS,re. QUANTITY, re.DATE)) 
	return allow_cross_origin(json.JSONEncoder().encode(data))


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> LAST WEEK
@app.route('/keracolor_last_week_all_data', methods=['POST','GET'])
def send_keracolor_last_week_all_data ():
	DBsession = sessionmaker(bind=keracolor_db_connection)
	session_query = DBsession()
	data = []
	day_1 = datetime.date.today() - datetime.timedelta(days=0)
	day_2 = datetime.date.today() - datetime.timedelta(days=1)
	day_3 = datetime.date.today() - datetime.timedelta(days=2)
	day_4 = datetime.date.today() - datetime.timedelta(days=3)
	day_5 = datetime.date.today() - datetime.timedelta(days=4)
	day_6 = datetime.date.today() - datetime.timedelta(days=5)
	day_7 = datetime.date.today() - datetime.timedelta(days=6)
	week_days =[day_1,day_2,day_3,day_4,day_5,day_6,day_7]
	sql_cmd = session_query.query(Keracolor_New_stock_table ).filter(Keracolor_New_stock_table .DATE.in_(week_days))
	week = session_query.execute(sql_cmd)
	for paint in week: data.append(list(paint))
	return allow_cross_origin(json.JSONEncoder().encode(data))

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> THIS MONTH
@app.route('/keracolor_this_month_all_data', methods=(['POST','GET']))
def send_keracolor_this_month_all_data ():
	DBsession = sessionmaker(bind=keracolor_db_connection)
	session_query = DBsession()
	data = []
	mth = datetime.datetime.today()
	mth2 = str(mth.month) 
	current_month = '0'+ mth2
	sql_cmd = session_query.query(Keracolor_New_stock_table ).filter(Keracolor_New_stock_table .MONTH == current_month)
	for re in sql_cmd: data.insert(0,(re.UNAME, re.ITEM_NAME, re.UNITS, re. QUANTITY, re.DATE)) 
	return allow_cross_origin(json.JSONEncoder().encode(data))


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> LAST MONTH
@app.route('/keracolor_last_month_all_data', methods=(['POST','GET']))
def send_keracolor_last_month_all_data ():
	DBsession = sessionmaker(bind=keracolor_db_connection)
	session_query = DBsession()
	data = []
	lst_mth = datetime.datetime.today()
	lst_mth2 = str(lst_mth.month - 1) 
	last_month = '0'+ lst_mth2
	sql_cmd = session_query.query(Keracolor_New_stock_table ).filter(Keracolor_New_stock_table.MONTH == last_month)
	for re in sql_cmd: data.insert(0,(re.UNAME, re.ITEM_NAME, re.UNITS, re. QUANTITY, re.DATE)) 
	return allow_cross_origin(json.JSONEncoder().encode(data))






"""
		@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
		@
		@		STOCK FLOW
		@
		@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

"""

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> ALL
@app.route ('/keracolor_stock_flow_view_all',methods=['POST','GET'])
def keracolor_flow_view_all ():
	DBsession = sessionmaker(bind=keracolor_db_connection)
	session_query = DBsession()
	data = []
	sql_cmd = session_query.query(Keracolor_stock_flow_table).all()
	for re in sql_cmd: data.insert(0,(re.UNAME, re.ITEM_NAME, re.UNITS,re. QUANTITY, re.DATE)) 
	return allow_cross_origin(json.JSONEncoder().encode(data))

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> BY NAME
@app.route ('/keracolor_stock_flow_by_name',methods=['POST','GET'])
def keracolor_stock_flow_by_name ():
	DBsession = sessionmaker(bind=keracolor_db_connection)
	session_query = DBsession()
	if request.method == 'POST':
		name = request.form['name']
		results = session_query.query(Keracolor_stock_flow_table).filter(Keracolor_stock_flow_table.ITEM_NAME == name)
		data = []
		for name in results: data.insert(0,(name.UNAME, name.ITEM_NAME, name.UNITS,name.QUANTITY,name.DATE)) 
		return allow_cross_origin(json.JSONEncoder().encode(data))

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> UNITS
@app.route ('/keracolor_stock_flow_view_by_UNITS',methods=['POST','GET'])
def keracolor_flow_view_by_UNITS ():
	DBsession = sessionmaker(bind=keracolor_db_connection)
	session_query = DBsession()
	if request.method == 'POST':
		UNITS = request.form['UNITS']
		results = session_query.query(Keracolor_stock_flow_table).filter(Keracolor_stock_flow_table.UNITS == UNITS)
		data = []
		for name in results: data.insert(0,(name.UNAME, name.ITEM_NAME, name.UNITS,name.QUANTITY,name.DATE)) 
		return allow_cross_origin(json.JSONEncoder().encode(data))

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> DATE
@app.route('/keracolor_stock_flow_view_by_date_today', methods=['POST','GET'])
def keracolor_flow_view_by_today ():
	DBsession = sessionmaker(bind=keracolor_db_connection)
	session_query = DBsession()
	Today = datetime.date.today ()
	results = session_query.query(Keracolor_stock_flow_table).filter(Keracolor_stock_flow_table.DATE == Today)
	data = []
	for re in results: data.insert(0,(re.UNAME,re.ITEM_NAME, re.UNITS,re.QUANTITY,re.DATE)) 
	return allow_cross_origin(json.JSONEncoder().encode(data))


# ======================>>>>>>> stock_flow_view_by_date_date
@app.route('/keracolor_stock_flow_view_by_date_date', methods=['POST','GET'])
def keracolor_flow_view_by_date_date ():
	DBsession = sessionmaker(bind=keracolor_db_connection)
	session_query = DBsession()
	data = []
	date = request.form['date']
	if request.method == 'POST':
		results = session_query.query(Keracolor_stock_flow_table).filter(Keracolor_stock_flow_table.DATE == date)
		for re in results: data.insert(0,(re.UNAME,re.ITEM_NAME, re.UNITS,re.QUANTITY,re.DATE)) 
		return allow_cross_origin(json.JSONEncoder().encode(data))

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> FROM TO 
@app.route ('/keracolor_stock_flow_from_to_all',methods=['POST','GET'])
def keracolor_flow_From_and_To_dates ():
	DBsession = sessionmaker(bind=keracolor_db_connection)
	session_query = DBsession()
	if request.method == 'POST':
		From_date = request.form['from']
		To_date = request.form['to']
		print From_date
		print To_date
		sql_cmd = session_query.query(Keracolor_stock_flow_table).filter( Keracolor_stock_flow_table.DATE.between(From_date,To_date))
		paint = session_query.execute(sql_cmd)
		data = []
		for dates in paint: data.append(list(dates))
		return allow_cross_origin(json.JSONEncoder().encode(data))


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> LAST WEEK
@app.route('/keracolor_stock_flow_last_week_all_data',methods=['POST','GET'])
def keracolor_flow_last_week_all_data ():
	DBsession = sessionmaker(bind=keracolor_db_connection)
	session_query = DBsession()
	data = []
	day_1 = datetime.date.today() - datetime.timedelta(days=0)
	day_2 = datetime.date.today() - datetime.timedelta(days=1)
	day_3 = datetime.date.today() - datetime.timedelta(days=2)
	day_4 = datetime.date.today() - datetime.timedelta(days=3)
	day_5 = datetime.date.today() - datetime.timedelta(days=4)
	day_6 = datetime.date.today() - datetime.timedelta(days=5)
	day_7 = datetime.date.today() - datetime.timedelta(days=6)
	week_days =[day_1,day_2,day_3,day_4,day_5,day_6,day_7]
	sql_cmd = session_query.query(Keracolor_stock_flow_table).filter(Keracolor_stock_flow_table.DATE.in_(week_days))
	week = session_query.execute(sql_cmd)
	for paint in week: data.append(list(paint))
	return allow_cross_origin(json.JSONEncoder().encode(data))

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> THIS MONTH
@app.route('/keracolor_stock_flow_this_month_all_data', methods=(['POST','GET']))
def send_keracolor_stock_flow_this_month_all_data ():
	DBsession = sessionmaker(bind=keracolor_db_connection)
	session_query = DBsession()
	data = []
	mth = datetime.datetime.today()
	mth2 = str(mth.month) 
	current_month = '0'+ mth2
	sql_cmd = session_query.query(Keracolor_stock_flow_table).filter(Keracolor_stock_flow_table.MONTH == current_month)
	for re in sql_cmd: data.insert(0,(re.UNAME, re.ITEM_NAME, re.UNITS, re. QUANTITY, re.DATE)) 
	return allow_cross_origin(json.JSONEncoder().encode(data))


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> LAST MONTH
@app.route('/keracolor_stock_flow_last_month_all_data', methods=(['POST','GET']))
def send_keracolor_stock_flow_last_month_all_data ():
	DBsession = sessionmaker(bind=keracolor_db_connection)
	session_query = DBsession()
	data = []
	lst_mth = datetime.datetime.today()
	lst_mth2 = str(lst_mth.month - 1) 
	last_month = '0'+ lst_mth2
	sql_cmd = session_query.query(Keracolor_stock_flow_table).filter(Keracolor_stock_flow_table.MONTH == last_month)
	for re in sql_cmd: data.insert(0,(re.UNAME, re.ITEM_NAME, re.UNITS, re. QUANTITY, re.DATE)) 
	return allow_cross_origin(json.JSONEncoder().encode(data))

"""
		@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
		@
		@		STOCK STATUS
		@
		@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

"""

# stock status all .....
@app.route('/keracolor_stock_status_all_data', methods=(['POST','GET']))
def keracolor_status_all_data ():
	DBsession = sessionmaker(bind=keracolor_db_connection)
	session_query = DBsession()
	data = []
	sql_cmd = session_query.query(Keracolor_status_table).all()
	for re in sql_cmd: data.insert(0,(re.ITEM_NAME,re.QUANTITY)) 
	return allow_cross_origin(json.JSONEncoder().encode(data))


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> BY NAME
@app.route ('/keracolor_stock_status_by_name',methods=['POST','GET'])
def keracolor_stock_status_by_name ():
	DBsession = sessionmaker(bind=keracolor_db_connection)
	session_query = DBsession()
	if request.method == 'POST':
		name = request.form['name']
		results = session_query.query(Keracolor_status_table).filter(Keracolor_status_table.ITEM_NAME == name)
		data = []
		for name in results: data.insert(0,(name.ITEM_NAME,name.QUANTITY)) 
		return allow_cross_origin(json.JSONEncoder().encode(data))



