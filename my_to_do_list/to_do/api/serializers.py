from rest_framework.serializers import ModelSerializer
from to_do.models import Task


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        
#for the fields, you can make a list of what you want to return instead of returning all, for example
# fields = ['id', 'firstname', 'lastname', 'language']