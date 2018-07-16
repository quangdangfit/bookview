from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/<int:ma_sach>/', views.detail, name='detail'),
    path('authors/<int:ma_tg>/', views.author_profile, name='author_profile'),
    path('genres/<int:ma_loai>/', views.genre_detail, name='genre_detail'),
    path('', include('social_django.urls', namespace='social')),
    path('logout/', views.logout, name='logout'),
    path('login/', views.my_login, name='my_login'),
    path('register/', views.register, name='register'),
]