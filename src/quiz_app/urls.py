from django.contrib import admin
from django.urls import path, include

from .views import CategoryList, CategoryDetailList, QuizDetail

urlpatterns = [
    path('', CategoryList.as_view(), name='category'),
    path('<category>', CategoryDetailList.as_view(), name='category-detail'),
    path('question/<title>', QuizDetail.as_view(), name='quiz-detail'),

]
