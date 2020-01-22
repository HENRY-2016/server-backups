


from main_file import *


agency_db_connection = create_engine('sqlite:///data_bases/agency/agency.db')

@app.route('/test',methods=['POST'])
def test ():
    if  request.method == 'POST':
        airtel_1 = request.form['airtel']
        mtn_1 = request.form['mtn']
        print"=================="
        print airtel_1
        print "0000000000000000000000"
        print mtn_1
        return "received well....."

@app.route('/agency_record_new_day',methods=['POST'])
def reply_agency_record_new_day ():
    import datetime
    DBsession = sessionmaker(bind=agency_db_connection)
    session_query = DBsession()
    d = datetime.datetime.today()
    current_month = d.month #d.year

    if  request.method == 'POST':
        uname= request.form['uname']
        Date = request.form['date']
        airtel_1 = request.form['airtel']
        mtn_1 = request.form['mtn']
        centenary_1 = request.form['centenary']
        dfcu_1 = request.form['dfcu']
        dtb_1 = request.form['dtb']
        equity_1 = request.form['equity']
        stanbic_1 = request.form['stanbic']
        barclays_1 = request.form['barclays']
        drawings_1 = request.form['drawings']

        # cash 
        k50 = request.form['50k']
        k20 = request.form['20k']
        k10 = request.form['10k']
        k5 = request.form['5k']
        k2 = request.form['2k']
        k1 = request.form['1k']
        _1000 = request.form['_1000']
        _500 = request.form['_500']
        _200 = request.form['_200']
        _100 = request.form['_100']
        _50 = request.form['_50']
        
        # Do math
        papers = int(k50)+int(k20)+int(k10)+int(k5)+int(k2)+int(k1)
        coins = int(_1000)+int(_500)+int(_200)+int(_100)+int(_50)

        banks_1 = int(airtel_1)+int(mtn_1)+int(dfcu_1)+int(dtb_1)+int(equity_1)+int(stanbic_1)+int(barclays_1)
        cash_1 = papers + coins
        float_1 = cash_1 + banks_1 + int(drawings_1)
        
        # format with commas
        airtel = format(int(airtel_1),",")
        mtn = format(int(mtn_1), ",")
        centenary = format(int(centenary_1), ",")
        dfcu = format(int(dfcu_1), ",")
        dtb = format(int(dtb_1), ",")
        equity = format(int(equity_1), ",")
        stanbic = format(int(stanbic_1), ",")
        barclays = format(int(barclays_1), ",")
        drawings = format(int(drawings_1),",")
        banks = format(int(banks_1),",")
        cash = format(int(cash_1),",")
        Float = format(int(float_1),",")
        # print banks



        # UNAME,DATE,AIRTEL,MTN,CENTENARY,DFCU,DTB,EQUITY,STANBIC,BARCLAYS,CASH,DRAWINGS BANKS,FLOAT
        agency_new_day = Agency_New_day( current_month, uname,Date,airtel,mtn,centenary,dfcu,dtb,equity,stanbic,barclays,cash,drawings,banks,Float)
        session_query.add(agency_new_day)
        session_query.commit() 
    return "Data Received and Recorded Well ....."
