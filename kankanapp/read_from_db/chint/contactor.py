


from main_file import *
from datetime import datetime, timedelta
import datetime

contactor_db_connection = create_engine('sqlite:///data_bases/chint/contactor.db')

"""
		@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
		@
		@		NEW STOCK 
		@
		@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

"""

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> ALL
@app.route ('/contactor_stock_view_all',methods=['POST','GET'])
def contactor_view_all ():
	DBsession = sessionmaker(bind=contactor_db_connection)
	session_query = DBsession()
	data = []
	sql_cmd = session_query.query(CONTACTOR_NEW_STOCK_TABLE).all()
	
	for re in sql_cmd: data.insert(0,(re.UNAME, re.ITEM_NAME,re.QUANTITY, re.DATE)) 
	return allow_cross_origin(json.JSONEncoder().encode(data))

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> BY NAME
@app.route ('/contactor_stock_view_by_name',methods=['POST','GET'])
def contactor_view_by_name ():
	DBsession = sessionmaker(bind=contactor_db_connection)
	session_query = DBsession()
	data = []
	if request.method == 'POST':
		name = request.form['contactor_name']
		sql_cmd = session_query.query(CONTACTOR_NEW_STOCK_TABLE).filter(CONTACTOR_NEW_STOCK_TABLE.ITEM_NAME == name)
		for re in sql_cmd: data.insert(0,(re.UNAME, re.ITEM_NAME,re.QUANTITY, re.DATE)) 
		return allow_cross_origin(json.JSONEncoder().encode(data))

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> BY SIZE
@app.route ('/contactor_stock_view_by_size',methods=['POST','GET'])
def contactor_view_by_size ():
	DBsession = sessionmaker(bind=contactor_db_connection)
	session_query = DBsession()
	if request.method == 'POST':
		contactor_name = request.form['contactor_name']
		size = request.form['size']
		results = session_query.query(CONTACTOR_NEW_STOCK_TABLE).filter(and_(CONTACTOR_NEW_STOCK_TABLE.ITEM_NAME == contactor_name ,CONTACTOR_NEW_STOCK_TABLE.SIZE == size))
		data = []
		for name in results: data.insert(0,(name.UNAME, name.ITEM_NAME, name.SIZE,name.INVOICE,name.QUANTITY,name.DATE)) 
		return allow_cross_origin(json.JSONEncoder().encode(data))

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> DATE
@app.route('/contactor_stock_view_by_date_today', methods=['POST','GET'])
def contactor_view_by_today ():
	DBsession = sessionmaker(bind=contactor_db_connection)
	session_query = DBsession()
	data = []
	Today = datetime.date.today ()
	results = session_query.query(CONTACTOR_NEW_STOCK_TABLE).filter(CONTACTOR_NEW_STOCK_TABLE.DATE == Today)
	for re in results: data.insert(0,(re.UNAME,re.ITEM_NAME,re.QUANTITY,re.DATE)) 
	return allow_cross_origin(json.JSONEncoder().encode(data))


@app.route('/contactor_stock_view_by_date_date', methods=['POST','GET'])
def contactor_view_date_date ():
	DBsession = sessionmaker(bind=contactor_db_connection)
	session_query = DBsession()
	data = []
	if request.method == 'POST':
		Date = request.form['date']
		results = session_query.query(CONTACTOR_NEW_STOCK_TABLE).filter(CONTACTOR_NEW_STOCK_TABLE.DATE == Date)
		for re in results: data.insert(0,(re.UNAME,re.ITEM_NAME,re.QUANTITY,re.DATE)) 
		return allow_cross_origin(json.JSONEncoder().encode(data))

@app.route('/contactor_stock_view_by_date_date_name', methods=['POST','GET'])
def contactor_view_by_date_date_name ():
	DBsession = sessionmaker(bind=contactor_db_connection)
	session_query = DBsession()
	data = []
	if request.method == 'POST':
		Today = request.form['date']
		contactor_name = request.form['contactor_name']
		results = session_query.query(CONTACTOR_NEW_STOCK_TABLE).filter(CONTACTOR_NEW_STOCK_TABLE.ITEM_NAME == contactor_name ,CONTACTOR_NEW_STOCK_TABLE.DATE == Today)
		for re in results: data.insert(0,(re.UNAME,re.ITEM_NAME,re.QUANTITY,re.DATE)) 
		return allow_cross_origin(json.JSONEncoder().encode(data))

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> FROM TO 
@app.route('/contactor_from_to_all', methods=['POST','GET'])
def send_contactor_from_to_all ():
	DBsession = sessionmaker(bind=contactor_db_connection)
	session_query = DBsession()
	data = []
	sql_cmd = session_query.query(CONTACTOR_NEW_STOCK_TABLE).all()
	for re in sql_cmd: data.insert(0,(re.UNAME, re.ITEM_NAME,re. QUANTITY, re.DATE)) 
	return allow_cross_origin(json.JSONEncoder().encode(data))


@app.route('/contactor_from_to_name', methods=['POST','GET'])
def send_contactor_from_to_name ():
	DBsession = sessionmaker(bind=contactor_db_connection)
	session_query = DBsession()
	data = []
	converted_data = []
	if request.method == 'POST':
		From_date = request.form['from']
		To_date = request.form['to']
		contactor_name = request.form['contactor_name']
		sql_cmd = session_query.query(CONTACTOR_NEW_STOCK_TABLE).filter(CONTACTOR_NEW_STOCK_TABLE.DATE.between(From_date,To_date),CONTACTOR_NEW_STOCK_TABLE.ITEM_NAME == contactor_name)
		paint = session_query.execute(sql_cmd)
		for dates in paint: data.append(list(dates))
		return allow_cross_origin(json.JSONEncoder().encode(data))

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> LAST WEEK
@app.route('/contactor_last_week_all_data', methods=['POST','GET'])
def send_contactor_last_week_all_data ():
	DBsession = sessionmaker(bind=contactor_db_connection)
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
	sql_cmd = session_query.query(CONTACTOR_NEW_STOCK_TABLE).filter(CONTACTOR_NEW_STOCK_TABLE.DATE.in_(week_days))
	week = session_query.execute(sql_cmd)
	for paint in week: data.append(list(paint))
	return allow_cross_origin(json.JSONEncoder().encode(data))


@app.route('/contactor_last_week_name_data', methods=['POST','GET'])
def send_contactor_last_week_name_data ():
	DBsession = sessionmaker(bind=contactor_db_connection)
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
		contactor_name = request.form['contactor_name']
		sql_cmd = session_query.query(CONTACTOR_NEW_STOCK_TABLE).filter(CONTACTOR_NEW_STOCK_TABLE.DATE.in_(week_days),CONTACTOR_NEW_STOCK_TABLE.ITEM_NAME == contactor_name)
		week = session_query.execute(sql_cmd)
		for paint in week: data.append(list(paint))
		return allow_cross_origin(json.JSONEncoder().encode(data))



# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> THIS MONTH
@app.route('/contactor_this_month_all_data', methods=(['POST','GET']))
def send_contactor_this_month_all_data ():
	DBsession = sessionmaker(bind=contactor_db_connection)
	session_query = DBsession()
	data = []
	mth = datetime.datetime.today()
	mth2 = str(mth.month) 
	current_month = '0'+ mth2
	sql_cmd = session_query.query(CONTACTOR_NEW_STOCK_TABLE).filter(CONTACTOR_NEW_STOCK_TABLE.MONTH == current_month)
	for re in sql_cmd: data.insert(0,(re.UNAME, re.ITEM_NAME,re. QUANTITY, re.DATE)) 
	return allow_cross_origin(json.JSONEncoder().encode(data))



@app.route('/contactor_this_month_by_name_data', methods=(['POST','GET']))
def send_contactor_this_month_by_name_data ():
	DBsession = sessionmaker(bind=contactor_db_connection)
	session_query = DBsession()
	data = []
	mth = datetime.datetime.today()
	mth2 = str(mth.month) 
	current_month = '0'+ mth2
	if request.method == 'POST':
		contactor_name = request.form['contactor_name']
		sql_cmd = session_query.query(CONTACTOR_NEW_STOCK_TABLE).filter(CONTACTOR_NEW_STOCK_TABLE.MONTH == current_month,CONTACTOR_NEW_STOCK_TABLE.ITEM_NAME == contactor_name)
		for re in sql_cmd: data.insert(0,(re.UNAME, re.ITEM_NAME,re. QUANTITY, re.DATE)) 
		return allow_cross_origin(json.JSONEncoder().encode(data))

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> LAST MONTH
@app.route('/contactor_last_month_all_data', methods=(['POST','GET']))
def send_contactor_last_month_all_data ():
	DBsession = sessionmaker(bind=contactor_db_connection)
	session_query = DBsession()
	data = []
	lst_mth = datetime.datetime.today()
	lst_mth2 = str(lst_mth.month - 1) 
	last_month = '0'+ lst_mth2
	sql_cmd = session_query.query(CONTACTOR_NEW_STOCK_TABLE).filter(CONTACTOR_NEW_STOCK_TABLE.MONTH == last_month)
	for re in sql_cmd: data.insert(0,(re.UNAME, re.ITEM_NAME,re. QUANTITY, re.DATE)) 
	return allow_cross_origin(json.JSONEncoder().encode(data))

@app.route('/contactor_last_month_name_data', methods=(['POST','GET']))
def send_contactor_last_month_name_data ():
	DBsession = sessionmaker(bind=contactor_db_connection)
	session_query = DBsession()
	data = []
	lst_mth = datetime.datetime.today()
	lst_mth2 = str(lst_mth.month - 1) 
	last_month = '0'+ lst_mth2
	if request.method == 'POST':
		contactor_name = request.form['contactor_name']
		sql_cmd = session_query.query(CONTACTOR_NEW_STOCK_TABLE).filter(CONTACTOR_NEW_STOCK_TABLE.MONTH == last_month,CONTACTOR_NEW_STOCK_TABLE.ITEM_NAME == contactor_name)
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
@app.route ('/contactor_stock_flow_view_all',methods=['POST','GET'])
def contactor_flow_view_all ():
	DBsession = sessionmaker(bind=contactor_db_connection)
	session_query = DBsession()
	data = []
	sql_cmd = session_query.query(CONTACTOR_STOCK_FLOW_TABLE).all()
	for re in sql_cmd: data.insert(0,(re.UNAME, re.ITEM_NAME,re. QUANTITY, re.DATE)) 
	return allow_cross_origin(json.JSONEncoder().encode(data))

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> NAME
@app.route ('/contactor_stock_flow_view_by_name',methods=['POST','GET'])
def contactor_flow_view_by_name ():
	DBsession = sessionmaker(bind=contactor_db_connection)
	session_query = DBsession()
	if request.method == 'POST':
		name = request.form['contactor_name']
		data = []
		# sql_cmd = select([CONTACTOR_STOCK_FLOW_TABLE], CONTACTOR_STOCK_FLOW_TABLE.ITEM_NAME == contactor_name)
		# request_results = session_query.execute(sql_cmd)
		# data = []
		# for results in request_results: data.append(list(results)) 
		# return allow_cross_origin(json.JSONEncoder().encode(data))
		sql_cmd = session_query.query(CONTACTOR_STOCK_FLOW_TABLE).filter(CONTACTOR_STOCK_FLOW_TABLE.ITEM_NAME == name)
		for re in sql_cmd: data.insert(0,(re.UNAME, re.ITEM_NAME,re.QUANTITY, re.DATE))
		print "..................."
		print data 
		return allow_cross_origin(json.JSONEncoder().encode(data))


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> SIZE
# @app.route ('/contactor_stock_flow_view_by_size',methods=['POST','GET'])
# def contactor_flow_view_by_size ():
# 	DBsession = sessionmaker(bind=contactor_db_connection)
# 	session_query = DBsession()
# 	if request.method == 'POST':
# 		contactor_name = request.form['contactor_name']
# 		size = request.form['size']
# 		print contactor_name
# 		print size
# 		results = session_query.query(CONTACTOR_STOCK_FLOW_TABLE).filter(and_(CONTACTOR_STOCK_FLOW_TABLE.ITEM_NAME == contactor_name ,CONTACTOR_STOCK_FLOW_TABLE.SIZE == size))
# 		data = []
# 		for name in results: data.insert(0,(name.UNAME, name.ITEM_NAME,name.QUANTITY,)) 
# 		return allow_cross_origin(json.JSONEncoder().encode(data))

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> DATE
@app.route('/contactor_stock_flow_view_by_date_today', methods=['POST','GET'])
def contactor_flow_view_by_today ():
	DBsession = sessionmaker(bind=contactor_db_connection)
	session_query = DBsession()
	Today = datetime.date.today ()
	results = session_query.query(CONTACTOR_STOCK_FLOW_TABLE).filter(CONTACTOR_STOCK_FLOW_TABLE.DATE == Today)
	data = []
	for re in results: data.insert(0,(re.UNAME,re.ITEM_NAME,re.QUANTITY,re.DATE)) 
	return allow_cross_origin(json.JSONEncoder().encode(data))


# ======================>>>>>>> stock_flow_view_by_date_date
@app.route('/contactor_stock_flow_view_by_date_date', methods=['POST','GET'])
def contactor_flow_view_by_date_date ():
	DBsession = sessionmaker(bind=contactor_db_connection)
	session_query = DBsession()
	data = []
	date = request.form['date']
	if request.method == 'POST':
		results = session_query.query(CONTACTOR_STOCK_FLOW_TABLE).filter(CONTACTOR_STOCK_FLOW_TABLE.DATE == date)
		for re in results: data.insert(0,(re.UNAME,re.ITEM_NAME,re.QUANTITY,re.DATE)) 
		return allow_cross_origin(json.JSONEncoder().encode(data))

# ======================>>>>>>> stock_flow_view_by_name_date
@app.route('/contactor_stock_flow_by_date_date_name', methods=['POST','GET'])
def contactor_flow_by_date_name ():
	DBsession = sessionmaker(bind=contactor_db_connection)
	session_query = DBsession()
	data = []
	Today = request.form['date']
	contactor_name = request.form['contactor_name']
	if request.method == 'POST':
		results = session_query.query(CONTACTOR_STOCK_FLOW_TABLE).filter(and_(CONTACTOR_STOCK_FLOW_TABLE.ITEM_NAME == contactor_name ,CONTACTOR_STOCK_FLOW_TABLE.DATE == Today))
		for re in results: data.insert(0,(re.UNAME,re.ITEM_NAME,re.QUANTITY,re.DATE)) 
		return allow_cross_origin(json.JSONEncoder().encode(data))


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> FROM TO 
@app.route ('/contactor_stock_flow_from_to_all',methods=['POST','GET'])
def contactor_flow_From_and_To_dates ():
	DBsession = sessionmaker(bind=contactor_db_connection)
	session_query = DBsession()
	if request.method == 'POST':
		From_date = request.form['from']
		To_date = request.form['to']
		print From_date
		print To_date
		sql_cmd = session_query.query(CONTACTOR_STOCK_FLOW_TABLE).filter( CONTACTOR_STOCK_FLOW_TABLE.DATE.between(From_date,To_date))
		paint = session_query.execute(sql_cmd)
		data = []
		for dates in paint: data.append(list(dates))
		return allow_cross_origin(json.JSONEncoder().encode(data))


@app.route ('/contactor_stock_flow_from_to_name',methods=['POST','GET'])
def contactor_flow_From_and_To_name():
	DBsession = sessionmaker(bind=contactor_db_connection)
	session_query = DBsession()
	data = []
	if request.method == 'POST':
		From_date = request.form['from']
		To_date = request.form['to']
		contactor_name = request.form['contactor_name']
		sql_cmd = session_query.query(CONTACTOR_STOCK_FLOW_TABLE).filter( CONTACTOR_STOCK_FLOW_TABLE.DATE.between(From_date,To_date),CONTACTOR_STOCK_FLOW_TABLE.ITEM_NAME == contactor_name)
		paint = session_query.execute(sql_cmd)
		for dates in paint: data.append(list(dates))
		return allow_cross_origin(json.JSONEncoder().encode(data))


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> LAST WEEK
@app.route('/contactor_stock_flow_last_week_all_data',methods=['POST','GET'])
def contactor_flow_last_week_all_data ():
	DBsession = sessionmaker(bind=contactor_db_connection)
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
	sql_cmd = session_query.query(CONTACTOR_STOCK_FLOW_TABLE).filter(CONTACTOR_STOCK_FLOW_TABLE.DATE.in_(week_days))
	week = session_query.execute(sql_cmd)
	for paint in week: data.append(list(paint))
	return allow_cross_origin(json.JSONEncoder().encode(data))

@app.route('/contactor_stock_flow_last_week_name_data',methods=['POST','GET'])
def contactor_flow_last_week_name_data ():
	DBsession = sessionmaker(bind=contactor_db_connection)
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
		contactor_name = request.form['contactor_name']
		sql_cmd = session_query.query(CONTACTOR_STOCK_FLOW_TABLE).filter(CONTACTOR_STOCK_FLOW_TABLE.DATE.in_(week_days),CONTACTOR_STOCK_FLOW_TABLE.ITEM_NAME == contactor_name)
		week = session_query.execute(sql_cmd)
		for paint in week: data.append(list(paint))
		return allow_cross_origin(json.JSONEncoder().encode(data))


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> THIS MONTH
@app.route('/contactor_stock_flow_this_month_all_data', methods=(['POST','GET']))
def send_contactor_stock_flow_this_month_all_data ():
	DBsession = sessionmaker(bind=contactor_db_connection)
	session_query = DBsession()
	data = []
	mth = datetime.datetime.today()
	mth2 = str(mth.month) 
	current_month = '0'+ mth2
	sql_cmd = session_query.query(CONTACTOR_STOCK_FLOW_TABLE).filter(CONTACTOR_STOCK_FLOW_TABLE.MONTH == current_month)
	for re in sql_cmd: data.insert(0,(re.UNAME, re.ITEM_NAME,re. QUANTITY, re.DATE)) 
	return allow_cross_origin(json.JSONEncoder().encode(data))


@app.route('/contactor_stock_flow_this_month_by_name_data', methods=(['POST','GET']))
def contactor_flow_this_month_name_data ():
	DBsession = sessionmaker(bind=contactor_db_connection)
	session_query = DBsession()
	data = []
	mth = datetime.datetime.today()
	mth2 = str(mth.month) 
	current_month = '0'+ mth2
	if request.method == 'POST':
		contactor_name = request.form['contactor_name']
		sql_cmd = session_query.query(CONTACTOR_STOCK_FLOW_TABLE).filter(CONTACTOR_STOCK_FLOW_TABLE.MONTH == current_month,CONTACTOR_STOCK_FLOW_TABLE.ITEM_NAME == contactor_name)
		for re in sql_cmd: data.insert(0,(re.UNAME, re.ITEM_NAME, re. QUANTITY, re.DATE)) 
		return allow_cross_origin(json.JSONEncoder().encode(data))


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ ====>> LAST MONTH
@app.route('/contactor_stock_flow_last_month_all_data', methods=(['POST','GET']))
def send_contactor_stock_flow_last_month_all_data ():
	DBsession = sessionmaker(bind=contactor_db_connection)
	session_query = DBsession()
	data = []
	lst_mth = datetime.datetime.today()
	lst_mth2 = str(lst_mth.month - 1) 
	last_month = '0'+ lst_mth2
	sql_cmd = session_query.query(CONTACTOR_STOCK_FLOW_TABLE).filter(CONTACTOR_STOCK_FLOW_TABLE.MONTH == last_month)
	for re in sql_cmd: data.insert(0,(re.UNAME, re.ITEM_NAME, re. QUANTITY, re.DATE)) 
	return allow_cross_origin(json.JSONEncoder().encode(data))


# stock flow last month name ....
@app.route('/contactor_stock_flow_last_month_name_data', methods=(['POST','GET']))
def contactor_last_month_name_data ():
	DBsession = sessionmaker(bind=contactor_db_connection)
	session_query = DBsession()
	data = []
	lst_mth = datetime.datetime.today()
	lst_mth2 = str(lst_mth.month - 1) 
	last_month = '0'+ lst_mth2
	if request.method == 'POST':
		contactor_name = request.form['contactor_name']
		sql_cmd = session_query.query(CONTACTOR_STOCK_FLOW_TABLE).filter(CONTACTOR_STOCK_FLOW_TABLE.MONTH == last_month,CONTACTOR_STOCK_FLOW_TABLE.ITEM_NAME == contactor_name)
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
@app.route('/contactor_stock_status_all_data', methods=(['POST','GET']))
def contactor_status_all_data ():
	print "============================================================"
	DBsession = sessionmaker(bind=contactor_db_connection)
	session_query = DBsession()
	data = []
	sql_cmd = session_query.query(CONTACTOR_STATUS_TABLE).all()
	for re in sql_cmd: data.insert(0,(re.ITEM_NAME,re.QUANTITY)) 
	return allow_cross_origin(json.JSONEncoder().encode(data))



# stock status name .....
@app.route('/contactor_stock_status_name_data', methods=(['POST','GET']))
def contactor_status_name_data ():
	DBsession = sessionmaker(bind=contactor_db_connection)
	session_query = DBsession()
	data = []
	if request.method == 'POST':
		contactor_name = request.form['contactor_name']
		print contactor_name	
		sql_cmd = session_query.query(CONTACTOR_STATUS_TABLE).filter(CONTACTOR_STATUS_TABLE.ITEM_NAME == contactor_name)
		for re in sql_cmd: data.insert(0,(re.ITEM_NAME,re.QUANTITY)) 
		return allow_cross_origin(json.JSONEncoder().encode(data))





