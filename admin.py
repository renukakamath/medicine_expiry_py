from flask import *
from database import *
from datetime import date

admin=Blueprint('admin',__name__)

@admin.route('/adhome')
def adhome():
    return render_template('admin/admin_home.html')


@admin.route('/addmed',methods=['get','post'])
def addmed():
    data={}
    today = date.today()
    data['today']=today
    print(data['today'])
    q="select * from medicine"
    res=select(q)
    data['md']=res
    
    if 'add' in request.form:
        mname=request.form['mname']
        mdesc=request.form['mdesc']
        mstock=request.form['mstock']
        mprice=request.form['mprice']
        exp=request.form['exp']
        q="insert into medicine values(null,'%s','%s','%s','%s','%s','pending')"%(mname,mdesc,mstock,mprice,exp)
        insert(q);
        flash("Medicine Added....")
        return redirect(url_for('admin.addmed'))
    
    
    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
    else:
        action=None
    if action=="delete":
        q="delete from medicine where medicine_id='%s'"%(id)
        delete(q)
    if action=="update":
        q="select * from medicine where medicine_id='%s'"%(id)
        res=select(q)
        data['sc']=res
        
    if 'edit' in request.form:
        mname=request.form['mname']
        mdesc=request.form['mdesc']
        mstock=request.form['mstock']
        mprice=request.form['mprice']
        exp=request.form['exp']    
        q="update medicine set medicine_name='%s',description='%s',stock='%s',price='%s',exp_date='%s' where medicine_id='%s'"%(mname,mdesc,mstock,mprice,exp,id)
        update(q)
        flash("Update Successfully")
        return redirect(url_for('admin.addmed'))
                                                
    if 'medid' in request.args:
        medid=request.args['medid']
        q="delete from medicine where medicine_id='%s'"%(medid)
        delete(q)    
        flash("Medicine Removed....")                                                                                                                                                                
    return render_template("admin/manage_medicine.html",data=data)
@admin.route('/viewuser')
def viewuser():
    data={}
    q="select * from user"
    res=select(q)
    data['user']=res
    return render_template("admin/viewuser.html",data=data)

@admin.route('/Viewcomplaint')
def Viewcomplaint():
    data={}
    uid=request.args['uid']
    q="select * from complaints inner join user using (user_id) inner join shop using (shop_id) where user_id='%s'"%(uid)
    res=select(q)
    data['comp']=res
    return render_template('admin/Viewcomplaint.html',data=data,uid=uid)
@admin.route('/sendreply',methods=['post','get'])
def sendreply():

    if "sendreply" in request.form:
        cid=request.args['cid']
        rep=request.form['reply']
        uid=request.args['uid']

        q="update complaints set replay='%s' where complaint_id='%s'"%(rep,cid)
        update(q)
        return redirect(url_for('admin.Viewcomplaint',uid=uid))
        
    return render_template('admin/sendreply.html')

@admin.route('/viewshop')
def viewshop():
    data={}

    q="select * from shop"
    res=select(q)
    data['shp']=res

    return render_template('admin/viewshop.html',data=data)


    
   


    



