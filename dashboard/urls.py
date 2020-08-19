from django.urls import path
from . import views


urlpatterns = [
    path('', views.BookList.as_view(), name='book_list'),
    # path('detail/<int:pk>/', views.BookDetail.as_view(), name='book_detail'),
    path('user/<str:username>', views.UserBookListView.as_view(), name='user_books'),
    path('detail/<int:pk>/', views.book_detail, name='book_detail'),
    path('new/', views.bookCreate, name='book_new'),
    path('edit/<int:pk>/', views.BookUpdate.as_view(), name='book_update'),
    path('delete/<int:pk>/', views.BookDelete.as_view(), name='book_delete'),
    path('search/', views.SearchView.as_view(), name='book_search'),
    path('about/', views.about, name='books_about'),
]
