from django.shortcuts import render
from django.http import JsonResponse
from .models import Searching

def search_view(request):
    query = request.GET.get('query', '')  # รับคำค้นหาจาก query parameter
    if query:
        # ตัวอย่างการค้นหาจากฐานข้อมูล
        results = Searching.objects.filter(query__icontains=query)
        results_list = [result.query for result in results]
        return JsonResponse({'results': results_list})
    return JsonResponse({'results': []})

def filter_view(request):
    # ตัวอย่างการกรองข้อมูล
    results = Searching.objects.all()  # สามารถกรองตามเงื่อนไขที่ต้องการได้
    results_list = [result.query for result in results]
    return JsonResponse({'results': results_list})