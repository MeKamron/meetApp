from rest_framework import generics, permissions
from .models import Question, Choice
from .serializers import QuestionSerializer, ChoiceSerializer
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from .permissions import IsSuperUserOrReadOnly
from rest_framework.authentication import TokenAuthentication
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsSuperUserOrReadOnly]
    authentication_classes = [TokenAuthentication]

class ChoiceList(generics.ListAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


# class ChoiceDetail(generics.RetrieveUpdateAPIView):
#     queryset = Choice.objects.all()
#     serializer_class = ChoiceSerializer
#     permission_classes = [permissions.IsAuthenticated]


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def vote(request):
    if request.method == 'POST':
        choices = Choice.objects.all()
        serializers = ChoiceSerializer(choices, many=True)
        id = request.data.get('id')
        choice = Choice.objects.get(id=id)
        choice.votes += 1
        choice.save()
        return Response(serializers.data)

 