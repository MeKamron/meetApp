from django.urls import path
from .views import *

urlpatterns = [
    path('questions/', QuestionList.as_view()),
    path('choices/', ChoiceList.as_view())
]
