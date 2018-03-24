from django.contrib import admin

from . import models

# Register your models here.


class InlineAddress(admin.StackedInline):
    model = models.Address
    extra = 0
    min_num = 0
    max_num = 100


class InlineHistory(admin.StackedInline):
    model = models.History
    extra = 0
    min_num = 0
    max_num = 100


class UserAdmin(admin.ModelAdmin):
    inlines = [InlineAddress, InlineHistory]


admin.site.register(models.User, UserAdmin)
