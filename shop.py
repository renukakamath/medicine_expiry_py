from flask import *
from database import *


shop=Blueprint('shop',__name__)


@shop.route('/shome')
def shome():
    
    return render_template('shop/shop_home.html')

@shop.route('/viewmed',methods=['get','post'])
def viewmed():
    data={}
    q="select * from medicine"
    data['md']=select(q)
    
    return render_template('shop/view_med.html',data=data)

@shop.route('/purchasemed',methods=['get','post'])
def purchasemed():
    data={}
    
    
    if 'id' in request.args:
        id=request.args['id']
        q="select * from medicine where medicine_id='%s'"%(id)
        data['dm']=select(q)
        
    if 'add' in request.form:
        ven=request.form['ven']   
        pri=request.form['pri']   
        qua=request.form['qua']
        tot=request.form['tot']
        q="select * from purchase_master where shop_id='%s'"%(session['sh_id'])
        res=select(q)
        if res:
            q="select * from purchase_master inner join purchase_child using(pm_id) where medicine_id='%s'"%(id)
            res=select(q)
            if res:
                pur_id=res[0]['pm_id']
                q="update purchase_master set total_amt=total_amt+'%s' where shop_id='%s'"%(tot,session['sh_id'])
                update(q)
                q="update purchase_child set quantity=quantity+'%s' where medicine_id='%s'"%(qua,id)
                update(q)
                flash("Quantity updated.....")
                return redirect(url_for('shop.viewmed'))
            else:
                q="update purchase_master set total_amt=total_amt+'%s' where shop_id='%s'"%(tot,session['sh_id'])
                update(q)
                q="insert into purchase_child values(null,'%s','%s','%s','%s')"%(idm,pur_id,qua,pri)   
                insert(q)
                q="insert into medicine_shop values(null,'%s','%s')"%(id,session['sh_id'])
                insert(q)
                flash("Successfully Purcahsed.....")
                return redirect(url_for('shop.viewmed'))
        else:
            q="insert into purchase_master values(null,'%s','%s','%s',now())"%(session['sh_id'],ven,tot,)
            idm=insert(q)
            q="insert into purchase_child values(null,'%s','%s','%s','%s')"%(idm,id,qua,pri)   
            insert(q)
            q="insert into medicine_shop values(null,'%s','%s')"%(id,session['sh_id'])
            insert(q)
            flash("Successfully Purcahsed.....")
            return redirect(url_for('shop.viewmed'))
    q="SELECT * FROM purchase_master INNER JOIN purchase_child INNER JOIN shop USING(shop_id) INNER JOIN medicine USING(medicine_id) INNER JOIN medicine_shop USING(shop_id) WHERE shop_id='%s'"%(session['sh_id'])
    data['vp']=select(q)
    
    return render_template('shop/puchase_medicine.html',data=data)

@shop.route('/viewbooking')
def viewbooking():
    data={}
    q="SELECT * FROM `order_child` INNER JOIN `order_master` USING (`om_id`)  INNER JOIN `user` USING (`user_id`) INNER JOIN medicine USING (medicine_id) where shop_id='%s'"%(session['sh_id'])
    res=select(q)
    data['book']=res


    if "action" in request.args:
        action=request.args['action']
        omid=request.args['omid']

        if action=='update':

            q="update order_master set status='Dispatched' where om_id='%s'"%(omid)
            update(q)


    return render_template('shop/viewbooking.html',data=data)

@shop.route('/Viewpayment')
def Viewpayment():
    data={}
    uid=request.args['uid']
    q="SELECT * FROM `payment` INNER JOIN `user` USING (user_id) INNER JOIN shop USING (shop_id) where user_id='%s'"%(uid)
    res=select(q)
    data['pay']=res
    return render_template('/shop/Viewpayment.html',data=data)




   


    
