from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout

from aorb.views import choice_view
from user.views import RegisterView

urlpatterns = [
    url(r'^$', choice_view, name='home'),
    # include the auth urls for ease of use
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^register$', RegisterView.as_view(), name='register'),
    url(r'^login$', login, name='login'),
    url(r'^logout$', logout, {'next_page': 'home'}, name='logout')
]

urlpatterns += [
    url(r'^admin/', admin.site.urls),
]
