from django.urls import path, include
from .views import *
app_name = 'category'
urlpatterns = [
    path('post/categories',TheCategory.as_view(), name='thecategory'),
    path('post/',ThePost.as_view(), name='thepost'),
    path('post/<int:id>', PostUpdateView.as_view(), name="postupdate"),
    path('post/get', SearchPostView.as_view(), name="search"),
]
