from __future__ import with_statement
from django.test import TestCase
from django.db import IntegrityError
from django.contrib.auth.models import User

from .models import Task


class TaskTest(TestCase):

    def setUp(self):
        self.user, created = User.objects.get_or_create(username='TestUser')
        self.task = Task.objects.create(user=self.user, name="Test Task 1")

    def testDisplay(self):
        self.assertEqual(str(self.task), "Test Task 1")
        self.task.name = ''
        self.assertEqual(str(self.task), "Unknown")

    def testBadCreation(self):
        with self.assertRaises(IntegrityError):
            Task.objects.create(name='Bad Test')


class TaskDetailViewTest(TestCase):

    def setUp(self):
        self.user, created = User.objects.get_or_create(username='TestUser')
        self.task = Task.objects.create(user=self.user, name="Test Task 2")        

    def testBasicResponse(self):
        resp = self.client.get('/task/%d/' % self.task.pk)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('object' in resp.context)
