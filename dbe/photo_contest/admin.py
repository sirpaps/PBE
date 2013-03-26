from django.contrib import admin
from dbe.photo_contest.models import *

class PromotionAdmin(admin.ModelAdmin):
    # search_fields = ["title"]
    list_display = ["name"]

class ImageProfileAdmin(admin.ModelAdmin):
    list_display = ["email", "caption", "image"]

admin.site.register(ImageProfile, ImageProfileAdmin)
admin.site.register(Promotion, PromotionAdmin)