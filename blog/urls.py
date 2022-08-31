from django.urls import path
from . import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    # detects if an int is in url path; if so, stores int as blog_id
    # and passes into detail function
    path('<int:blog_id>/', views.detail, name='detail'),
] 