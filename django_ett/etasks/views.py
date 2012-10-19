from django.views.generic import DetailView
from .models import Task


class TaskDetailView(DetailView):

    model = Task