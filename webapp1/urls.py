from django.urls import path
# from .views import BookListView
from . import views
urlpatterns = [
    # path('', BookListView.as_view(), name='book-list'),
    path('', views.index, name='index'),
]