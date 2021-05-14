from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Tickets,Order,Update
import json

# Create your views here.
def index(request):
    categorylist=[]
    for i in Product.objects.all():
        if i.category not in categorylist:
                categorylist.append(i.category)

    final=[]
    classvalue=0
    for i in categorylist:
        classvalue+=1
        # x=range(1,len(Product.objects.filter(category=i)))
        final.append([Product.objects.filter(category=i),classvalue])
        # print(len(Product.objects.filter(category=i)))

    return render(request,'shop/index.html',{'categories':final })
def aboutus(request):
    return render(request,'shop/aboutUs.html')
def contactus(request):
    tname=request.POST.get('name','')
    temail=request.POST.get('email','')
    tvalue=request.POST.get('ticket','')
    ticket=Tickets(name=tname,email=temail,ticket=tvalue)
    ticket.save()
    return render(request,'shop/contactUs.html')
def prodview(request,myid):
    prod=Product.objects.filter(id=myid)
    return render(request,'shop/prodView.html',{'product':prod[0]})
def tracker(request):
    if request.method=='POST':
        order_id=request.POST.get('orderId','')
        email=request.POST.get('email','')
        result=Order.objects.filter(email=email,order_id=order_id)
        if len(result)>0:
            ordersummary=json.loads(result[0].cartjson)
            # smmry=json.dumps(ordersummary)
            updates={}
            for i in Update.objects.filter(order_id=order_id):
                updates[i.order_update]=str(i.timestamp)[:8]
            # updt=json.dumps(updates)
            
            return render(request,'shop/tracker.html',{'summary':ordersummary,'updates':updates,'search':True})
        else:
            return render(request,'shop/tracker.html',{'search':False})
    return render(request,'shop/tracker.html')
def checkout(request):
    if request.method=='POST':
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        address=request.POST.get('address','')
        state=request.POST.get('state','')
        city=request.POST.get('city','')
        zip_code=request.POST.get('zip_code','')
        cartjson=request.POST.get('cartjson','')
        orderplaced=True
        order=Order(name=name,email=email,phone=phone,address=address,state=state,city=city,zip_code=zip_code,cartjson=cartjson)
        orderid=order.order_id
        order.save()
        orderid=order.order_id
        updates=Update(order_id=orderid,order_update='Order has been placed.')
        updates.save()
        return render(request,'shop/checkout.html',{'orderplaced':orderplaced,'id':orderid})
    return render(request,'shop/checkout.html')


