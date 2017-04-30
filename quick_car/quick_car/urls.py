"""quick_car URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from quick_app import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^map', views.map, name='map'),
    url(r'^login', views.login, name='login'),
    url(r'^signup', views.signup, name='signup'),
    url(r'^history',views.history,name='history'),
<<<<<<< HEAD
    url(r'^signgarage',views.signupgarage,name='signupgarage'),
    url(r'^send_notification',views.send_notification,name='send_notification'),
    url(r'^get_notification',views.get_notification,name='get_notification'),
    url(r'^open_send_bill',views.open_send_bill,name='open_send_bill')
=======
    url(r'^signgarage',views.signgarage,name='signgarage'),
    url(r'^payment',views.payment,name='payment'),
    url(r'^test',views.test,name='test'),
>>>>>>> 54d76559416fed0a194000b7b2e22895a7fe6c94
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
