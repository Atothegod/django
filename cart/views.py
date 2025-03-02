from django.shortcuts import render
from django.http import JsonResponse
from .models import ShoppingCart, PaymentSystem, OrderSystem
from users.models import User

# ฟังก์ชันสำหรับดูตะกร้าสินค้า
def view_cart(request):
    # จำลองข้อมูลการแสดงตะกร้า
    cart_items = ShoppingCart.objects.filter(user=request.user)
    return render(request, 'cart/view_cart.html', {'cart_items': cart_items})

# ฟังก์ชันสำหรับเพิ่มสินค้าในตะกร้า
def add_item(request):
    if request.method == "POST":
        # รับข้อมูลสินค้าและเพิ่มในตะกร้า
        product_id = request.POST.get("product_id")
        # จำลองการเพิ่มสินค้า
        cart = ShoppingCart(user=request.user)
        cart.save()  # เพิ่มรายการในตะกร้า

        return JsonResponse({"status": "success", "message": "Item added to cart"})

    return JsonResponse({"status": "error", "message": "Invalid request"})

# ฟังก์ชันสำหรับลบสินค้าออกจากตะกร้า
def remove_item(request):
    if request.method == "POST":
        # รับข้อมูลสินค้าและลบออกจากตะกร้า
        product_id = request.POST.get("product_id")
        # จำลองการลบสินค้า
        cart = ShoppingCart.objects.filter(user=request.user, id=product_id).first()
        if cart:
            cart.delete()
            return JsonResponse({"status": "success", "message": "Item removed from cart"})
        return JsonResponse({"status": "error", "message": "Item not found in cart"})

    return JsonResponse({"status": "error", "message": "Invalid request"})

# ฟังก์ชันสำหรับการชำระเงิน
def process_payment(request):
    if request.method == "POST":
        # จำลองการประมวลผลการชำระเงิน
        payment = PaymentSystem(user=request.user)
        payment.save()  # ประมวลผลการชำระเงิน

        return JsonResponse({"status": "success", "message": "Payment processed successfully"})

    return JsonResponse({"status": "error", "message": "Invalid request"})

# ฟังก์ชันสำหรับสร้างใบแจ้งหนี้
def generate_invoice(request):
    if request.method == "POST":
        # จำลองการสร้างใบแจ้งหนี้
        invoice = "Invoice data here"
        return JsonResponse({"status": "success", "message": invoice})

    return JsonResponse({"status": "error", "message": "Invalid request"})

# ฟังก์ชันสำหรับการสั่งซื้อสินค้า
def place_order(request):
    if request.method == "POST":
        # จำลองการสั่งซื้อสินค้า
        order = OrderSystem(user=request.user)
        order.save()  # สั่งซื้อสินค้า

        return JsonResponse({"status": "success", "message": "Order placed successfully"})

    return JsonResponse({"status": "error", "message": "Invalid request"})

# ฟังก์ชันสำหรับติดตามสถานะการสั่งซื้อ
def track_order(request):
    order_id = request.GET.get("order_id")
    order = OrderSystem.objects.filter(id=order_id).first()

    if order:
        # จำลองการติดตามสถานะการสั่งซื้อ
        return JsonResponse({"status": "success", "order_status": "Order is being processed"})
    return JsonResponse({"status": "error", "message": "Order not found"})

# ฟังก์ชันสำหรับยกเลิกคำสั่งซื้อ
def cancel_order(request):
    order_id = request.GET.get("order_id")
    order = OrderSystem.objects.filter(id=order_id).first()

    if order:
        order.delete()  # ยกเลิกคำสั่งซื้อ
        return JsonResponse({"status": "success", "message": "Order cancelled successfully"})

    return JsonResponse({"status": "error", "message": "Order not found"})
