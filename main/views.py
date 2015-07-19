from django.shortcuts import render
from django.views.generic import View
from .models import User


class UserIndexView(View):
    template_name = 'main/index.html'

    def get(self, request):
        user_list = User.objects.all()[:5]
        return render(request, self.template_name, {'user_list': user_list})
