from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import api_views, views


router = DefaultRouter()
router.register(r'books', api_views.BookViewSet)
router.register(r'reviews', api_views.ReviewViewSet)


urlpatterns = [
    path('', views.home, name='home'),
    path('book_list/', views.book_list, name='book_list'),
    path('books/<int:id>', views.book_detail, name='book_detail'),
    path('books/<int:book_pk>/reviews/new/', views.review_edit, name='review_create'),
    path('books/<int:book_pk>/reviews/<int:review_pk>/', views.review_edit, name='review_edit'),
    path('books/<int:pk>/media/', views.book_media, name='book_media'),
    path('book_search/', views.book_search, name='book_search'),
    path('publishers/<int:pk>/', views.publisher_edit, name='publisher_edit'),
    path('publishers/new/', views.publisher_edit, name='publisher_create'),

    # APIs
    path('api/', include((router.urls, 'api'))),
    path('api/login/', api_views.Login.as_view(), name='api_login'),
]