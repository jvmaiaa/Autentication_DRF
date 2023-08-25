from rest_framework import viewsets
from .models import Livro, Profile
from .serializers import LivroSerializer, ProfileSerializer

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer



