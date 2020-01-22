
from main_file import app, allow_cross_origin
from flask import render_template,request,redirect,url_for

# Testing the server .....
@app.route("/in")
def index ():
    return allow_cross_origin("<br><br><center><b>Hi :: Henry :: </b><br>... The Server Is Running Well ...</center>")

# Admin Index Gui .....
# @app.route("/admin")
# def admin ():
#     return allow_cross_origin(render_template('AdminLogIn.html'))

@app.route("/validate_login",methods=["POST","GET"])
def validate_login ():
    uname = 'admin'
    pwd = 'kankan2019'
    admin_uname_input = request.form['uname']
    admin_pwd_input = request.form['pwd']

    if (admin_uname_input == uname) and (admin_pwd_input == pwd):
        return redirect(url_for('success'))
    else:
        return redirect(url_for('admin'))

@app.route("/admin")
def success ():
    return allow_cross_origin(render_template('AdminEntriesGui.html'))
    
@app.route("/AdminIndex")
def AdminIndex_gui () :
    return allow_cross_origin(render_template('AdminEntriesGui.html'))

@app.route("/AdminAddChintNames")
def AdminAddChintNames_gui ():
    return allow_cross_origin(render_template('AdminAddChintNames.html'))
