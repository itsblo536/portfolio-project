from django.urls import path
from . import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    # allows users to search for blogs by number
    path('<int:blog_id>/', views.detail, name='detail'),
] 