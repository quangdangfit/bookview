from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='index'),
    path('books/', views.CreateBookView.as_view(), name='create_book'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='detail'),
    path('authors/', views.AuthorListView.as_view(), name='author_list'),
    path('authors/<int:pk>/', views.AuthorDetailView.as_view(), name='author_profile'),
    path('genres/<int:pk>/', views.GenreDetailView.as_view(), name='genre_detail'),
    path('login/', views.LoginView.as_view(), name='my_login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('', include('social_django.urls', namespace='social')),
    path('logout/', views.logout, name='logout'),
    path('users/<int:pk>/', views.UserProfile.as_view(), name='user_profile'),
]