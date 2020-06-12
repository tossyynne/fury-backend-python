
from rest_framework import viewsets
from task.serializer import TaskSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


from rest_framework.authentication import SessionAuthentication, BasicAuthentication



from task.models import Task

# Django
from django.shortcuts import render
from django.contrib.auth.models import User

# Task App
from task.serializer import  TaskSerializer
from task.models import Task

# Provider OAuth2

class TaskCreate(viewsets.ModelViewSet):
    """ This Route implements task  """
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    def get(self, request):
        """ Get all todos """
        todos = Task.objects.filter(owner=request.user.id)
        serializer = TaskSerializer(todos, many=True)
        return Response(serializer.data)
    def post(self, request):
        """ Adding a new task. """
        serializer = TaskSerializer(data=request.DATA)
        if not serializer.is_valid():
            return Response(serializer.errors, status=
                status.HTTP_400_BAD_REQUEST)
        else:
            data = serializer.data
            owner = request.user
            t = Task(owner=owner,description=data['description'], done=False,due_date=data['due_date'])
            t.save()
            request.DATA['id'] = t.pk # return id
            return Response(data, status=status.HTTP_201_CREATED)
    

