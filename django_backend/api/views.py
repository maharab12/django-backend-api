from rest_framework import generics
from .models import Todo
from .serilaizer import TodoSerilaizer

class TodoGetCreate(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerilaizer

class TodoUdpadeDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerilaizer