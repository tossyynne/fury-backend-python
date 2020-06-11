from rest_framework import serializers
from task.models import Task
from django.utils import timezone
from django.contrib.auth.models import User
from account.models import Account
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('username','email', 'password')

