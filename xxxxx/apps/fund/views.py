from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .backend import FundHelper


# Create your views here.
class FundIndexView(LoginRequiredMixin, View):
    login_url = 'login'
    f = FundHelper

    def get(self, request):

        data = self.f.get_multiple_data([160716])
        return render(request, 'index.html', {'item': data})