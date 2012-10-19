from __future__ import with_statement
from django.utils import unittest
from django.db import IntegrityError
from django.contrib.auth.models import User

from .models import Task


class TaskTest(unittest.TestCase):

    def setUp(self):
        self.user, created = User.objects.get_or_create(username='TestUser')
        self.task = Task.objects.create(user=self.user, name="Test Task 1")

    def testDisplay(self):
        self.assertEqual(str(self.task), "Test Task 1")

    def testBadCreation(self):
        with self.assertRaises(IntegrityError):
            Task.objects.create(name='Bad Test')
