from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Subject)
admin.site.register(Assignment)
admin.site.register(Test)
admin.site.register(UserSubjectRelation)
admin.site.register(Question)
admin.site.register(StudentAnswer)
