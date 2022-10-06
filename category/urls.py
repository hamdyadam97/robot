from django.urls import path, include
from .views import *
app_name = 'category'
urlpatterns = [
    path('thecategory',TheCategory.as_view(), name='thecategory'),
    path('createpost',ThePost.as_view(), name='thepost'),
    path('update/<int:id>', PostUpdateView.as_view(), name="postupdate"),
    path('search', SearchPostView.as_view(), name="search"),
]
