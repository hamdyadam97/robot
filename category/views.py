from rest_framework import generics, status, permissions,filters
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response

from category.models import Category, Post
from category.serializer import CategorySerializer, PostSerializer
from django_filters.rest_framework import DjangoFilterBackend


class TheCategory(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name','the_type']


class ThePost(CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def perform_create(self, serializer):
        return serializer.save()


class PostUpdateView(RetrieveUpdateAPIView):
    serializer_class = PostSerializer

    permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    print(queryset)
    lookup_field = "id"



class SearchPostView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category']
    search_fields = ['title','description']