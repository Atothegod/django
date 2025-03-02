from django.shortcuts import render
from users.models import User
from sellers.models import Seller

def manage_users(request):
    users = User.objects.all()
    return render(request, 'adminpanel/manage_users.html', {'users': users})

def manage_sellers(request):
    sellers = Seller.objects.all()
    return render(request, 'adminpanel/manage_sellers.html', {'sellers': sellers})

def view_reports(request):
    # สามารถทำการแสดงผลหรือจัดการรายงานที่เกี่ยวข้อง
    return render(request, 'adminpanel/view_reports.html')
