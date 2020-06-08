import graphene
from .typeDef import TaskType, UserType
from main.models import Task
from django.core.exceptions import ObjectDoesNotExist

class Query:
    all_tasks = graphene.List(TaskType)
    task = graphene.Field(TaskType, id=graphene.ID())
    all_users = graphene.List(UserType)
    user = graphene.Field(UserType, id=graphene.Int())

    def resolve_all_tasks(self, info, **kwargs):
  	    return Task.objects.all()

    def resolve_task(self, info, **kwargs):
        try:
       		return Task.objects.get(pk=kwargs.get('id'))
        except ObjectDoesNotExist:
       		return None

    def resolve_all_users(self, info, **kwargs):
    	return User.objects.all()
       
    def resolve_user(self, info, **kwargs):
        try:
       		return User.objects.get(pk=kwargs.get('id'))
        except ObjectDoesNotExist:
       		return None         