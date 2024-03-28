from django.contrib import admin
from testapp.models import Hydjobs1,Bngjobs1,Punejobs1

class HydjobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','address','email','phonenumber']
admin.site.register(Hydjobs1,HydjobsAdmin)

class BngjobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','address','email','phonenumber']
admin.site.register(Bngjobs1,BngjobsAdmin)

class PunejobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','address','email','phonenumber']
admin.site.register(Punejobs1,PunejobsAdmin)
