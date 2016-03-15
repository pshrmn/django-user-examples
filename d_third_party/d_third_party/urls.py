from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import logout

from aorb.views import choice_view

urlpatterns = [
    url(r'^$', choice_view, name='home'),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^logout$', logout, {'next_page': 'home'}, name='logout')
]

urlpatterns += [
    url(r'^admin/', admin.site.urls),
]
