from django.urls import path, include
from .views import *
app_name = 'category'
urlpatterns = [
    path('post/makeorder', ProductOrderUpdateView.as_view(), name="order"),
    path('post/categories',TheCategory.as_view(), name='thecategory'),
    path('post/',TheProduct.as_view(), name='thepost'),
    path('post/<int:id>', ProductUpdateView.as_view(), name="postupdate"),
    path('post/get', SearchPostView.as_view(), name="search"),
    path('post/product', TheProductlist.as_view(), name="listproduct"),

]
