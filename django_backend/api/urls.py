from django.urls import  path
from .views import TodoGetCreate,TodoUdpadeDelete
urlpatterns = [
    path('',TodoGetCreate.as_view()),
    path('<int:pk>',TodoUdpadeDelete.as_view())
]