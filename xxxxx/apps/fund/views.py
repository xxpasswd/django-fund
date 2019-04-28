from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .backend import FundHelper
from .models import UserFund


# Create your views here.
class FundIndexView(LoginRequiredMixin, View):
    login_url = 'login'
    f = FundHelper

    def get(self, request):

        codes = UserFund.objects.values_list('code__code', flat=True)
        data = self.f.get_multiple_data(codes)
        return render(request, 'index.html', {'item': data})
