from django.urls import path
from .views import *


urlpatterns = [   
    path('posts/', PostList.as_view()),
    path('posts/<int:pk>/', PostDetail.as_view()),
    path('posts/related/', related_post),
    # path('posts/search/', postSearch),
    path('categories/', CategoryList.as_view()),
    # path('categories/search/', categorySearch),
    path('subcategories/', SubCategoryList.as_view()),
    # path('subcategories/search/', subCategorySearch)
    path('comments/', CommentList.as_view()),
]