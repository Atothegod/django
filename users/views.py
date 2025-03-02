from django.shortcuts import render
from django.http import HttpResponse

# ฟังก์ชันสำหรับการสมัครสมาชิก
def sign_up(request):
    return HttpResponse("Sign Up Page")

# ฟังก์ชันสำหรับการเข้าสู่ระบบ
def login(request):
    return HttpResponse("Login Page")

# ฟังก์ชันสำหรับการดูโปรไฟล์
def view_profile(request):
    return HttpResponse("Profile Page")

# ฟังก์ชันสำหรับการจัดการบัตรของขวัญ
def manage_gift_card(request):
    return HttpResponse("Manage Gift Card Page")