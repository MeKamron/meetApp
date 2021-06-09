from rest_framework import generics, permissions
from .models import Question, Choice
from accounts.models import Profile
from .serializers import QuestionSerializer, ChoiceSerializer
from blog.permissions import IsVerifiedOrReadOnly, IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .permissions import IsSuperUserOrReadOnly
from rest_framework.decorators import api_view

class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsSuperUserOrReadOnly]

class ChoiceList(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = [permissions.IsAuthenticated]


# class ChoiceDetail(generics.RetrieveUpdateAPIView):
#     queryset = Choice.objects.all()
#     serializer_class = ChoiceSerializer
#     permission_classes = [permissions.IsAuthenticated]


@api_view(['POST'])
def vote(request):
    if request.method == 'POST':
        choices = Choice.objects.all()
        serializers = ChoiceSerializer(choices, many=True)
        id = request.data.get('id')
        choice = Choice.objects.get(id=id)
        choice.votes += 1
        choice.save()
        return Response(serializers.data)