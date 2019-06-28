from django.urls import path

from FDUSystem import views
from django.conf.urls import url

app_name = 'FDUSystem'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index.html$', views.index, name='index'),
    url(r'^signin.html$', views.signin, name='signin'),
    url(r'^signup.html$', views.signup, name='signup'),
    url(r'^index.html$', views.signout, name='signout'),
    url(r'^home.html$', views.home, name='home'),
    url(r'^home/.+$', views.home, name='homepages'),
    url(r'^resetpsd.html$', views.resetpsd, name='resetpsd'),
    url(r'^deleteSelected/.+$', views.deleteSelected, name='delete'),
    url(r'^search/.+$', views.search, name='search'),
    url(r'^add/.+$', views.addpage, name='adddata'),
    url(r'^edit/.+$', views.edit, name='edit'),
    url(r'^edit.html$', views.edit, name='editpage'),
    url(r'^add.html$', views.addpage, name='addpage'),

]
