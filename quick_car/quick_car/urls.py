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
    url(r'^mecedit', views.mecedit, name='mecedit'),
    url(r'^sh2', views.sh2, name='sh2'),
    url(r'^minihistory', views.minihistory, name='minihistory'),
    url(r'^editprofile', views.editprofile, name='editprofile'),
    url(r'^brows', views.brows, name='brows'),
    url(r'^formbill', views.formbill, name='formbill'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^bill', views.bill, name='bill'),
    url(r'^mechanic_home', views.mechanic_home, name='mechanic_home'),
    url(r'^login', views.login, name='login'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^signup', views.signup, name='signup'),
    url(r'^history',views.history,name='history'),
    url(r'^single_history',views.single_history,name='single_history'),
    url(r'^send_notification',views.send_notification,name='send_notification'),
    url(r'^get_notification',views.get_notification,name='get_notification'),
    url(r'^show_notification',views.show_notification,name='show_notification'),
    url(r'^open_send_bill',views.open_send_bill,name='open_send_bill'),
    url(r'^signgarage',views.signgarage,name='signupgarage'),
    url(r'^payment',views.payment,name='payment'),
    url(r'^test',views.test,name='test'),
    url(r'^sest',views.test,name='sest'),
    url(r'^create_job',views.create_job,name='create_job'),
    url(r'^send_job',views.send_job,name='send_job'),
    url(r'^auth_login',views.auth_login,name='auth_login'),
    url(r'^get_garage',views.get_garage,name='get_garage'),
    url(r'^wait',views.wait,name='wait'),
    url(r'^match_complete',views.match_complete,name='match_complete'),
    url(r'^match_fail',views.match_fail,name='match_fail'),
    url(r'^get_location_garage',views.get_location_garage,name='get_location_garage'),
    url(r'^get_noti_from_click',views.get_noti_from_click,name='get_noti_from_click'),
    url(r'^res_noti_to_bill',views.res_noti_to_bill,name='res_noti_to_bill'),
    url(r'^select_mechanic',views.select_mechanic,name='select_mechanic'),
    url(r'^is_match_complete',views.is_match_complete,name='is_match_complete'),
    url(r'^get_user_match',views.get_user_match,name='get_user_match'),
    url(r'^get_history',views.get_history,name='get_history'),
    url(r'^get_history_from_click',views.get_history_from_click,name='get_history_from_click'),
    url(r'^res_history_to_single',views.res_history_to_single,name='res_history_to_single'),
    url(r'^click',views.click,name='click'),
    url(r'^sing_up_new_user',views.sing_up_new_user,name='sing_up_new_user'),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
