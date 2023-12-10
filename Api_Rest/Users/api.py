from Users.models import proyect
from rest_framework import viewsets , permissions
from .serializer import ProjectSerializer
class ProjectViewSet(viewsets.ModelViewSet): # aqui digo que consulats se pueden hacer
   queryset=proyect.objects.all()
   permission_classes=[permissions.AllowAny]
   serializer_class=ProjectSerializer