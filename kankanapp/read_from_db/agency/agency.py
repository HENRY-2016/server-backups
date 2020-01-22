
from main_file import *
from datetime import date, timedelta
import datetime

agency_db_connection = create_engine('sqlite:///data_bases/agency/agency.db') #create_engine('sqlite:////data_bases/agency/agency.db')


def listToString (s):
	str1 = " "
	return (str1.join(s))

@app.route('/agency_prev_float', methods=['POST','GET'])
def  send_show_agency_prev_float ():
	DBsession = sessionmaker(bind=agency_db_connection)
	session_query = DBsession()
	data = []
	today = datetime.date.today ()
	yesterday = today - datetime.timedelta(days = 1)
	sql_cmd = session_query.query(Agency_New_day).filter(Agency_New_day.DATE == yesterday)
	for results in sql_cmd: data.insert(0,(results.FLOAT)) 
	# remove_u = [str(i) for i in data]
	# print remove_u 
	converted_figure = listToString (data)
	return allow_cross_origin(converted_figure)



# show all details
@app.route('/query_agency_show_all_report', methods=['POST','GET'])
def  send_show_all_report ():
	DBsession = sessionmaker(bind=agency_db_connection)
	session_query = DBsession()
	data = []
	sql_cmd = session_query.query(Agency_New_day).all ()

	for results in sql_cmd: data.insert(0,(results.UNAME,results.DATE,results.AIRTEL,results.MTN,results.CENTENARY,results.DFCU,results.DTB,results.EQUITY,results.STANBIC,results.BARCLAYS,results.CASH,results.DRAWINGS,results.FLOAT)) 
	return allow_cross_origin(json.JSONEncoder().encode(data))

# By date
@app.route ('/agency_view_by_date_details',methods=['POST','GET'])
def send_agency_view_by_date_details ():
	DBsession = sessionmaker(bind=agency_db_connection)
	session_query = DBsession()
	if request.method == 'POST':
		data = []
		input_date = request.form['date']
		sql_cmd = session_query.query(Agency_New_day).filter(Agency_New_day.DATE == input_date)
		for results in sql_cmd: data.insert(0,(results.UNAME,results.DATE,results.AIRTEL,results.MTN,results.CENTENARY,results.DFCU,results.DTB,results.EQUITY,results.STANBIC,results.BARCLAYS,results.CASH,results.DRAWINGS,results.FLOAT)) 
		return allow_cross_origin(json.JSONEncoder().encode(data))

@app.route ('/agency_query_From_and_To_dates',methods=['POST','GET'])
def send_From_and_To_dates ():
	DBsession = sessionmaker(bind=agency_db_connection)
	session_query = DBsession()

	if request.method == 'POST':
		From_date = request.form['From_date']
		To_date = request.form['To_date']
		sql_cmd = session_query.query(Agency_New_day).filter(Agency_New_day.DATE.between(From_date,To_date))
		data = []
		for results in sql_cmd: data.insert(0,(results.UNAME,results.DATE,results.AIRTEL,results.MTN,results.CENTENARY,results.DFCU,results.DTB,results.EQUITY,results.STANBIC,results.BARCLAYS,results.CASH,results.DRAWINGS,results.FLOAT)) 
		return allow_cross_origin(json.JSONEncoder().encode(data))


# yestardays report
@app.route('/agency_query_yestardays_report', methods=['POST','GET'])
def send_agency_yestardays_report ():
	DBsession = sessionmaker(bind=agency_db_connection)
	session_query = DBsession()
	yesterday = datetime.date.today() - datetime.timedelta(days=1)
	sql_cmd = session_query.query(Agency_New_day).filter(Agency_New_day.DATE == yesterday)
	data = []
	for results in sql_cmd: data.insert(0,(results.UNAME,results.DATE,results.AIRTEL,results.MTN,results.CENTENARY,results.DFCU,results.DTB,results.EQUITY,results.STANBIC,results.BARCLAYS,results.CASH,results.DRAWINGS,results.FLOAT)) 
	return allow_cross_origin(json.JSONEncoder().encode(data))

# week report
@app.route('/query_agency_week_report', methods=['POST','GET'])
def send_agency_week_report ():
	DBsession = sessionmaker(bind=agency_db_connection)
	session_query = DBsession()
	data = []

	day_1 = datetime.date.today() - datetime.timedelta(days=0)
	day_2 = datetime.date.today() - datetime.timedelta(days=1)
	day_3 = datetime.date.today() - datetime.timedelta(days=2)
	day_4 = datetime.date.today() - datetime.timedelta(days=3)
	day_5 = datetime.date.today() - datetime.timedelta(days=4)
	day_6 = datetime.date.today() - datetime.timedelta(days=5)
	day_7 = datetime.date.today() - datetime.timedelta(days=6)

	week_days =(day_1,day_2,day_3,day_4,day_5,day_6,day_7)
	sql_cmd = session_query.query(Agency_New_day).filter(Agency_New_day.DATE.in_(week_days))
	for results in sql_cmd: data.insert(0,(results.UNAME,results.DATE,results.AIRTEL,results.MTN,results.CENTENARY,results.DFCU,results.DTB,results.EQUITY,results.STANBIC,results.BARCLAYS,results.CASH,results.DRAWINGS,results.FLOAT)) 
	return allow_cross_origin(json.JSONEncoder().encode(data))



# This month
@app.route('/query_agency_this_month_report', methods=['POST','GET'])
def send_all_agency_this_month_report ():
	DBsession = sessionmaker(bind=agency_db_connection)
	session_query = DBsession()
	data = []

	d = datetime.datetime.today()
	current_month = d.month 
	sql_cmd = session_query.query(Agency_New_day).filter(Agency_New_day.MONTH == current_month)

	for results in sql_cmd: data.insert(0,(results.UNAME,results.DATE,results.AIRTEL,results.MTN,results.CENTENARY,results.DFCU,results.DTB,results.EQUITY,results.STANBIC,results.BARCLAYS,results.CASH,results.DRAWINGS,results.FLOAT)) 
	return allow_cross_origin(json.JSONEncoder().encode(data))



# Last month
@app.route('/query_agency_last_month_report', methods=['POST','GET'])
def send_all_agency_last_month_report ():
	DBsession = sessionmaker(bind=agency_db_connection)
	session_query = DBsession()
	data = []
	d = datetime.datetime.today()
	current_month = d.month
	last_month = current_month - 1

	sql_cmd = session_query.query(Agency_New_day).filter(Agency_New_day.MONTH == last_month)
	for results in sql_cmd: data.insert(0,(results.UNAME,results.DATE,results.AIRTEL,results.MTN,results.CENTENARY,results.DFCU,results.DTB,results.EQUITY,results.STANBIC,results.BARCLAYS,results.CASH,results.DRAWINGS,results.FLOAT)) 
	return allow_cross_origin(json.JSONEncoder().encode(data))


"""
			=============================== SUMMARY ==========================
"""
@app.route('/query_agency_summary_show_all_report', methods=['POST','GET'])
def send_agency_summary_show_all_report ():
	DBsession = sessionmaker(bind=agency_db_connection)
	session_query = DBsession()

	my_query = session_query.query(Agency_New_day).all()

	data = []
	for results in my_query: data.insert(0,(results.UNAME,results.DATE,results.BANKS, results.CASH,results.DRAWINGS,results.FLOAT))
	return allow_cross_origin(json.JSONEncoder().encode(data))

@app.route ('/agency_view_by_date_summary',methods=['POST','GET'])
def send_agency_view_by_date_summary ():
	DBsession = sessionmaker(bind=agency_db_connection)
	session_query = DBsession()
	if request.method == 'POST':
		summary_date = request.form['summary_date']
		sql_cmd =  session_query.query(Agency_New_day).filter(Agency_New_day.DATE == summary_date)
		data = []
		for results in sql_cmd:data.insert(0,(results.UNAME,results.DATE,results.BANKS,results.CASH,results.DRAWINGS,results.FLOAT))
		return allow_cross_origin(json.JSONEncoder().encode(data))


@app.route ('/agency_query_From_To_date_summary',methods=['POST','GET'])
def send_From_and_To_date_summary ():
	DBsession = sessionmaker(bind=agency_db_connection)
	session_query = DBsession()

	if request.method == 'POST':
		From_date = request.form['From_date']
		To_date = request.form['To_date']

		sql_cmd = session_query.query(Agency_New_day).filter(Agency_New_day.DATE.between(From_date,To_date))

		data = []
		for results in sql_cmd:
			data.insert(0,(results.UNAME,results.DATE,results.BANKS,results.CASH,results.DRAWINGS,results.FLOAT))
		return allow_cross_origin(json.JSONEncoder().encode(data))

@app.route('/agency_query_yestardays_summary_report', methods=['POST','GET'])
def send_agency_yestardays_summary_report ():
	DBsession = sessionmaker(bind=agency_db_connection)
	session_query = DBsession()
	data = []
	yesterday = datetime.date.today() - datetime.timedelta(days=1)
	sql_cmd = session_query.query(Agency_New_day).filter(Agency_New_day.DATE == yesterday)
	for results in sql_cmd:data.insert(0,(results.UNAME,results.DATE,results.BANKS,results.CASH,results.DRAWINGS,results.FLOAT))
	return allow_cross_origin(json.JSONEncoder().encode(data))

# last week
@app.route('/query_agency_week_summary_report', methods=['POST','GET'])
def send_agency_summary_week_report ():
	DBsession = sessionmaker(bind=agency_db_connection)
	session_query = DBsession()
	data = []

	day_1 = datetime.date.today() - datetime.timedelta(days=0)
	day_2 = datetime.date.today() - datetime.timedelta(days=1)
	day_3 = datetime.date.today() - datetime.timedelta(days=2)
	day_4 = datetime.date.today() - datetime.timedelta(days=3)
	day_5 = datetime.date.today() - datetime.timedelta(days=4)
	day_6 = datetime.date.today() - datetime.timedelta(days=5)
	day_7 = datetime.date.today() - datetime.timedelta(days=6)

	week_days =(day_1,day_2,day_3,day_4,day_5,day_6,day_7)
	sql_cmd = session_query.query(Agency_New_day).filter(Agency_New_day.DATE.in_(week_days))

	for results in sql_cmd:data.insert(0,(results.UNAME,results.DATE,results.BANKS,results.CASH,results.DRAWINGS,results.FLOAT))
	return allow_cross_origin(json.JSONEncoder().encode(data))


# This month
@app.route('/query_agency_this_month_summary_report', methods=['POST','GET'])
def send_all_agency_this_month_summary_report ():
	DBsession = sessionmaker(bind=agency_db_connection)
	session_query = DBsession()
	data = []
	d = datetime.datetime.today()
	current_month = d.month 

	sql_cmd = session_query.query(Agency_New_day).filter(Agency_New_day.MONTH == current_month)
	for results in sql_cmd:data.insert(0,(results.UNAME,results.DATE,results.BANKS,results.CASH,results.DRAWINGS,results.FLOAT))
	return allow_cross_origin(json.JSONEncoder().encode(data))

# Last month
@app.route('/query_agency_last_month_summary_report', methods=['POST','GET'])
def send_all_agency_last_month_summary_report ():
	DBsession = sessionmaker(bind=agency_db_connection)
	session_query = DBsession()
	data = []
	d = datetime.datetime.today()
	current_month = d.month
	last_month = current_month - 1

	# sql_cmd = session_query.query(Agency_New_day).filter(Agency_New_day.MONTH == last_month)
	sql_cmd = session_query.query(Agency_New_day).all()
	for results in sql_cmd:data.insert(0,(results.UNAME,results.DATE,results.BANKS,results.CASH,results.DRAWINGS,results.FLOAT))
	return allow_cross_origin(json.JSONEncoder().encode(data))
