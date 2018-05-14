from django.conf.urls import url
from . import views

app_name = 'customer'
urlpatterns = [
    url(r'^$', views.customer_list, name='customer_list'),
    url(r'^import/', views.customer_import, name='customer_import'),
]
