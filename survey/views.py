from rest_framework import generics, permissions
from .models import Question, Choice
from accounts.models import Profile
from .serializers import QuestionSerializer, ChoiceSerializer
from blog.permissions import IsVerifiedOrReadOnly, IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAdminUser]

class ChoiceList(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = [permissions.IsAuthenticated]


