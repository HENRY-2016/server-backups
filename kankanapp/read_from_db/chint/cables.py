


from main_file import *
from datetime import datetime, timedelta
import datetime

cabels_db_connection = create_engine('sqlite:///data_bases/chint/cables.db')

"""
		@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
		@
		@		NEW STOCK 
		@
		@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

"""

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> ALL
@app.route ('/cabels_stock_view_all',methods=['POST','GET'])
def cabels_view_all ():
	DBsession = sessionmaker(bind=cabels_db_connection)
	session_query = DBsession()
	data = []
	sql_cmd = session_query.query(CABLES_NEW_STOCK_TABLE).all()
	
	for re in sql_cmd: data.insert(0,(re.UNAME, re.ITEM_NAME,re.QUANTITY, re.DATE)) 
	return allow_cross_origin(json.JSONEncoder().encode(data))

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> BY NAME
@app.route ('/cabels_stock_view_by_name',methods=['POST','GET'])
def cabels_view_by_name ():
	DBsession = sessionmaker(bind=cabels_db_connection)
	session_query = DBsession()
	data = []
	if request.method == 'POST':
		name = request.form['cabels_name']
		sql_cmd = session_query.query(CABLES_NEW_STOCK_TABLE).filter(CABLES_NEW_STOCK_TABLE.ITEM_NAME == name)
		for re in sql_cmd: data.insert(0,(re.UNAME, re.ITEM_NAME,re.QUANTITY, re.DATE)) 
		return allow_cross_origin(json.JSONEncoder().encode(data))

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> BY SIZE
@app.route ('/cabels_stock_view_by_size',methods=['POST','GET'])
def cabels_view_by_size ():
	DBsession = sessionmaker(bind=cabels_db_connection)
	session_query = DBsession()
	if request.method == 'POST':
		cabels_name = request.form['cabels_name']
		size = request.form['size']
		results = session_query.query(CABLES_NEW_STOCK_TABLE).filter(and_(CABLES_NEW_STOCK_TABLE.ITEM_NAME == cabels_name ,CABLES_NEW_STOCK_TABLE.SIZE == size))
		data = []
		for name in results: data.insert(0,(name.UNAME, name.ITEM_NAME, name.SIZE,name.INVOICE,name.QUANTITY,name.DATE)) 
		return allow_cross_origin(json.JSONEncoder().encode(data))

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> DATE
@app.route('/cabels_stock_view_by_date_today', methods=['POST','GET'])
def cabels_view_by_today ():
	DBsession = sessionmaker(bind=cabels_db_connection)
	session_query = DBsession()
	data = []
	Today = datetime.date.today ()
	results = session_query.query(CABLES_NEW_STOCK_TABLE).filter(CABLES_NEW_STOCK_TABLE.DATE == Today)
	for re in results: data.insert(0,(re.UNAME,re.ITEM_NAME,re.QUANTITY,re.DATE)) 
	return allow_cross_origin(json.JSONEncoder().encode(data))


@app.route('/cabels_stock_view_by_date_date', methods=['POST','GET'])
def cabels_view_date_date ():
	DBsession = sessionmaker(bind=cabels_db_connection)
	session_query = DBsession()
	data = []
	if request.method == 'POST':
		Date = request.form['date']
		results = session_query.query(CABLES_NEW_STOCK_TABLE).filter(CABLES_NEW_STOCK_TABLE.DATE == Date)
		for re in results: data.insert(0,(re.UNAME,re.ITEM_NAME,re.QUANTITY,re.DATE)) 
		return allow_cross_origin(json.JSONEncoder().encode(data))

@app.route('/cabels_stock_view_by_date_date_name', methods=['POST','GET'])
def cabels_view_by_date_date_name ():
	DBsession = sessionmaker(bind=cabels_db_connection)
	session_query = DBsession()
	data = []
	if request.method == 'POST':
		Today = request.form['date']
		cabels_name = request.form['cabels_name']
		results = session_query.query(CABLES_NEW_STOCK_TABLE).filter(CABLES_NEW_STOCK_TABLE.ITEM_NAME == cabels_name ,CABLES_NEW_STOCK_TABLE.DATE == Today)
		for re in results: data.insert(0,(re.UNAME,re.ITEM_NAME,re.QUANTITY,re.DATE)) 
		return allow_cross_origin(json.JSONEncoder().encode(data))

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> FROM TO 
@app.route('/cabels_from_to_all', methods=['POST','GET'])
def send_cabels_from_to_all ():
	DBsession = sessionmaker(bind=cabels_db_connection)
	session_query = DBsession()
	data = []
	sql_cmd = session_query.query(CABLES_NEW_STOCK_TABLE).all()
	for re in sql_cmd: data.insert(0,(re.UNAME, re.ITEM_NAME,re. QUANTITY, re.DATE)) 
	return allow_cross_origin(json.JSONEncoder().encode(data))


@app.route('/cabels_from_to_name', methods=['POST','GET'])
def send_cabels_from_to_name ():
	DBsession = sessionmaker(bind=cabels_db_connection)
	session_query = DBsession()
	data = []
	converted_data = []
	if request.method == 'POST':
		From_date = request.form['from']
		To_date = request.form['to']
		cabels_name = request.form['cabels_name']
		sql_cmd = session_query.query(CABLES_NEW_STOCK_TABLE).filter(CABLES_NEW_STOCK_TABLE.DATE.between(From_date,To_date),CABLES_NEW_STOCK_TABLE.ITEM_NAME == cabels_name)
		paint = session_query.execute(sql_cmd)
		for dates in paint: data.append(list(dates))
		return allow_cross_origin(json.JSONEncoder().encode(data))

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> LAST WEEK
@app.route('/cabels_last_week_all_data', methods=['POST','GET'])
def send_cabels_last_week_all_data ():
	DBsession = sessionmaker(bind=cabels_db_connection)
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
	sql_cmd = session_query.query(CABLES_NEW_STOCK_TABLE).filter(CABLES_NEW_STOCK_TABLE.DATE.in_(week_days))
	week = session_query.execute(sql_cmd)
	for paint in week: data.append(list(paint))
	return allow_cross_origin(json.JSONEncoder().encode(data))


@app.route('/cabels_last_week_name_data', methods=['POST','GET'])
def send_cabels_last_week_name_data ():
	DBsession = sessionmaker(bind=cabels_db_connection)
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
	if request.method == 'POST':
		cabels_name = request.form['cabels_name']
		sql_cmd = session_query.query(CABLES_NEW_STOCK_TABLE).filter(CABLES_NEW_STOCK_TABLE.DATE.in_(week_days),CABLES_NEW_STOCK_TABLE.ITEM_NAME == cabels_name)
		week = session_query.execute(sql_cmd)
		for paint in week: data.append(list(paint))
		return allow_cross_origin(json.JSONEncoder().encode(data))



# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> THIS MONTH
@app.route('/cabels_this_month_all_data', methods=(['POST','GET']))
def send_cabels_this_month_all_data ():
	DBsession = sessionmaker(bind=cabels_db_connection)
	session_query = DBsession()
	data = []
	mth = datetime.datetime.today()
	mth2 = str(mth.month) 
	current_month = '0'+ mth2
	sql_cmd = session_query.query(CABLES_NEW_STOCK_TABLE).filter(CABLES_NEW_STOCK_TABLE.MONTH == current_month)
	for re in sql_cmd: data.insert(0,(re.UNAME, re.ITEM_NAME,re. QUANTITY, re.DATE)) 
	return allow_cross_origin(json.JSONEncoder().encode(data))



@app.route('/cabels_this_month_by_name_data', methods=(['POST','GET']))
def send_cabels_this_month_by_name_data ():
	DBsession = sessionmaker(bind=cabels_db_connection)
	session_query = DBsession()
	data = []
	mth = datetime.datetime.today()
	mth2 = str(mth.month) 
	current_month = '0'+ mth2
	if request.method == 'POST':
		cabels_name = request.form['cabels_name']
		sql_cmd = session_query.query(CABLES_NEW_STOCK_TABLE).filter(CABLES_NEW_STOCK_TABLE.MONTH == current_month,CABLES_NEW_STOCK_TABLE.ITEM_NAME == cabels_name)
		for re in sql_cmd: data.insert(0,(re.UNAME, re.ITEM_NAME,re. QUANTITY, re.DATE)) 
		return allow_cross_origin(json.JSONEncoder().encode(data))

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> LAST MONTH
@app.route('/cabels_last_month_all_data', methods=(['POST','GET']))
def send_cabels_last_month_all_data ():
	DBsession = sessionmaker(bind=cabels_db_connection)
	session_query = DBsession()
	data = []
	lst_mth = datetime.datetime.today()
	lst_mth2 = str(lst_mth.month - 1) 
	last_month = '0'+ lst_mth2
	sql_cmd = session_query.query(CABLES_NEW_STOCK_TABLE).filter(CABLES_NEW_STOCK_TABLE.MONTH == last_month)
	for re in sql_cmd: data.insert(0,(re.UNAME, re.ITEM_NAME,re. QUANTITY, re.DATE)) 
	return allow_cross_origin(json.JSONEncoder().encode(data))

@app.route('/cabels_last_month_name_data', methods=(['POST','GET']))
def send_cabels_last_month_name_data ():
	DBsession = sessionmaker(bind=cabels_db_connection)
	session_query = DBsession()
	data = []
	lst_mth = datetime.datetime.today()
	lst_mth2 = str(lst_mth.month - 1) 
	last_month = '0'+ lst_mth2
	if request.method == 'POST':
		cabels_name = request.form['cabels_name']
		sql_cmd = session_query.query(CABLES_NEW_STOCK_TABLE).filter(CABLES_NEW_STOCK_TABLE.MONTH == last_month,CABLES_NEW_STOCK_TABLE.ITEM_NAME == cabels_name)
		for re in sql_cmd: data.insert(0,(re.UNAME, re.ITEM_NAME,re. QUANTITY, re.DATE)) 
		return allow_cross_origin(json.JSONEncoder().encode(data))






"""
		@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
		@
		@		STOCK FLOW
		@
		@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

"""

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> ALL
@app.route ('/cabels_stock_flow_view_all',methods=['POST','GET'])
def cabels_flow_view_all ():
	DBsession = sessionmaker(bind=cabels_db_connection)
	session_query = DBsession()
	data = []
	sql_cmd = session_query.query(CABLES_STOCK_FLOW_TABLE).all()
	for re in sql_cmd: data.insert(0,(re.UNAME, re.ITEM_NAME,re. QUANTITY, re.DATE)) 
	return allow_cross_origin(json.JSONEncoder().encode(data))

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> NAME
@app.route ('/cabels_stock_flow_view_by_name',methods=['POST','GET'])
def cabels_flow_view_by_name ():
	DBsession = sessionmaker(bind=cabels_db_connection)
	session_query = DBsession()
	if request.method == 'POST':
		name = request.form['cabels_name']
		data = []
		# sql_cmd = select([CABLES_STOCK_FLOW_TABLE], CABLES_STOCK_FLOW_TABLE.ITEM_NAME == cabels_name)
		# request_results = session_query.execute(sql_cmd)
		# data = []
		# for results in request_results: data.append(list(results)) 
		# return allow_cross_origin(json.JSONEncoder().encode(data))
		sql_cmd = session_query.query(CABLES_STOCK_FLOW_TABLE).filter(CABLES_STOCK_FLOW_TABLE.ITEM_NAME == name)
		for re in sql_cmd: data.insert(0,(re.UNAME, re.ITEM_NAME,re.QUANTITY, re.DATE))
		print "..................."
		print data 
		return allow_cross_origin(json.JSONEncoder().encode(data))


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> SIZE
# @app.route ('/cabels_stock_flow_view_by_size',methods=['POST','GET'])
# def cabels_flow_view_by_size ():
# 	DBsession = sessionmaker(bind=cabels_db_connection)
# 	session_query = DBsession()
# 	if request.method == 'POST':
# 		cabels_name = request.form['cabels_name']
# 		size = request.form['size']
# 		print cabels_name
# 		print size
# 		results = session_query.query(CABLES_STOCK_FLOW_TABLE).filter(and_(CABLES_STOCK_FLOW_TABLE.ITEM_NAME == cabels_name ,CABLES_STOCK_FLOW_TABLE.SIZE == size))
# 		data = []
# 		for name in results: data.insert(0,(name.UNAME, name.ITEM_NAME,name.QUANTITY,)) 
# 		return allow_cross_origin(json.JSONEncoder().encode(data))

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> DATE
@app.route('/cabels_stock_flow_view_by_date_today', methods=['POST','GET'])
def cabels_flow_view_by_today ():
	DBsession = sessionmaker(bind=cabels_db_connection)
	session_query = DBsession()
	Today = datetime.date.today ()
	results = session_query.query(CABLES_STOCK_FLOW_TABLE).filter(CABLES_STOCK_FLOW_TABLE.DATE == Today)
	data = []
	for re in results: data.insert(0,(re.UNAME,re.ITEM_NAME,re.QUANTITY,re.DATE)) 
	return allow_cross_origin(json.JSONEncoder().encode(data))


# ======================>>>>>>> stock_flow_view_by_date_date
@app.route('/cabels_stock_flow_view_by_date_date', methods=['POST','GET'])
def cabels_flow_view_by_date_date ():
	DBsession = sessionmaker(bind=cabels_db_connection)
	session_query = DBsession()
	data = []
	date = request.form['date']
	if request.method == 'POST':
		results = session_query.query(CABLES_STOCK_FLOW_TABLE).filter(CABLES_STOCK_FLOW_TABLE.DATE == date)
		for re in results: data.insert(0,(re.UNAME,re.ITEM_NAME,re.QUANTITY,re.DATE)) 
		return allow_cross_origin(json.JSONEncoder().encode(data))

# ======================>>>>>>> stock_flow_view_by_name_date
@app.route('/cabels_stock_flow_by_date_date_name', methods=['POST','GET'])
def cabels_flow_by_date_name ():
	DBsession = sessionmaker(bind=cabels_db_connection)
	session_query = DBsession()
	data = []
	Today = request.form['date']
	cabels_name = request.form['cabels_name']
	if request.method == 'POST':
		results = session_query.query(CABLES_STOCK_FLOW_TABLE).filter(and_(CABLES_STOCK_FLOW_TABLE.ITEM_NAME == cabels_name ,CABLES_STOCK_FLOW_TABLE.DATE == Today))
		for re in results: data.insert(0,(re.UNAME,re.ITEM_NAME,re.QUANTITY,re.DATE)) 
		return allow_cross_origin(json.JSONEncoder().encode(data))


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> FROM TO 
@app.route ('/cabels_stock_flow_from_to_all',methods=['POST','GET'])
def cabels_flow_From_and_To_dates ():
	DBsession = sessionmaker(bind=cabels_db_connection)
	session_query = DBsession()
	if request.method == 'POST':
		From_date = request.form['from']
		To_date = request.form['to']
		print From_date
		print To_date
		sql_cmd = session_query.query(CABLES_STOCK_FLOW_TABLE).filter( CABLES_STOCK_FLOW_TABLE.DATE.between(From_date,To_date))
		paint = session_query.execute(sql_cmd)
		data = []
		for dates in paint: data.append(list(dates))
		return allow_cross_origin(json.JSONEncoder().encode(data))


@app.route ('/cabels_stock_flow_from_to_name',methods=['POST','GET'])
def cabels_flow_From_and_To_name():
	DBsession = sessionmaker(bind=cabels_db_connection)
	session_query = DBsession()
	data = []
	if request.method == 'POST':
		From_date = request.form['from']
		To_date = request.form['to']
		cabels_name = request.form['cabels_name']
		sql_cmd = session_query.query(CABLES_STOCK_FLOW_TABLE).filter( CABLES_STOCK_FLOW_TABLE.DATE.between(From_date,To_date),CABLES_STOCK_FLOW_TABLE.ITEM_NAME == cabels_name)
		paint = session_query.execute(sql_cmd)
		for dates in paint: data.append(list(dates))
		return allow_cross_origin(json.JSONEncoder().encode(data))


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> LAST WEEK
@app.route('/cabels_stock_flow_last_week_all_data',methods=['POST','GET'])
def cabels_flow_last_week_all_data ():
	DBsession = sessionmaker(bind=cabels_db_connection)
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
	sql_cmd = session_query.query(CABLES_STOCK_FLOW_TABLE).filter(CABLES_STOCK_FLOW_TABLE.DATE.in_(week_days))
	week = session_query.execute(sql_cmd)
	for paint in week: data.append(list(paint))
	return allow_cross_origin(json.JSONEncoder().encode(data))

@app.route('/cabels_stock_flow_last_week_name_data',methods=['POST','GET'])
def cabels_flow_last_week_name_data ():
	DBsession = sessionmaker(bind=cabels_db_connection)
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
	if request.method == 'POST':
		cabels_name = request.form['cabels_name']
		sql_cmd = session_query.query(CABLES_STOCK_FLOW_TABLE).filter(CABLES_STOCK_FLOW_TABLE.DATE.in_(week_days),CABLES_STOCK_FLOW_TABLE.ITEM_NAME == cabels_name)
		week = session_query.execute(sql_cmd)
		for paint in week: data.append(list(paint))
		return allow_cross_origin(json.JSONEncoder().encode(data))


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> THIS MONTH
@app.route('/cabels_stock_flow_this_month_all_data', methods=(['POST','GET']))
def send_cabels_stock_flow_this_month_all_data ():
	DBsession = sessionmaker(bind=cabels_db_connection)
	session_query = DBsession()
	data = []
	mth = datetime.datetime.today()
	mth2 = str(mth.month) 
	current_month = '0'+ mth2
	sql_cmd = session_query.query(CABLES_STOCK_FLOW_TABLE).filter(CABLES_STOCK_FLOW_TABLE.MONTH == current_month)
	for re in sql_cmd: data.insert(0,(re.UNAME, re.ITEM_NAME,re. QUANTITY, re.DATE)) 
	return allow_cross_origin(json.JSONEncoder().encode(data))


@app.route('/cabels_stock_flow_this_month_by_name_data', methods=(['POST','GET']))
def cabels_flow_this_month_name_data ():
	DBsession = sessionmaker(bind=cabels_db_connection)
	session_query = DBsession()
	data = []
	mth = datetime.datetime.today()
	mth2 = str(mth.month) 
	current_month = '0'+ mth2
	if request.method == 'POST':
		cabels_name = request.form['cabels_name']
		sql_cmd = session_query.query(CABLES_STOCK_FLOW_TABLE).filter(CABLES_STOCK_FLOW_TABLE.MONTH == current_month,CABLES_STOCK_FLOW_TABLE.ITEM_NAME == cabels_name)
		for re in sql_cmd: data.insert(0,(re.UNAME, re.ITEM_NAME, re. QUANTITY, re.DATE)) 
		return allow_cross_origin(json.JSONEncoder().encode(data))


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> LAST MONTH
@app.route('/cabels_stock_flow_last_month_all_data', methods=(['POST','GET']))
def send_cabels_stock_flow_last_month_all_data ():
	DBsession = sessionmaker(bind=cabels_db_connection)
	session_query = DBsession()
	data = []
	lst_mth = datetime.datetime.today()
	lst_mth2 = str(lst_mth.month - 1) 
	last_month = '0'+ lst_mth2
	sql_cmd = session_query.query(CABLES_STOCK_FLOW_TABLE).filter(CABLES_STOCK_FLOW_TABLE.MONTH == last_month)
	for re in sql_cmd: data.insert(0,(re.UNAME, re.ITEM_NAME, re. QUANTITY, re.DATE)) 
	return allow_cross_origin(json.JSONEncoder().encode(data))


# stock flow last month name ....
@app.route('/cabels_stock_flow_last_month_name_data', methods=(['POST','GET']))
def cabels_last_month_name_data ():
	DBsession = sessionmaker(bind=cabels_db_connection)
	session_query = DBsession()
	data = []
	lst_mth = datetime.datetime.today()
	lst_mth2 = str(lst_mth.month - 1) 
	last_month = '0'+ lst_mth2
	if request.method == 'POST':
		cabels_name = request.form['cabels_name']
		sql_cmd = session_query.query(CABLES_STOCK_FLOW_TABLE).filter(CABLES_STOCK_FLOW_TABLE.MONTH == last_month,CABLES_STOCK_FLOW_TABLE.ITEM_NAME == cabels_name)
		for re in sql_cmd: data.insert(0,(re.UNAME, re.ITEM_NAME, re. QUANTITY, re.DATE)) 
		return allow_cross_origin(json.JSONEncoder().encode(data))


"""
		@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
		@
		@		STOCK STATUS
		@
		@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

"""

# stock status all .....
@app.route('/cabels_stock_status_all_data', methods=(['POST','GET']))
def cabels_status_all_data ():
	print "============================================================"
	DBsession = sessionmaker(bind=cabels_db_connection)
	session_query = DBsession()
	data = []
	sql_cmd = session_query.query(CABLES_STATUS_TABLE).all()
	for re in sql_cmd: data.insert(0,(re.ITEM_NAME,re.QUANTITY)) 
	return allow_cross_origin(json.JSONEncoder().encode(data))



# stock status name .....
@app.route('/cabels_stock_status_name_data', methods=(['POST','GET']))
def cabels_status_name_data ():
	DBsession = sessionmaker(bind=cabels_db_connection)
	session_query = DBsession()
	data = []
	if request.method == 'POST':
		cabels_name = request.form['cabels_name']
		print cabels_name	
		sql_cmd = session_query.query(CABLES_STATUS_TABLE).filter(CABLES_STATUS_TABLE.ITEM_NAME == cabels_name)
		for re in sql_cmd: data.insert(0,(re.ITEM_NAME,re.QUANTITY)) 
		return allow_cross_origin(json.JSONEncoder().encode(data))





