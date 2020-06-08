from graphene_django.types import DjangoObjectType
from main.models import Task
from django.contrib.auth.models import User

class TaskType(DjangoObjectType):
    class Meta:
        model = Task
        fields = ('id', 'assigned_to', 'title', 'description', 'status', 'created_on')

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'task')