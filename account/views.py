
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from rest_framework.decorators import   api_view, renderer_classes
from rest_framework import schemas
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


# Django
from django.shortcuts import render
from django.contrib.auth.models import User


# Local

from account.models import Account
from account.serializer import RegistrationSerializer



class registration_view(viewsets.ModelViewSet):

    """ This Route implements User  """
    queryset = Account.objects.all()
    serializer_class = RegistrationSerializer
    
    def post(self, request):
        """ Allow registration of new users. """
        """ Adding a new task. """
        if request.method == 'POST':
            serializer = RegistrationSerializer(data=request.data)
        data= {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "Successfully registered a new user."
            data['email']=account.email
            data['username']=account.username
        else:
            data=serializer.errors
        return Response(data)

    # def put(self, request, todo_id):
    #     """ Update a todo """
    #     serializer = TodoSerializer(data=request.DATA)
    #     if not serializer.is_valid():
    #         return Response(serializer.errors, status=
    #             status.HTTP_400_BAD_REQUEST)
    #     else:
    #         data = serializer.data
    #         desc = data['description']
    #         done = data['done']
    #         t = Todo(id=todo_id, owner=request.user, description=desc,\
    #                  done=done, updated=datetime.now())
    #         t.save()
    #         return Response(status=status.HTTP_200_OK)



