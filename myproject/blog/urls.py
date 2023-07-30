from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.main, name='main'),  # URL для основної сторінки
    path('blog_post/', views.post, name='blog_post'),
    path('daily_plan/create/', views.daily_plan_create, name='create_daily_plan'),
    path('daily_plan/<int:plan_id>/', views.view_daily_plan, name='view_daily_plan'),
    path('daily_plan/list/', views.list_daily_plans, name='list_daily_plans'),
    path('daily_plans_by_date/<str:date>/', views.daily_plans_by_date, name='daily_plans_by_date'),
    path('post/create/', views.create_post, name='create_post'),
]