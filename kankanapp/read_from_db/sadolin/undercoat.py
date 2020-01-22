


from main_file import *
from datetime import datetime, timedelta
import datetime

undercoat_db_connection = create_engine('sqlite:///data_bases/sadolin/undercoat.db')

"""
		@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
		@
		@		NEW STOCK 
		@
		@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

"""

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> ALL
@app.route ('/undercoat_stock_view_all',methods=['POST','GET'])
def undercoat_view_all ():
	DBsession = sessionmaker(bind=undercoat_db_connection)
	session_query = DBsession()
	data = []
	sql_cmd = session_query.query(Undercoat_New_stock_table).all()
	
	for re in sql_cmd: data.insert(0,(re.UNAME, re.ITEM_NAME, re.SIZE, re.INVOICE,re.QUANTITY, re.DATE)) 
	return allow_cross_origin(json.JSONEncoder().encode(data))


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> BY SIZE
@app.route ('/undercoat_stock_view_by_size',methods=['POST','GET'])
def undercoat_view_by_size ():
	DBsession = sessionmaker(bind=undercoat_db_connection)
	session_query = DBsession()
	if request.method == 'POST':
		size = request.form['size']
		results = session_query.query(Undercoat_New_stock_table).filter(Undercoat_New_stock_table.SIZE == size)
		data = []
		for name in results: data.insert(0,(name.UNAME, name.ITEM_NAME, name.SIZE,name.INVOICE,name.QUANTITY,name.DATE)) 
		return allow_cross_origin(json.JSONEncoder().encode(data))

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> DATE
@app.route('/undercoat_stock_view_by_date_today', methods=['POST','GET'])
def undercoat_view_by_today ():
	DBsession = sessionmaker(bind=undercoat_db_connection)
	session_query = DBsession()
	data = []
	Today = datetime.date.today ()
	results = session_query.query(Undercoat_New_stock_table).filter(Undercoat_New_stock_table.DATE == Today)
	for re in results: data.insert(0,(re.UNAME,re.ITEM_NAME, re.SIZE,re.INVOICE,re.QUANTITY,re.DATE)) 
	return allow_cross_origin(json.JSONEncoder().encode(data))


@app.route('/undercoat_stock_view_by_date_date', methods=['POST','GET'])
def undercoat_view_date_date ():
	DBsession = sessionmaker(bind=undercoat_db_connection)
	session_query = DBsession()
	data = []
	if request.method == 'POST':
		Date = request.form['date']
		results = session_query.query(Undercoat_New_stock_table).filter(Undercoat_New_stock_table.DATE == Date)
		for re in results: data.insert(0,(re.UNAME,re.ITEM_NAME, re.SIZE,re.INVOICE,re.QUANTITY,re.DATE)) 
		return allow_cross_origin(json.JSONEncoder().encode(data))

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> FROM TO 
@app.route('/undercoat_from_to_all', methods=['POST','GET'])
def send_undercoat_from_to_all ():
	DBsession = sessionmaker(bind=undercoat_db_connection)
	session_query = DBsession()
	data = []
	sql_cmd = session_query.query(Undercoat_New_stock_table).all()
	for re in sql_cmd: data.insert(0,(re.UNAME, re.ITEM_NAME, re.SIZE, re.INVOICE,re. QUANTITY, re.DATE)) 
	return allow_cross_origin(json.JSONEncoder().encode(data))


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> LAST WEEK
@app.route('/undercoat_last_week_all_data', methods=['POST','GET'])
def send_undercoat_last_week_all_data ():
	DBsession = sessionmaker(bind=undercoat_db_connection)
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
	sql_cmd = session_query.query(Undercoat_New_stock_table).filter(Undercoat_New_stock_table.DATE.in_(week_days))
	week = session_query.execute(sql_cmd)
	for paint in week: data.append(list(paint))
	return allow_cross_origin(json.JSONEncoder().encode(data))

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> THIS MONTH
@app.route('/undercoat_this_month_all_data', methods=(['POST','GET']))
def send_undercoat_this_month_all_data ():
	DBsession = sessionmaker(bind=undercoat_db_connection)
	session_query = DBsession()
	data = []
	mth = datetime.datetime.today()
	mth2 = str(mth.month) 
	current_month = '0'+ mth2
	sql_cmd = session_query.query(Undercoat_New_stock_table).filter(Undercoat_New_stock_table.MONTH == current_month)
	for re in sql_cmd: data.insert(0,(re.UNAME, re.ITEM_NAME, re.SIZE, re.INVOICE, re. QUANTITY, re.DATE)) 
	return allow_cross_origin(json.JSONEncoder().encode(data))


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> LAST MONTH
@app.route('/undercoat_last_month_all_data', methods=(['POST','GET']))
def send_undercoat_last_month_all_data ():
	DBsession = sessionmaker(bind=undercoat_db_connection)
	session_query = DBsession()
	data = []
	lst_mth = datetime.datetime.today()
	lst_mth2 = str(lst_mth.month - 1) 
	last_month = '0'+ lst_mth2
	sql_cmd = session_query.query(Undercoat_New_stock_table).filter(Undercoat_New_stock_table.MONTH == last_month)
	for re in sql_cmd: data.insert(0,(re.UNAME, re.ITEM_NAME, re.SIZE, re.INVOICE, re. QUANTITY, re.DATE)) 
	return allow_cross_origin(json.JSONEncoder().encode(data))






"""
		@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
		@
		@		STOCK FLOW
		@
		@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

"""

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> ALL
@app.route ('/undercoat_stock_flow_view_all',methods=['POST','GET'])
def undercoat_flow_view_all ():
	DBsession = sessionmaker(bind=undercoat_db_connection)
	session_query = DBsession()
	data = []
	sql_cmd = session_query.query(Undercoat_stock_flow_table).all()
	for re in sql_cmd: data.insert(0,(re.UNAME, re.ITEM_NAME, re.SIZE,re. QUANTITY, re.DATE)) 
	return allow_cross_origin(json.JSONEncoder().encode(data))

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> SIZE
@app.route ('/undercoat_stock_flow_view_by_size',methods=['POST','GET'])
def undercoat_flow_view_by_size ():
	DBsession = sessionmaker(bind=undercoat_db_connection)
	session_query = DBsession()
	if request.method == 'POST':
		size = request.form['size']
		results = session_query.query(Undercoat_stock_flow_table).filter(Undercoat_stock_flow_table.SIZE == size)
		data = []
		for name in results: data.insert(0,(name.UNAME, name.ITEM_NAME, name.SIZE,name.QUANTITY,name.DATE)) 
		return allow_cross_origin(json.JSONEncoder().encode(data))

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> DATE
@app.route('/undercoat_stock_flow_view_by_date_today', methods=['POST','GET'])
def undercoat_flow_view_by_today ():
	DBsession = sessionmaker(bind=undercoat_db_connection)
	session_query = DBsession()
	Today = datetime.date.today ()
	results = session_query.query(Undercoat_stock_flow_table).filter(Undercoat_stock_flow_table.DATE == Today)
	data = []
	for re in results: data.insert(0,(re.UNAME,re.ITEM_NAME, re.SIZE,re.QUANTITY,re.DATE)) 
	return allow_cross_origin(json.JSONEncoder().encode(data))


# ======================>>>>>>> stock_flow_view_by_date_date
@app.route('/undercoat_stock_flow_view_by_date_date', methods=['POST','GET'])
def undercoat_flow_view_by_date_date ():
	DBsession = sessionmaker(bind=undercoat_db_connection)
	session_query = DBsession()
	data = []
	date = request.form['date']
	if request.method == 'POST':
		results = session_query.query(Undercoat_stock_flow_table).filter(Undercoat_stock_flow_table.DATE == date)
		for re in results: data.insert(0,(re.UNAME,re.ITEM_NAME, re.SIZE,re.QUANTITY,re.DATE)) 
		return allow_cross_origin(json.JSONEncoder().encode(data))

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> FROM TO 
@app.route ('/undercoat_stock_flow_from_to_all',methods=['POST','GET'])
def undercoat_flow_From_and_To_dates ():
	DBsession = sessionmaker(bind=undercoat_db_connection)
	session_query = DBsession()
	if request.method == 'POST':
		From_date = request.form['from']
		To_date = request.form['to']
		print From_date
		print To_date
		sql_cmd = session_query.query(Undercoat_stock_flow_table).filter( Undercoat_stock_flow_table.DATE.between(From_date,To_date))
		paint = session_query.execute(sql_cmd)
		data = []
		for dates in paint: data.append(list(dates))
		return allow_cross_origin(json.JSONEncoder().encode(data))


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> LAST WEEK
@app.route('/undercoat_stock_flow_last_week_all_data',methods=['POST','GET'])
def undercoat_flow_last_week_all_data ():
	DBsession = sessionmaker(bind=undercoat_db_connection)
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
	sql_cmd = session_query.query(Undercoat_stock_flow_table).filter(Undercoat_stock_flow_table.DATE.in_(week_days))
	week = session_query.execute(sql_cmd)
	for paint in week: data.append(list(paint))
	return allow_cross_origin(json.JSONEncoder().encode(data))

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> THIS MONTH
@app.route('/undercoat_stock_flow_this_month_all_data', methods=(['POST','GET']))
def send_undercoat_stock_flow_this_month_all_data ():
	DBsession = sessionmaker(bind=undercoat_db_connection)
	session_query = DBsession()
	data = []
	mth = datetime.datetime.today()
	mth2 = str(mth.month) 
	current_month = '0'+ mth2
	sql_cmd = session_query.query(Undercoat_stock_flow_table).filter(Undercoat_stock_flow_table.MONTH == current_month)
	for re in sql_cmd: data.insert(0,(re.UNAME, re.ITEM_NAME, re.SIZE, re. QUANTITY, re.DATE)) 
	return allow_cross_origin(json.JSONEncoder().encode(data))


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> LAST MONTH
@app.route('/undercoat_stock_flow_last_month_all_data', methods=(['POST','GET']))
def send_undercoat_stock_flow_last_month_all_data ():
	DBsession = sessionmaker(bind=undercoat_db_connection)
	session_query = DBsession()
	data = []
	lst_mth = datetime.datetime.today()
	lst_mth2 = str(lst_mth.month - 1) 
	last_month = '0'+ lst_mth2
	sql_cmd = session_query.query(Undercoat_stock_flow_table).filter(Undercoat_stock_flow_table.MONTH == last_month)
	for re in sql_cmd: data.insert(0,(re.UNAME, re.ITEM_NAME, re.SIZE, re. QUANTITY, re.DATE)) 
	return allow_cross_origin(json.JSONEncoder().encode(data))

"""
		@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
		@
		@		STOCK STATUS
		@
		@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

"""

# stock status all .....
@app.route('/undercoat_stock_status_all_data', methods=(['POST','GET']))
def undercoat_status_all_data ():
	DBsession = sessionmaker(bind=undercoat_db_connection)
	session_query = DBsession()
	data = []
	sql_cmd = session_query.query(Undercoat_status_table).all()
	for re in sql_cmd: data.insert(0,(re.ITEM_NAME,re.TWENTY_LTR, re.FOUR_LTR)) 
	return allow_cross_origin(json.JSONEncoder().encode(data))





