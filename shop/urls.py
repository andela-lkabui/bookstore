from django.conf.urls import url, include

import views

urlpatterns = [
    url(r'^search/', views.search, name='search'),
]