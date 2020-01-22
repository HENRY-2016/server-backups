



from main_file import *
from datetime import datetime, timedelta
import datetime
thinner_db_connection = create_engine('sqlite:///data_bases/sadolin/thinner.db')

@app.route('/thinner_record_new_stock',methods=['POST'])
def thinner_record_new_stock ():
    DBsession = sessionmaker(bind=thinner_db_connection)
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

        five_ltr = '5 ltrs'
        one_ltr =  '1 ltr'

        print uname

        # uname = 'henry'
        # paint_name = 'White'
        # size= '4 ltrs'  
        # qty = '5'
        # Date= '2019-08-16'
        # current_month = '08'
        # invoce_no = '60056'

        new_stock = Thinner_new_stock (uname,paint_name,size,invoce_no,qty,Date,current_month)
        session_query.add(new_stock)
        session_query.commit() 
        #==========================
        paint_names_in_db = session_query.query(Thinner_stock_status ).order_by(Thinner_stock_status.ITEM_NAME)
        paint_names_list  = []
        for paint in paint_names_in_db: paint_names_list.insert (0, paint.ITEM_NAME)


        """ INSERTING DATA   """
        if (paint_name in paint_names_list): # do updating....
            row_2_update = session_query.query(Thinner_stock_status ).filter_by(ITEM_NAME = paint_name)

            if size == five_ltr:
                for quantity in row_2_update: quantity_in_db = quantity.FIVE_LTR # get quantity value
                new_quantity_value = int(quantity_in_db) + int(qty)
                session_query.query(Thinner_stock_status).filter_by(ITEM_NAME = paint_name).update({"FIVE_LTR":new_quantity_value})			
                session_query.commit()

            elif size == one_ltr:
                for quantity in row_2_update: quantity_in_db = quantity.ONE_LTR # get quantity value
                new_quantity_value = int(quantity_in_db) + int(qty)
                session_query.query(Thinner_stock_status).filter_by(ITEM_NAME = paint_name).update({"ONE_LTR":new_quantity_value})			
                session_query.commit()

        elif (paint_name not in paint_names_list):
            if (paint_name not in paint_names_list) and (size == five_ltr):
                sql = Thinner_stock_status(paint_name,qty,0)
                session_query.add(sql)
                session_query.commit()
            elif (paint_name not in paint_names_list) and (size == one_ltr):
                sql = Thinner_stock_status(paint_name,0,qty)
                session_query.add(sql)
                session_query.commit()

            elif (paint_name in paint_names_list):
                pass


	return "New stock added well ....."

# UNAME, ITEM_NAME, SIZE, QUANTITY , DATE
@app.route ('/thinner_record_used_paint',methods=['POST'])
def thinner_record_used_paint ():
    DBsession = sessionmaker(bind=thinner_db_connection)
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

        
        five_ltr = '5 ltrs'
        one_ltr =  '1 ltr'

        # uname = 'henry'
        # paint_name = 'White'
        # size= '4 ltrs'  
        # qty = '5'
        # Date= '2019-08-10'
        # current_month = '08'

        recorded_paint = Thinner_stock_flow (uname,paint_name,size,qty,Date,current_month)
        session_query.add(recorded_paint)
        session_query.commit()

        #==========================
        paint_names_in_db = session_query.query(Thinner_stock_status ).order_by(Thinner_stock_status.ITEM_NAME)
        paint_names_list  = []
        for paint in paint_names_in_db: paint_names_list.insert (0, paint.ITEM_NAME)

        """ INSERTING DATA   """
        if (paint_name in paint_names_list): # do updating....
            row_2_update = session_query.query(Thinner_stock_status ).filter_by(ITEM_NAME = paint_name)
            
            if size == five_ltr:
                for quantity in row_2_update: quantity_in_db = quantity.FIVE_LTR # get quantity value
                new_quantity_value = int(quantity_in_db) - int(qty)
                session_query.query(Thinner_stock_status).filter_by(ITEM_NAME = paint_name).update({"FIVE_LTR":new_quantity_value})			
                session_query.commit()

            elif size == one_ltr:
                for quantity in row_2_update: quantity_in_db = quantity.ONE_LTR # get quantity value
                new_quantity_value = int(quantity_in_db) - int(qty)
                session_query.query(Thinner_stock_status).filter_by(ITEM_NAME = paint_name).update({"ONE_LTR":new_quantity_value})			
                session_query.commit()

        elif (paint_name not in paint_names_list):
            
            if (paint_name not in paint_names_list) and (size == five_ltr):
                sql = Thinner_stock_status(paint_name,0,qty)
                session_query.add(sql)
                session_query.commit()

            elif (paint_name not in paint_names_list) and (size == one_ltr):
                sql = Thinner_stock_status(paint_name,qty,0)
                session_query.add(sql)
                session_query.commit()

            elif (paint_name in paint_names_list):
                pass

	return "Data recorded well ......."
