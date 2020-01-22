
from main_file import *
from datetime import datetime, timedelta
import datetime
plastimul_dpm_db_connection = create_engine('sqlite:///data_bases/mapei/adesilexP7.db')

@app.route('/adesilexP7_record_new_stock',methods=['POST'])
def adesilexp7_record_new_stock ():
	DBsession = sessionmaker(bind=plastimul_dpm_db_connection)
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
		new_stock = Planiseal_grey_New_stock_table (uname,item_name,unit,qty,Date,current_month)
		session_query.add(new_stock)
		session_query.commit() 
		#==========================

		name_to_update = session_query.query(AdesilexP7_status_table).order_by(AdesilexP7_status_table.ITEM_NAME)
		plastimul_dpm_name_list  = []
		for name in name_to_update: plastimul_dpm_name_list.insert (0, name.ITEM_NAME)


		""" INSERTING DATA   """
		if (item_name in plastimul_dpm_name_list): # do updating....
			row_2_update = session_query.query(AdesilexP7_status_table ).filter_by(ITEM_NAME = item_name)

			for quantity in row_2_update: quantity_in_db = quantity.QUANTITY # get quantity value
			new_quantity_value = int(quantity_in_db) + int(qty)
			session_query.query(AdesilexP7_status_table).filter_by(ITEM_NAME = item_name).update({"QUANTITY":new_quantity_value})			
			session_query.commit()


		elif (item_name not in plastimul_dpm_name_list):
			sql = AdesilexP7_status_table(item_name,qty)
			session_query.add(sql)
			session_query.commit()
	return "New stock added well ....."


@app.route ('/adesilexP7_record_taken',methods=['POST'])
def adesilexp7_record_taken ():
	DBsession = sessionmaker(bind=plastimul_dpm_db_connection)
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

		item_taken = AdesilexP7_stock_flow_table (uname,item_name,unit,qty,Date,current_month)
		session_query.add(item_taken)
		session_query.commit()

		#==========================
		name_to_update = session_query.query(AdesilexP7_status_table ).order_by(AdesilexP7_status_table.ITEM_NAME)
		plastimul_dpm_name_list  = []
		for name in name_to_update: plastimul_dpm_name_list.insert (0, name.ITEM_NAME)

		""" INSERTING DATA   """
		if (item_name in plastimul_dpm_name_list): # do updating....
			row_2_update = session_query.query(AdesilexP7_status_table ).filter_by(ITEM_NAME = item_name)

			for quantity in row_2_update: quantity_in_db = quantity.QUANTITY # get quantity value
			new_quantity_value = int(quantity_in_db) - int(qty)
			session_query.query(AdesilexP7_status_table).filter_by(ITEM_NAME = item_name).update({"QUANTITY":new_quantity_value})			
			session_query.commit()
			

		elif (item_name not in plastimul_dpm_name_list):
			qty_value = 0 - int(qty)
			sql = AdesilexP7_status_table(item_name,qty_value)
			session_query.add(sql)
			session_query.commit()

	return "Data recorded well ......."

