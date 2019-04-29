from django.contrib import admin
from django.db import IntegrityError

from .models import Fund, UserFund, FundDetail

# Register your models here.


def add_to_user_fund(modeladmin, request, queryset):
    user = request.user
    for q in queryset:
        try:
            UserFund.objects.create(code=q, user=user)
        except IntegrityError:
            pass


@admin.register(Fund)
class FundAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'is_valid')
    list_editable = ('is_valid',)
    actions = [add_to_user_fund]
    pass


class FundDetailAdmin(admin.ModelAdmin):
    pass


class UserFundAdmin(admin.ModelAdmin):
    list_display = ('code', 'user', 'is_valid')


# admin.site.register(Fund, FundAdmin)
admin.site.register(FundDetail, FundDetailAdmin)
admin.site.register(UserFund, UserFundAdmin)
