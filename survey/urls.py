from django.urls import path
from .views import *

urlpatterns = [
    path('questions/', QuestionList.as_view()),
    path('choices/', ChoiceList.as_view()),
    # path('choices/<int:pk>/', ChoiceDetail.as_view()),
    path('choices/vote/', vote)
]
