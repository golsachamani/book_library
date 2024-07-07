from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import *

admin.site.register(Book)
admin.site.register(Member)
admin.site.register(BookInstace)
admin.site.register(Lend)
admin.site.register(Comment)
