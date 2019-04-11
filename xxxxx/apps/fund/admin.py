from django.contrib import admin
from .models import Fund, UserFund, FundDetail

# Register your models here.


@admin.register(Fund)
class FundAdmin(admin.ModelAdmin):
    pass


class FundDetailAdmin(admin.ModelAdmin):
    pass


class UserFundAdmin(admin.ModelAdmin):
    pass


# admin.site.register(Fund, FundAdmin)
admin.site.register(FundDetail, FundDetailAdmin)
admin.site.register(UserFund, UserFundAdmin)
