from http.client import PAYMENT_REQUIRED
from re import A
from flask import *
from database import *

customer=Blueprint('customer',__name__)

@customer.route('/chome')
def chome():
    
    return render_template('user/user_home.html')

@customer.route('/viewmedicine')
def viewmedicine():
    data={}
    q="select * from medicine inner join medicine_shop using(medicine_id) inner join shop using(shop_id)"
    data['md']=select(q)
    
    return render_template('user/view_medicine.html',data=data)


@customer.route('/customercart',methods=['get','post'])
def customercart():
    data={}
    q="SELECT * FROM order_master INNER JOIN order_child USING(om_id) INNER JOIN `user` USING(user_id) INNER JOIN shop USING(shop_id) INNER JOIN medicine USING(medicine_id) where user_id='%s' and order_master.status='pending'"%(session['cus_id'])
    data['od']=select(q)
    
    if 'id' in request.args:
        id=request.args['id']
        sid=request.args['sid']
        q="select * from medicine where medicine_id='%s'"%(id)
        res=select(q)
        data['dm']=res
    if 'add' in request.form:
        sid=request.args['sid']
        print(sid)
        mid=request.form['mid']
        pri=request.form['pri']
        qua=request.form['qua']
        tot=request.form['tot']
        q="select * from order_master where  user_id='%s' and status='pending'"%(session['cus_id'])
        print(q)
        res=select(q)
        if res:
            ommid=res[0]['om_id']
            q="select * from order_master where shop_id='%s'"%(sid)
            e=select(q)
            print(q)
            if e:
                q="select * from order_master inner join order_child using(om_id) where medicine_id='%s'"%(mid)
                print(q)
                res=select(q)
                if res:
                    ommid=res[0]['om_id']
                    
                    q="update order_master set total=total+'%s' where om_id='%s'"%(tot,ommid)
                    update(q)
                    q="update order_child set quantity=quantity+'%s' where medicine_id='%s'"%(qua,mid)
                    update(q)
                    flash("Medicine Already in Cart Quantity Updated.......")
                    return redirect(url_for('customer.viewmedicine'))
                else:
                    q="update order_master set total=total+'%s' where om_id='%s'"%(tot,ommid)
                    update(q)
                    q="insert into order_child values(null,'%s','%s','%s','%s',now())"%(ommid,mid,qua,pri)
                    insert(q)
                    flash("Medicine Added To Cart.......")
                    return redirect(url_for('customer.viewmedicine'))
            else:
                flash("One Item from another shop is existed your cart.... kindly please remove the current item or purcahse from same shop...")
        else:
            q="insert into order_master  values(null,'%s','%s','%s',now(),'pending')"%(session['cus_id'],sid,tot)        
            nid=insert(q)
            q="insert into order_child values(null,'%s','%s','%s','%s',now())"%(nid,mid,qua,pri)
            insert(q)
            flash("Medicine Added To Cart.......")
            return redirect(url_for('customer.viewmedicine'))
        
    if 'checkout' in request.form:
        amt=request.form['amt']
        sp_id=request.form['sp_id']
        om_id=request.form['om_id']
        data['pay']=amt
        data['sp_id']=sp_id
        data['om_id']=om_id
    
    if 'pay' in request.form:
        sp_id=request.form['sp_id']
        om_id=request.form['om_id']
        tamt=request.form['tamt']
        q="insert into payment values(null,'%s','%s','%s',now())"%(session['cus_id'],sp_id,tamt)
        insert(q)
        q="update order_master set status='paid' where om_id='%s'"%(om_id)
        update(q)
        flash("payment_succesfull.......")
        return redirect(url_for('customer.viewmedicine'))
        
    if 'rm' in request.args:
        rm=request.args['rm']
        q="delete from order_master where om_id='%s'"%(rm)
        delete(q)
        q="delete from order_child where om_id='%s'"%(rm)
        delete(q)    
    return render_template('user/customer_cart.html',data=data)


@customer.route('/myorders',methods=['get','post'])
def myorders():
    data={}
    
    q="SELECT * FROM order_master INNER JOIN order_child USING(om_id) INNER JOIN `user` USING(user_id) INNER JOIN shop USING(shop_id) INNER JOIN medicine USING(medicine_id) where user_id='%s' and order_master.status='paid' or order_master.status='outfordelivery' or order_master.status='delivered'"%(session['cus_id'])
    print(q)
    data['od']=select(q)
    
    if 'sid' in request.args:
        sid=request.args['sid']
        data['sid']=sid

    if 'send' in request.form:
        sid=request.form['sid']
        com=request.form['comp']
        q="insert into complaints values(null,'%s','%s','%s','pending',now())"%(session['cus_id'],sid,com)
        insert(q)
        flash("complaint added successfully......")
        return redirect(url_for('customer.myorders'))
       


    # q="select * from complaints inner join shop using (shop_id) inner join user using (user_id)";
    # res=select(q)
    # data['comp']=res


    return render_template('user/user_myorders.html',data=data)

# @customer.route('/sendcomplaint',methods=['get','post'])
# def sendcomplaint():
#     return render_template('user/sendcomplaint.html')
   


