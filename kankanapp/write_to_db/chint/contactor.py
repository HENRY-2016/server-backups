

from main_file import *
from datetime import datetime, timedelta
import datetime

contactor_db_connection = create_engine('sqlite:///data_bases/chint/contactor.db')

@app.route('/contactor_record_new_stock',methods=['POST'])
def contactor_record_new_stock ():
	DBsession = sessionmaker(bind=contactor_db_connection)
	session_query = DBsession()
	mth = datetime.datetime.today()
	mth2 = str(mth.month) 
	current_month = '0'+ mth2

	if  request.method == 'POST':
		uname= request.form['uname']
		item_name= request.form['item_name']
		qty = request.form ['qty']
		Date= request.form['date']

		new_stock = CONTACTOR_NEW_STOCK_TABLE (uname,item_name,qty,Date,current_month)
		session_query.add(new_stock)
		session_query.commit() 
		#==========================

		name_to_update = session_query.query(CONTACTOR_STATUS_TABLE).order_by(CONTACTOR_STATUS_TABLE.ITEM_NAME)
		contactor_name_list  = []
		for name in name_to_update: contactor_name_list.insert (0, name.ITEM_NAME)


		""" INSERTING DATA   """
		if (item_name in contactor_name_list): # do updating....
			row_2_update = session_query.query(CONTACTOR_STATUS_TABLE ).filter_by(ITEM_NAME = item_name)

			for quantity in row_2_update: quantity_in_db = quantity.QUANTITY # get quantity value
			new_quantity_value = int(quantity_in_db) + int(qty)
			session_query.query(CONTACTOR_STATUS_TABLE).filter_by(ITEM_NAME = item_name).update({"QUANTITY":new_quantity_value})			
			session_query.commit()


		elif (item_name not in contactor_name_list):
			sql = CONTACTOR_STATUS_TABLE(item_name,qty)
			session_query.add(sql)
			session_query.commit()
	return " <center>CONTACTOR ::: <br><br>New stock added well .....</center>"


@app.route ('/record_contactor_taken_stock',methods=['POST'])
def contactor_record_taken ():
	DBsession = sessionmaker(bind=contactor_db_connection)
	session_query = DBsession()
	mth = datetime.datetime.today()
	mth2 = str(mth.month) 
	current_month = '0'+ mth2 

	if request.method == "POST":
		uname = request.form['uname']
		item_name = request.form['item_name']
		qty = request.form ['qty']
		Date= request.form['date']

		item_taken = CONTACTOR_STOCK_FLOW_TABLE (uname,item_name,qty,Date,current_month)
		session_query.add(item_taken)
		session_query.commit()

		#==========================
		name_to_update = session_query.query(CONTACTOR_STATUS_TABLE ).order_by(CONTACTOR_STATUS_TABLE.ITEM_NAME)
		contactor_name_list  = []
		for name in name_to_update: contactor_name_list.insert (0, name.ITEM_NAME)

		""" INSERTING DATA   """
		if (item_name in contactor_name_list): # do updating....
			row_2_update = session_query.query(CONTACTOR_STATUS_TABLE ).filter_by(ITEM_NAME = item_name)

			for quantity in row_2_update: quantity_in_db = quantity.QUANTITY # get quantity value
			new_quantity_value = int(quantity_in_db) - int(qty)
			session_query.query(CONTACTOR_STATUS_TABLE).filter_by(ITEM_NAME = item_name).update({"QUANTITY":new_quantity_value})			
			session_query.commit()
			

		elif (item_name not in contactor_name_list):
			qty_value = 0 - int(qty)
			sql = CONTACTOR_STATUS_TABLE(item_name,qty_value)
			session_query.add(sql)
			session_query.commit()

	return " <center>CONTACTOR :::<br><br> Data recorded well .......</center>"
#====================================================================================
