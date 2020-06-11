
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
from task.serializer import RegistrationSerializer
from task.serializer import UserSerializer, TaskSerializer
from task.models import Task

# Provider OAuth2

class TaskCreate(viewsets.ModelViewSet):

    """ This view implements create task  """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    def get(self, request):
        """ Get all todos """
        todos = Todo.objects.filter(owner=request.user.id)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
    def post(self, request):
        """ Allow registration of new users. """
        """ Adding a new task. """
        serializer = TaskSerializer(data=request.DATA)
        if not serializer.is_valid():
            return Response(serializer.errors, status=
                status.HTTP_400_BAD_REQUEST)
        else:
            data = serializer.data
            # owner = request.user
            t = Task(description=data['description'], done=False)
            t.save()
            # request.DATA['id'] = t.pk # return id
            return Response(data, status=status.HTTP_201_CREATED)
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



# class RegistrationView(APIView):
#     """ Allow registration of new users. """
#     permission_classes = ()

#     def post(self, request):
#         serializer = RegistrationSerializer(data=request.DATA)

#         # Check format and unique constraint
#         if not serializer.is_valid():
#             return Response(serializer.errors,\
#                             status=status.HTTP_400_BAD_REQUEST)
#         data = serializer.data

#         u = User.objects.create(username=data['username'])
#         u.set_password(data['password'])
#         u.save()

#         # Create OAuth2 client
#         name = u.username
#         client = Client(user=u, name=name, url='' + name,\
#                 client_id=name, client_secret='', client_type=1)
#         client.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

