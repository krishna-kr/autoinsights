from django.contrib import admin
from .models import FeedbackData

# Register your models here.


class FeedbackDataAdmin(admin.ModelAdmin):
    list_display = ('user','name','email','mobile','message','request_date')
admin.site.register(FeedbackData,FeedbackDataAdmin)