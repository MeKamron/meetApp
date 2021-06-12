from django.urls import path
from .views import *


urlpatterns = [   
    path('posts/', PostList.as_view()),
    path('posts/<int:pk>/', PostDetail.as_view()),
    path('posts/related/<int:user_id>/', mixed_posts),
    # path('posts/search/', postSearch),
    path('categories/', CategoryList.as_view()),
    # path('categories/search/', categorySearch),
    path('subcategories/', SubCategoryList.as_view()),
    # path('subcategories/search/', subCategorySearch)
    path('comments/', CommentList.as_view()),
    path('comments/<int:pk>/', CommentDetail.as_view()),
    path('categories/<int:pk>/', CategoryDetail.as_view()),
    path('recommendations/<int:user_id>/', recommendations),
]