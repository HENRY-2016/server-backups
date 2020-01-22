

from main_file import *
from datetime import datetime, timedelta
import datetime

silver_db_connection = create_engine('sqlite:///data_bases/chint/silver.db')

@app.route('/silver_switch_record_new_stock',methods=['POST'])
def silver_switch_record_new_stock ():
	DBsession = sessionmaker(bind=silver_db_connection)
	session_query = DBsession()
	mth = datetime.datetime.today()
	mth2 = str(mth.month) 
	current_month = '0'+ mth2

	if  request.method == 'POST':
		uname= request.form['uname']
		item_name= request.form['item_name']
		qty = request.form ['qty']
		Date= request.form['date']

		new_stock = SILVER_SWITCH_NEW_STOCK_TABLE (uname,item_name,qty,Date,current_month)
		session_query.add(new_stock)
		session_query.commit() 
		#==========================

		name_to_update = session_query.query(SILVER_SWITCH_STATUS_TABLE).order_by(SILVER_SWITCH_STATUS_TABLE.ITEM_NAME)
		silver  = []
		for name in name_to_update: silver.insert (0, name.ITEM_NAME)


		""" INSERTING DATA   """
		if (item_name in silver): # do updating....
			row_2_update = session_query.query(SILVER_SWITCH_STATUS_TABLE ).filter_by(ITEM_NAME = item_name)

			for quantity in row_2_update: quantity_in_db = quantity.QUANTITY # get quantity value
			new_quantity_value = int(quantity_in_db) + int(qty)
			session_query.query(SILVER_SWITCH_STATUS_TABLE).filter_by(ITEM_NAME = item_name).update({"QUANTITY":new_quantity_value})			
			session_query.commit()


		elif (item_name not in silver):
			sql = SILVER_SWITCH_STATUS_TABLE(item_name,qty)
			session_query.add(sql)
			session_query.commit()
	return " <center>SILVER SWITCH ::: <br><br>New stock added well .....</center>"


@app.route ('/record_silver_switch_taken_stock',methods=['POST'])
def silver_switch_record_taken ():
	DBsession = sessionmaker(bind=silver_db_connection)
	session_query = DBsession()
	mth = datetime.datetime.today()
	mth2 = str(mth.month) 
	current_month = '0'+ mth2 

	if request.method == "POST":
		uname = request.form['uname']
		item_name = request.form['item_name']
		qty = request.form ['qty']
		Date= request.form['date']

		item_taken = SILVER_SWITCH_STOCK_FLOW_TABLE (uname,item_name,qty,Date,current_month)
		session_query.add(item_taken)
		session_query.commit()

		#==========================
		name_to_update = session_query.query(SILVER_SWITCH_STATUS_TABLE ).order_by(SILVER_SWITCH_STATUS_TABLE.ITEM_NAME)
		silver  = []
		for name in name_to_update: silver.insert (0, name.ITEM_NAME)

		""" INSERTING DATA   """
		if (item_name in silver): # do updating....
			row_2_update = session_query.query(SILVER_SWITCH_STATUS_TABLE ).filter_by(ITEM_NAME = item_name)

			for quantity in row_2_update: quantity_in_db = quantity.QUANTITY # get quantity value
			new_quantity_value = int(quantity_in_db) - int(qty)
			session_query.query(SILVER_SWITCH_STATUS_TABLE).filter_by(ITEM_NAME = item_name).update({"QUANTITY":new_quantity_value})			
			session_query.commit()
			

		elif (item_name not in silver):
			qty_value = 0 - int(qty)
			sql = SILVER_SWITCH_STATUS_TABLE(item_name,qty_value)
			session_query.add(sql)
			session_query.commit()

	return " <center>SILVER SWITCH :::<br><br> Data recorded well .......</center>"
#====================================================================================
#====================================================================================
#====================================================================================
#====================================================================================

@app.route('/silver_socket_record_new_stock',methods=['POST'])
def silver_socket_record_new_stock ():
	DBsession = sessionmaker(bind=silver_db_connection)
	session_query = DBsession()
	mth = datetime.datetime.today()
	mth2 = str(mth.month) 
	current_month = '0'+ mth2

	if  request.method == 'POST':
		uname= request.form['uname']
		item_name= request.form['item_name']
		qty = request.form ['qty']
		Date= request.form['date']

		new_stock = SILVER_SOCKET_NEW_STOCK_TABLE (uname,item_name,qty,Date,current_month)
		session_query.add(new_stock)
		session_query.commit() 
		#==========================

		name_to_update = session_query.query(SILVER_SOCKET_STATUS_TABLE).order_by(SILVER_SOCKET_STATUS_TABLE.ITEM_NAME)
		silver  = []
		for name in name_to_update: silver.insert (0, name.ITEM_NAME)


		""" INSERTING DATA   """
		if (item_name in silver): # do updating....
			row_2_update = session_query.query(SILVER_SOCKET_STATUS_TABLE ).filter_by(ITEM_NAME = item_name)

			for quantity in row_2_update: quantity_in_db = quantity.QUANTITY # get quantity value
			new_quantity_value = int(quantity_in_db) + int(qty)
			session_query.query(SILVER_SOCKET_STATUS_TABLE).filter_by(ITEM_NAME = item_name).update({"QUANTITY":new_quantity_value})			
			session_query.commit()


		elif (item_name not in silver):
			sql = SILVER_SOCKET_STATUS_TABLE(item_name,qty)
			session_query.add(sql)
			session_query.commit()
	return " <center>SILVER SOCKET ::: <br><br>New stock added well .....</center>"


@app.route ('/record_silver_socket_taken_stock',methods=['POST'])
def silver_socket_record_taken ():
	DBsession = sessionmaker(bind=silver_db_connection)
	session_query = DBsession()
	mth = datetime.datetime.today()
	mth2 = str(mth.month) 
	current_month = '0'+ mth2 

	if request.method == "POST":
		uname = request.form['uname']
		item_name = request.form['item_name']
		qty = request.form ['qty']
		Date= request.form['date']

		item_taken = SILVER_SOCKET_STOCK_FLOW_TABLE (uname,item_name,qty,Date,current_month)
		session_query.add(item_taken)
		session_query.commit()

		#==========================
		name_to_update = session_query.query(SILVER_SOCKET_STATUS_TABLE ).order_by(SILVER_SOCKET_STATUS_TABLE.ITEM_NAME)
		silver  = []
		for name in name_to_update: silver.insert (0, name.ITEM_NAME)

		""" INSERTING DATA   """
		if (item_name in silver): # do updating....
			row_2_update = session_query.query(SILVER_SOCKET_STATUS_TABLE ).filter_by(ITEM_NAME = item_name)

			for quantity in row_2_update: quantity_in_db = quantity.QUANTITY # get quantity value
			new_quantity_value = int(quantity_in_db) - int(qty)
			session_query.query(SILVER_SOCKET_STATUS_TABLE).filter_by(ITEM_NAME = item_name).update({"QUANTITY":new_quantity_value})			
			session_query.commit()
			

		elif (item_name not in silver):
			qty_value = 0 - int(qty)
			sql = SILVER_SOCKET_STATUS_TABLE(item_name,qty_value)
			session_query.add(sql)
			session_query.commit()

	return " <center>SILVER SOCKET :::<br><br> Data recorded well .......</center>"
#====================================================================================
#====================================================================================
#====================================================================================
#====================================================================================
