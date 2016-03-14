from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import redirect

from .forms import CreateUserForm


class RegisterView(CreateView):

    """
    create a new user
    """

    template_name = 'registration/register.html'
    model = User
    form_class = CreateUserForm
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        auth_login(self.request, user)
        return redirect('home')
