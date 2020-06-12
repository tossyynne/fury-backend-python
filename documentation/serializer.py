from rest_framework import serializers
from django.utils import timezone
from django.contrib.auth.models import User
from documentation.models import Documentation
class DocumentationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Documentation
        fields= ('path_name','action_name','route','curl')
