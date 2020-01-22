


from main_file import *
from datetime import datetime, timedelta
import datetime
keracolor_db_connection = create_engine('sqlite:///data_bases/mapei/keracolor.db')


@app.route('/keracolor_record_new_stock',methods=['POST'])
def keracolor_record_new_stock ():
	DBsession = sessionmaker(bind=keracolor_db_connection)
	session_query = DBsession()
	mth = datetime.datetime.today()
	mth2 = str(mth.month) 
	current_month = '0'+ mth2

	if  request.method == 'POST':
		uname= request.form['uname']
		item_name= request.form['item_name']
		unit= request.form['unit']  
		qty = request.form ['qty']
		Date= request.form['date']

        # UNAME, ITEM_NAME, unit, QUANTITY , DATE,MONTH
		new_stock = Keracolor_New_stock_table (uname,item_name,unit,qty,Date,current_month)
		session_query.add(new_stock)
		session_query.commit() 
		#==========================

		name_to_update = session_query.query(Keracolor_status_table).order_by(Keracolor_status_table.ITEM_NAME)
		keracolor_name_list  = []
		for name in name_to_update: keracolor_name_list.insert (0, name.ITEM_NAME)


		""" INSERTING DATA   """
		if (item_name in keracolor_name_list): # do updating....
			row_2_update = session_query.query(Keracolor_status_table ).filter_by(ITEM_NAME = item_name)

			for quantity in row_2_update: quantity_in_db = quantity.QUANTITY # get quantity value
			new_quantity_value = int(quantity_in_db) + int(qty)
			session_query.query(Keracolor_status_table).filter_by(ITEM_NAME = item_name).update({"QUANTITY":new_quantity_value})			
			session_query.commit()


		elif (item_name not in keracolor_name_list):
			sql = Keracolor_status_table(item_name,qty)
			session_query.add(sql)
			session_query.commit()
	return "New stock added well ....."


@app.route ('/keracolor_record_taken',methods=['POST'])
def keracolor_record_taken ():
	DBsession = sessionmaker(bind=keracolor_db_connection)
	session_query = DBsession()
	mth = datetime.datetime.today()
	mth2 = str(mth.month) 
	current_month = '0'+ mth2 

	if request.method == "POST":
		uname = request.form['uname']
		item_name = request.form['item_name']
		unit= request.form['unit']  
		qty = request.form ['qty']
		Date= request.form['date']

		item_taken = Keracolor_stock_flow_table (uname,item_name,unit,qty,Date,current_month)
		session_query.add(item_taken)
		session_query.commit()

		#==========================
		name_to_update = session_query.query(Keracolor_status_table ).order_by(Keracolor_status_table.ITEM_NAME)
		keracolor_name_list  = []
		for name in name_to_update: keracolor_name_list.insert (0, name.ITEM_NAME)

		""" INSERTING DATA   """
		if (item_name in keracolor_name_list): # do updating....
			row_2_update = session_query.query(Keracolor_status_table ).filter_by(ITEM_NAME = item_name)

			for quantity in row_2_update: quantity_in_db = quantity.QUANTITY # get quantity value
			new_quantity_value = int(quantity_in_db) - int(qty)
			session_query.query(Keracolor_status_table).filter_by(ITEM_NAME = item_name).update({"QUANTITY":new_quantity_value})			
			session_query.commit()
			

		elif (item_name not in keracolor_name_list):
			qty_value = 0 - int(qty)
			sql = Keracolor_status_table(item_name,qty_value)
			session_query.add(sql)
			session_query.commit()

	return "Data recorded well ......."
