


from main_file import *
from datetime import datetime, timedelta
import datetime
base_super_db_connection = create_engine('sqlite:///data_bases/sadolin/base_super.db')


@app.route('/base_super_record_new_stock',methods=['POST'])
def base_super_record_new_stock ():
	DBsession = sessionmaker(bind=base_super_db_connection)
	session_query = DBsession()
	mth = datetime.datetime.today()
	mth2 = str(mth.month) 
	current_month = '0'+ mth2

	if  request.method == 'POST':
		uname= request.form['uname']
		base_name= request.form['base_name']
		size= request.form['size']  
		invoce_no= request.form['invoce_no']
		qty = request.form ['qty']
		Date= request.form['date']

		one_ltr =  '1 ltr'
		four_ltr = '4 ltrs'

		# uname = 'henry'
		# base_name = 'White'
		# size= '4 ltrs'  
		# qty = '5'
		# Date= '2019-08-16'
		# current_month = '08'
		# invoce_no = '60056'

		new_stock = Base_super_New_stock_table (uname,base_name,size,invoce_no,qty,Date,current_month)
		session_query.add(new_stock)
		session_query.commit() 
		#==========================
		base_names_in_db = session_query.query(Base_super_status_table).order_by(Base_super_status_table.ITEM_NAME)
		base_names_list  = []
		for paint in base_names_in_db: base_names_list.insert (0, paint.ITEM_NAME)


		""" INSERTING DATA   """
		if (base_name in base_names_list): # do updating....
			row_2_update = session_query.query(Base_super_status_table ).filter_by(ITEM_NAME = base_name)

			if size == one_ltr:
				for quantity in row_2_update: quantity_in_db = quantity.ONE_LTR # get quantity value
				new_quantity_value = int(quantity_in_db) + int(qty)
				session_query.query(Base_super_status_table).filter_by(ITEM_NAME = base_name).update({"ONE_LTR":new_quantity_value})			
				session_query.commit()

			elif size == four_ltr:
				for quantity in row_2_update: quantity_in_db = quantity.FOUR_LTR # get quantity value
				new_quantity_value = int(quantity_in_db) + int(qty)
				session_query.query(Base_super_status_table).filter_by(ITEM_NAME = base_name).update({"FOUR_LTR":new_quantity_value})			
				session_query.commit()

		elif (base_name not in base_names_list):

			if (base_name not in base_names_list) and (size == one_ltr):
				sql = Base_super_status_table(base_name,0,qty)
				session_query.add(sql)
				session_query.commit()

			elif (base_name not in base_names_list) and (size == four_ltr):
				sql = Base_super_status_table(base_name,qty,0)
				session_query.add(sql)
				session_query.commit()

			elif (base_name in base_names_list):
				pass


	return "New stock added well ....."

# UNAME, ITEM_NAME, SIZE, QUANTITY , DATE
@app.route ('/base_super_record_used_paint',methods=['POST'])
def base_super_record_used_paint ():
	DBsession = sessionmaker(bind=base_super_db_connection)
	session_query = DBsession()
	mth = datetime.datetime.today()
	mth2 = str(mth.month) 
	current_month = '0'+ mth2 

	if request.method == "POST":
		uname = request.form['uname']
		base_name = request.form['base_name']
		size= request.form['size']  
		qty = request.form ['qty']
		Date= request.form['date']

		one_ltr = '1 ltr'
		four_ltr =  '4 ltrs'

		# uname = 'henry'
		# base_name = 'White'
		# size= '4 ltrs'  
		# qty = '5'
		# Date= '2019-08-15'
		# current_month = '08'

		recorded_paint = Base_super_stock_flow_table (uname,base_name,size,qty,Date,current_month)
		session_query.add(recorded_paint)
		session_query.commit()

		#==========================
		base_names_in_db = session_query.query(Base_super_status_table ).order_by(Base_super_status_table.ITEM_NAME)
		base_names_list  = []
		for paint in base_names_in_db: base_names_list.insert (0, paint.ITEM_NAME)

		""" INSERTING DATA   """
		if (base_name in base_names_list): # do updating....
			row_2_update = session_query.query(Base_super_status_table ).filter_by(ITEM_NAME = base_name)

			if size == one_ltr:
				for quantity in row_2_update: quantity_in_db = quantity.ONE_LTR # get quantity value
				new_quantity_value = int(quantity_in_db) - int(qty)
				session_query.query(Base_super_status_table).filter_by(ITEM_NAME = base_name).update({"ONE_LTR":new_quantity_value})			
				session_query.commit()

			elif size == four_ltr:
				for quantity in row_2_update: quantity_in_db = quantity.FOUR_LTR # get quantity value
				new_quantity_value = int(quantity_in_db) - int(qty)
				print new_quantity_value
				session_query.query(Base_super_status_table).filter_by(ITEM_NAME = base_name).update({"FOUR_LTR":new_quantity_value})			
				session_query.commit()

		elif (base_name not in base_names_list):

			if (base_name not in base_names_list) and (size == one_ltr):
				sql = Base_super_status_table(base_name,0,qty)
				session_query.add(sql)
				session_query.commit()

			elif (base_name not in base_names_list) and (size == four_ltr):
				sql = Base_super_status_table(base_name,qty,0)
				session_query.add(sql)
				session_query.commit()

			elif (base_name in base_names_list):
				pass

	return "Data recorded well ......."
