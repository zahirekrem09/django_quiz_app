from django.shortcuts import render
from rest_framework import generics
from .models import Category, Quiz
from .serializers import CategorySerializer, CategoryDetailSerializer


class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryDetailList(generics.ListAPIView):
    serializer_class = CategoryDetailSerializer

    def get_queryset(self):
        queryset = Quiz.objects.all()
        category = self.kwargs['category']
        queryset = queryset.filter(category__name=category)
        return queryset
