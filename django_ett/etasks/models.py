from django.db import models
from django.contrib.auth.models import User
from tastypie.models import create_api_key


# Connect the tastypie API key creation call
models.signals.post_save.connect(create_api_key, sender=User)


class Task(models.Model):
    """
    Represents a user's task entry that time can be allocated to
    """

    user = models.ForeignKey(User, related_name='tasks')
    name = models.CharField('Task Name', max_length=200, blank=False)
    archived = models.BooleanField('Archived?', default=False)
    created = models.DateTimeField('Created Date/Time', auto_now_add=True)

    @property
    def total_time(self):
        entries = self.entries.filter(type=TimeEntry.TYPE_ON).count()
        if entries:
            return entries * 15
        return 0

    def __unicode__(self):
        if self.name:
            return self.name
        return u'Unknown'


class TimeEntry(models.Model):
    """
    A entry of time against a task
    """

    TYPE_OFF = 1
    TYPE_ON = 2
    TYPE_STRIKE = 3

    TYPE_CHOICES = (
        (TYPE_OFF, 'Off'),
        (TYPE_ON, 'On'),
        (TYPE_STRIKE, 'Strike'),
    )

    task = models.ForeignKey(Task, related_name='entries')
    type = models.IntegerField('Type', choices=TYPE_CHOICES, default=TYPE_OFF)
    date = models.DateField('Date')
    segment = models.IntegerField('Segment')

    created = models.DateTimeField('Created Date/Time', auto_now_add=True)
    updated = models.DateTimeField('Updated Date/Time', auto_now=True)

    def get_segment_time(self):
        if self.segment > 0:
            return self.segment * 15
        return 0

    def __unicode__(self):
        return u'%s - %s %s' % (self.task.name, self.date,
                                self.get_segment_time())
