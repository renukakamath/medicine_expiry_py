from flask import *
from database import *


public=Blueprint('public',__name__)

@public.route('/')
def home():
    return render_template('public/index.html')


@public.route('/login',methods=['get','post'])
def login():
    if 'login' in request.form:
        uname=request.form['uname']
        passw=request.form['passw']
        q="select * from login where user_name='%s' and password='%s'"%(uname,passw)
        res=select(q)
        if res:
            utype=res[0]['user_type']
            session['log_id']=res[0]['login_id']
            log_id=session['log_id']
            if utype=='admin':
                
                return redirect(url_for('admin.adhome'))
            elif utype=='user':
                q="select * from user where login_id='%s'"%(session['log_id'])
                res=select(q)
                if res:
                    session['cus_id']=res[0]['user_id']
                    cus_id=session['cus_id']
                    return redirect(url_for('customer.chome'))
                
                
            elif utype=="shop":
                q="select * from shop where login_id='%s'"%(session['log_id'])
                res=select(q)
                if res:
                    session['sh_id']=res[0]['shop_id']
                    sh_id=session['sh_id']
                    return redirect (url_for('shop.shome'))
        else:
            flash("invalid username or password.....")
            return redirect(url_for('public.login'))
                
     
    return render_template('public/login.html')


@public.route('/custreg',methods=['get','post'])
def custreg():
    if 'add' in request.form:
        fname=request.form['fname']     
        lname=request.form['lname']     
        place=request.form['place']     
        phone=request.form['phone']     
        email=request.form['email']     
        uname=request.form['uname']     
        passw=request.form['passw']   
        q="insert into login values(null,'%s','%s','user')"%(uname,passw)
        id=insert(q)
        q="insert into user values(null,'%s','%s','%s','%s','%s','%s')"%(id,fname,lname,place,phone,email)
        insert(q)
        return redirect(url_for('public.login'))  
    return render_template('public/customer_register.html')


@public.route('/shopreg',methods=['get','post'])
def shopreg():
    if 'add' in request.form:
        sname=request.form['sname']     
        place=request.form['place']     
        phone=request.form['phone']     
        email=request.form['email']     
        uname=request.form['uname']     
        passw=request.form['passw']   
        q="insert into login values(null,'%s','%s','shop')"%(uname,passw)
        id=insert(q)
        q="insert into shop values(null,'%s','%s','%s','%s','%s')"%(id,sname,place,phone,email)
        insert(q)
        return redirect(url_for('public.login'))
    
    return render_template('public/shop_reg.html')