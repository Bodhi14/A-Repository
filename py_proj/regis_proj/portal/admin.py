from django.contrib import admin
from .models import Answer

# Register your models here.

class AnswerModel(admin.ModelAdmin):
    list_display = ['ans1', 'ans2', 'ans3', 'ans4']

admin.site.register(Answer, AnswerModel)
