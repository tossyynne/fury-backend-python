
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from rest_framework.authentication import SessionAuthentication, BasicAuthentication

# Django
from django.shortcuts import render
from django.contrib.auth.models import User

# Documentation App
from documentation.serializer import DocumentationSerializer
from documentation.models import Documentation

# Provider OAuth2



from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from rest_framework.decorators import   api_view, renderer_classes
from rest_framework import schemas





class Documentation_view(viewsets.ModelViewSet):
    """ This Route implements Documentation  """
    queryset = Documentation.objects.all()
    serializer_class = DocumentationSerializer
    
    def post(self, request):
        """ Allow registration of new users. """
        """ Adding a new task. """
        if request.method == 'POST':
            serializer = DocumentationSerializer(data=request.data)
        data= {}
        if serializer.is_valid():
            document = serializer.save()
            data['pathname'] = "Successfully registered a new user."
            data['action_name']=document.action_name
            data['route']=document.route
        else:
            data=serializer.errors
        return Response(data)



