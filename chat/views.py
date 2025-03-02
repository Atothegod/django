# from django.shortcuts import render, get_object_or_404
# from django.http import JsonResponse
# from .models import ChatSupport
# from users.models import User
# from sellers.models import Seller

# # ฟังก์ชันสำหรับแชทกับผู้ขาย
# def chat_with_seller(request):
#     if request.method == "POST":
#         # รับข้อมูลจาก request
#         user = request.user  # ผู้ใช้ที่ทำการแชท
#         seller_id = request.POST.get("seller_id")  # id ของผู้ขาย
#         message = request.POST.get("message")  # ข้อความที่ส่งไป

#         seller = get_object_or_404(Seller, id=seller_id)  # หาผู้ขายจาก id

#         # สร้าง chat entry
#         chat = ChatSupport.objects.create(user=user, seller=seller, message=message)

#         return JsonResponse({"status": "success", "message": chat.message})

#     return render(request, 'chat/chat_with_seller.html')  # หน้าแสดงแชทกับผู้ขาย

# # ฟังก์ชันสำหรับแชทกับแอดมิน
# def chat_with_admin(request):
#     if request.method == "POST":
#         # รับข้อมูลจาก request
#         user = request.user  # ผู้ใช้ที่ทำการแชท
#         message = request.POST.get("message")  # ข้อความที่ส่งไป

#         admin = User.objects.filter(is_staff=True).first()  # หาผู้ดูแลระบบแอดมิน

#         # สร้าง chat entry
#         chat = ChatSupport.objects.create(user=user, admin=admin, message=message)

#         return JsonResponse({"status": "success", "message": chat.message})

#     return render(request, 'chat/chat_with_admin.html')  # หน้าแสดงแชทกับแอดมิน
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# ฟังก์ชันสำหรับการแชทกับผู้ขาย
@login_required
def chat_with_seller(request):
    # โค้ดที่เกี่ยวข้องกับการแชทกับผู้ขาย
    return render(request, 'chat/seller_chat.html')  # เปลี่ยนเป็น template ที่ต้องการ

# ฟังก์ชันสำหรับการแชทกับแอดมิน
@login_required
def chat_with_admin(request):
    # โค้ดที่เกี่ยวข้องกับการแชทกับแอดมิน
    return render(request, 'chat/admin_chat.html')  # เปลี่ยนเป็น template ที่ต้องการ
