
from main_file import *
from datetime import datetime, timedelta
import datetime
bg_db_connection = create_engine('sqlite:///data_bases/sadolin/budget_gloss.db')


@app.route('/bg_record_new_stock',methods=['POST'])
def bg_record_new_stock ():
	DBsession = sessionmaker(bind=bg_db_connection)
	session_query = DBsession()
	mth = datetime.datetime.today()
	mth2 = str(mth.month) 
	current_month = '0'+ mth2

	if  request.method == 'POST':
		uname= request.form['uname']
		paint_name= request.form['item_name']
		size= request.form['size']  
		invoce_no= request.form['invoce_no']
		qty = request.form ['qty']
		Date= request.form['date']

		half_ltr = '0.5 ltr'
		one_ltr =  '1 ltr'
		four_ltr = '4 ltrs'

		# uname = 'henry'
		# paint_name = 'White'
		# size= '4 ltrs'  
		# qty = '5'
		# Date= '2019-08-16'
		# current_month = '08'
		# invoce_no = '60056'

		bg_new_stock = Budget_glose_New_stock_table (uname,paint_name,size,invoce_no,qty,Date,current_month)
		session_query.add(bg_new_stock)
		session_query.commit() 
		#==========================
		paint_names_in_db = session_query.query(Budget_glose_status_table ).order_by(Budget_glose_status_table.ITEM_NAME)
		paint_names_list  = []
		for paint in paint_names_in_db: paint_names_list.insert (0, paint.ITEM_NAME)


		""" INSERTING DATA   """
		if (paint_name in paint_names_list): # do updating....
			row_2_update = session_query.query(Budget_glose_status_table ).filter_by(ITEM_NAME = paint_name)
			
			if size == half_ltr:
				for quantity in row_2_update: quantity_in_db = quantity.HALF_LTR # get quantity value
				new_quantity_value = int(quantity_in_db) + int(qty)
				session_query.query(Budget_glose_status_table).filter_by(ITEM_NAME = paint_name).update({"HALF_LTR":new_quantity_value})			
				session_query.commit()
			
			elif size == one_ltr:
				for quantity in row_2_update: quantity_in_db = quantity.ONE_LTR # get quantity value
				new_quantity_value = int(quantity_in_db) + int(qty)
				session_query.query(Budget_glose_status_table).filter_by(ITEM_NAME = paint_name).update({"ONE_LTR":new_quantity_value})			
				session_query.commit()
			
			elif size == four_ltr:
				for quantity in row_2_update: quantity_in_db = quantity.FOUR_LTR # get quantity value
				new_quantity_value = int(quantity_in_db) + int(qty)
				session_query.query(Budget_glose_status_table).filter_by(ITEM_NAME = paint_name).update({"FOUR_LTR":new_quantity_value})			
				session_query.commit()

		elif (paint_name not in paint_names_list):
			if (paint_name not in paint_names_list) and (size == half_ltr):
				# ITEM_NAME, FOUR_LTR, ONE_LTR , HALF_LTR
				sql = Budget_glose_status_table(paint_name,0,0,qty)
				session_query.add(sql)
				session_query.commit()
				
			elif (paint_name not in paint_names_list) and (size == one_ltr):
				sql = Budget_glose_status_table(paint_name,0,qty,0)
				session_query.add(sql)
				session_query.commit()

			elif (paint_name not in paint_names_list) and (size == four_ltr):
				sql = Budget_glose_status_table(paint_name,qty,0,0)
				session_query.add(sql)
				session_query.commit()

			elif (paint_name in paint_names_list):
				pass


	return "New stock added well ....."

# UNAME, ITEM_NAME, SIZE, QUANTITY , DATE
@app.route ('/bg_record_used_paint',methods=['POST'])
def bg_record_used_paint ():
	DBsession = sessionmaker(bind=bg_db_connection)
	session_query = DBsession()
	mth = datetime.datetime.today()
	mth2 = str(mth.month) 
	current_month = '0'+ mth2 

	if request.method == "POST":
		uname = request.form['uname']
		paint_name = request.form['item_name']
		size= request.form['size']  
		qty = request.form ['qty']
		Date= request.form['date']

		half_ltr = '0.5 ltr'
		one_ltr =  '1 ltr'
		four_ltr = '4 ltrs'

		# uname = 'henry'
		# paint_name = 'White'
		# size= '4 ltrs'  
		# qty = '5'
		# Date= '2019-08-15'
		# current_month = '08'

		recorded_paint = Budget_glose_stock_flow_table (uname,paint_name,size,qty,Date,current_month)
		session_query.add(recorded_paint)
		session_query.commit()

		#==========================
		paint_names_in_db = session_query.query(Budget_glose_status_table ).order_by(Budget_glose_status_table.ITEM_NAME)
		paint_names_list  = []
		for paint in paint_names_in_db: paint_names_list.insert (0, paint.ITEM_NAME)

		""" INSERTING DATA   """
		if (paint_name in paint_names_list): # do updating....
			row_2_update = session_query.query(Budget_glose_status_table ).filter_by(ITEM_NAME = paint_name)
			
			if size == half_ltr:
				for quantity in row_2_update: quantity_in_db = quantity.HALF_LTR # get quantity value
				new_quantity_value = int(quantity_in_db) - int(qty)
				session_query.query(Budget_glose_status_table).filter_by(ITEM_NAME = paint_name).update({"HALF_LTR":new_quantity_value})			
				session_query.commit()
			
			elif size == one_ltr:
				for quantity in row_2_update: quantity_in_db = quantity.ONE_LTR # get quantity value
				new_quantity_value = int(quantity_in_db) - int(qty)
				session_query.query(Budget_glose_status_table).filter_by(ITEM_NAME = paint_name).update({"ONE_LTR":new_quantity_value})			
				session_query.commit()
			
			elif size == four_ltr:
				for quantity in row_2_update: quantity_in_db = quantity.FOUR_LTR # get quantity value
				print quantity_in_db
				if not quantity_in_db:
					print "is empty....."
					quantity_in_db = 0
					new_quantity_value = int(quantity_in_db) - int(qty)
					print new_quantity_value
					session_query.query(Budget_glose_status_table).filter_by(ITEM_NAME = paint_name).update({"FOUR_LTR":new_quantity_value})			
					session_query.commit()

				if quantity_in_db: 
					print "is not empty......"
					new_quantity_value = int(quantity_in_db) - int(qty)
					print new_quantity_value
					session_query.query(Budget_glose_status_table).filter_by(ITEM_NAME = paint_name).update({"FOUR_LTR":new_quantity_value})			
					session_query.commit()

		elif (paint_name not in paint_names_list):
			if (paint_name not in paint_names_list) and (size == half_ltr):
				# ITEM_NAME, FOUR_LTR, ONE_LTR , HALF_LTR
				sql = Budget_glose_status_table(paint_name,0,0,qty)
				session_query.add(sql)
				session_query.commit()
				
			elif (paint_name not in paint_names_list) and (size == one_ltr):
				sql = Budget_glose_status_table(paint_name,0,qty,0)
				session_query.add(sql)
				session_query.commit()

			elif (paint_name not in paint_names_list) and (size == four_ltr):
				sql = Budget_glose_status_table(paint_name,qty,0,0)
				session_query.add(sql)
				session_query.commit()

			elif (paint_name in paint_names_list):
				pass

	return "Data recorded well ......."
