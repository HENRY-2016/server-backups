




from main_file import *
from datetime import datetime, timedelta
import datetime
matt_db_connection = create_engine('sqlite:///data_bases/sadolin/matt.db')


@app.route('/matt_record_new_stock',methods=['POST'])
def matt_record_new_stock ():
	DBsession = sessionmaker(bind=matt_db_connection)
	session_query = DBsession()
	mth = datetime.datetime.today()
	mth2 = str(mth.month) 
	current_month = '0'+ mth2

	if  request.method == 'POST':
		uname= request.form['uname']
		paint_name= request.form['paint_name']
		size= request.form['size']  
		invoce_no= request.form['invoce_no']
		qty = request.form ['qty']
		Date= request.form['date']

		one_ltr =  '1 ltr'
		four_ltr = '4 ltrs'
		twenty_ltr = '20 ltrs'

		# uname = 'henry'
		# paint_name = 'White'
		# size= '4 ltrs'  
		# qty = '5'
		# Date= '2019-08-16'
		# current_month = '08'
		# invoce_no = '60056'

		new_stock = Matt_New_stock_table (uname,paint_name,size,invoce_no,qty,Date,current_month)
		session_query.add(new_stock)
		session_query.commit() 
		#==========================
		paint_names_in_db = session_query.query(Matt_status_table).order_by(Matt_status_table.ITEM_NAME)
		paint_names_list  = []
		for paint in paint_names_in_db: paint_names_list.insert (0, paint.ITEM_NAME)


		""" INSERTING DATA   """
		if (paint_name in paint_names_list): # do updating....
			row_2_update = session_query.query(Matt_status_table ).filter_by(ITEM_NAME = paint_name)

			if size == one_ltr:
				for quantity in row_2_update: quantity_in_db = quantity.ONE_LTR # get quantity value
				new_quantity_value = int(quantity_in_db) + int(qty)
				session_query.query(Matt_status_table).filter_by(ITEM_NAME = paint_name).update({"ONE_LTR":new_quantity_value})			
				session_query.commit()

			elif size == four_ltr:
				for quantity in row_2_update: quantity_in_db = quantity.FOUR_LTR # get quantity value
				new_quantity_value = int(quantity_in_db) + int(qty)
				session_query.query(Matt_status_table).filter_by(ITEM_NAME = paint_name).update({"FOUR_LTR":new_quantity_value})			
				session_query.commit()

			elif size == twenty_ltr:
				for quantity in row_2_update: quantity_in_db = quantity.TWENTY_LTR # get quantity value
				new_quantity_value = int(quantity_in_db) + int(qty)
				session_query.query(Matt_status_table).filter_by(ITEM_NAME = paint_name).update({"TWENTY_LTR":new_quantity_value})			
				session_query.commit()

		elif (paint_name not in paint_names_list):

			if (paint_name not in paint_names_list) and (size == one_ltr):
				sql = Matt_status_table(paint_name,0,0,qty)
				session_query.add(sql)
				session_query.commit()

			elif (paint_name not in paint_names_list) and (size == four_ltr):
				sql = Matt_status_table(paint_name,0,qty,0)
				session_query.add(sql)
				session_query.commit()

			elif (paint_name not in paint_names_list) and (size == twenty_ltr):
				sql = Matt_status_table(paint_name,qty,0,0)
				session_query.add(sql)
				session_query.commit()

			elif (paint_name in paint_names_list):
				pass


	return "New stock added well ....."

# UNAME, ITEM_NAME, SIZE, QUANTITY , DATE
@app.route ('/matt_record_used_paint',methods=['POST'])
def matt_record_used_paint ():
	DBsession = sessionmaker(bind=matt_db_connection)
	session_query = DBsession()
	mth = datetime.datetime.today()
	mth2 = str(mth.month) 
	current_month = '0'+ mth2 

	if request.method == "POST":
		uname = request.form['uname']
		paint_name = request.form['paint_name']
		size= request.form['size']  
		qty = request.form ['qty']
		Date= request.form['date']

		one_ltr = '1 ltr'
		four_ltr =  '4 ltrs'
		twenty_ltr = '20 ltrs'

		# uname = 'henry'
		# paint_name = 'White'
		# size= '4 ltrs'  
		# qty = '5'
		# Date= '2019-08-15'
		# current_month = '08'

		recorded_paint = Matt_stock_flow_table (uname,paint_name,size,qty,Date,current_month)
		session_query.add(recorded_paint)
		session_query.commit()

		#==========================
		paint_names_in_db = session_query.query(Matt_status_table ).order_by(Matt_status_table.ITEM_NAME)
		paint_names_list  = []
		for paint in paint_names_in_db: paint_names_list.insert (0, paint.ITEM_NAME)

		""" INSERTING DATA   """
		if (paint_name in paint_names_list): # do updating....
			row_2_update = session_query.query(Matt_status_table ).filter_by(ITEM_NAME = paint_name)

			if size == one_ltr:
				for quantity in row_2_update: quantity_in_db = quantity.ONE_LTR # get quantity value
				new_quantity_value = int(quantity_in_db) - int(qty)
				session_query.query(Matt_status_table).filter_by(ITEM_NAME = paint_name).update({"ONE_LTR":new_quantity_value})			
				session_query.commit()

			elif size == four_ltr:
				for quantity in row_2_update: quantity_in_db = quantity.FOUR_LTR # get quantity value
				new_quantity_value = int(quantity_in_db) - int(qty)
				print new_quantity_value
				session_query.query(Matt_status_table).filter_by(ITEM_NAME = paint_name).update({"FOUR_LTR":new_quantity_value})			
				session_query.commit()

			elif size == twenty_ltr:
				for quantity in row_2_update: quantity_in_db = quantity.TWENTY_LTR # get quantity value
				new_quantity_value = int(quantity_in_db) - int(qty)
				print new_quantity_value
				session_query.query(Matt_status_table).filter_by(ITEM_NAME = paint_name).update({"TWENTY_LTR":new_quantity_value})			
				session_query.commit()

		elif (paint_name not in paint_names_list):

			if (paint_name not in paint_names_list) and (size == one_ltr):
				sql = Matt_status_table(paint_name,0,0,qty)
				session_query.add(sql)
				session_query.commit()

			elif (paint_name not in paint_names_list) and (size == four_ltr):
				sql = Matt_status_table(paint_name,0,qty,0)
				session_query.add(sql)
				session_query.commit()

			elif (paint_name not in paint_names_list) and (size == twenty_ltr):
				sql = Matt_status_table(paint_name,qty,0,0)
				session_query.add(sql)
				session_query.commit()

			elif (paint_name in paint_names_list):
				pass

	return "Data recorded well ......."
