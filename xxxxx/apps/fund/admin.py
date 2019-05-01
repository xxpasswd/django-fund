from django.contrib import admin
from django.db import IntegrityError

from .models import Fund, UserFund, FundDetail

# Register your models here.


def add_to_user_have(modeladmin, request, queryset):
    user = request.user
    for q in queryset:
        try:
            UserFund.objects.create(code=q, user=user, status=1)
        except IntegrityError:
            UserFund.objects.filter(code=q).update(status=1)


def add_to_user_monitor(modeladmin, request, queryset):
    user = request.user
    for q in queryset:
        try:
            UserFund.objects.create(code=q, user=user, status=2)
        except IntegrityError:
            UserFund.objects.filter(code=q).update(status=2)


@admin.register(Fund)
class FundAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'is_valid')
    list_editable = ('is_valid',)
    actions = [add_to_user_have, add_to_user_monitor]
    pass


class UserFundAdmin(admin.ModelAdmin):
    list_display = ('code', 'user', 'status', 'is_valid')
    list_editable = ('status',)


# admin.site.register(Fund, FundAdmin)
admin.site.register(FundDetail)
admin.site.register(UserFund, UserFundAdmin)
