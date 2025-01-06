from django.urls import path
from .views.news_view import (NewListView,
                              NewDetailView)



urlpatterns = [
    path('news_list', NewListView.as_view()),
    path('news/<int:id>', NewDetailView.as_view())
]