from django.db import models

class Searching(models.Model):
    query = models.CharField(max_length=255)

    def filter(self):
        # ฟังก์ชันกรองข้อมูล
        pass

    def search(self):
        # ฟังก์ชันค้นหาข้อมูล
        pass

