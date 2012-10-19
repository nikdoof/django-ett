from tastypie.resources import ModelResource
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import Authorization
from tastypie.api import Api

from .models import Task


class EtasksAuthorization(Authorization):

    def apply_limits(self, request, object_list):

        if request and hasattr(request, 'user'):
            return object_list.filter(user__pk=request.user.pk)

        return object_list.none()


class TaskResource(ModelResource):

    class Meta:
        queryset = Task.objects.all()
        resource_name = 'task'

        authentication = ApiKeyAuthentication()
        authorization = EtasksAuthorization()


v1_api = Api(api_name='1.0')
v1_api.register(TaskResource())
