from django.db import models
import re


class Message(models.Model):
    regex = None

    @classmethod
    def check(cls, line):
        obj = cls()
        for k,v in re.match(cls.regex, line).groupdict().items():
            obj.__setattr__(k, v)
        return obj


    class Meta:
        abstract = True
