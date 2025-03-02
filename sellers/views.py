from django.shortcuts import render, redirect
from .models import Seller
from django.contrib.auth.decorators import login_required

# ฟังก์ชันสำหรับลงทะเบียนเป็น Seller
@login_required
def register_seller(request):
    if request.method == 'POST':
        shop_name = request.POST.get('shop_name')
        # สร้าง Seller ใหม่
        Seller.objects.create(user=request.user, shop_name=shop_name)
        return redirect('manage_profile')  # หลังจากลงทะเบียนเสร็จ จะไปที่หน้าโปรไฟล์
    return render(request, 'sellers/register.html')

# ฟังก์ชันสำหรับจัดการโปรไฟล์ของ Seller
@login_required
def manage_profile(request):
    seller = Seller.objects.get(user=request.user)  # ค้นหา Seller จาก user ที่ล็อกอิน
    return render(request, 'sellers/profile.html', {'seller': seller})

# ฟังก์ชันสำหรับจัดการสินค้าของ Seller (สามารถเพิ่มฟังก์ชันได้ตามต้องการ)
@login_required
def manage_products(request):
    seller = Seller.objects.get(user=request.user)  # ค้นหา Seller จาก user ที่ล็อกอิน
    products = seller.products.all()  # ดึงข้อมูลสินค้าทั้งหมดของ Seller นี้
    return render(request, 'sellers/products.html', {'products': products})

@login_required
# sellers/views.py
def manage_point(request):
    # โค้ดสำหรับจัดการคะแนน
    return render(request, 'sellers/point.html')
