from django.conf.urls import url
from django.contrib import admin
from django.urls import include

from User import views


urlpatterns = [
    url('^admin/', admin.site.urls),
    url ('^signup/$', views.signup, name='signup'),
    url('accounts/', include('django.contrib.auth.urls')),
    url('^$', views.home, name='home'),

]
