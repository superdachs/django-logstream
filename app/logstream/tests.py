from django.db import models
from django.test import TestCase

from .models import Message


class TestModel(Message):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    sex = models.CharField(max_length=1, choices=(('male', 'm'), ('female', 'f'), ('other', 'o')))

    regex = r'(?P<name>\w+),(?P<age>\d+),(?P<sex>\w)'

    class Meta:
        abstract = True


class BaseTests(TestCase):

    def test_matching(self):
        obj = TestModel.check('bla,99,o')
        assert obj.name == 'bla'
        assert obj.age == '99'
        assert obj.sex == 'o'
