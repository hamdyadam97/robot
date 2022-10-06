from rest_framework import generics, status, permissions,filters
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response

from category.models import Category, Post
from category.serializer import CategorySerializer, PostSerializer
from django_filters.rest_framework import DjangoFilterBackend


class TheCategory(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name','the_type']


class ThePost(ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        print(self.category)
        return self.queryset.filter(category=self.category)


class PostUpdateView(RetrieveUpdateAPIView):
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    lookup_field = "id"

    # def get_queryset(self):
    #     return self.queryset.filter(category=self.category)


class SearchPostView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category']
    search_fields = ['title','description']