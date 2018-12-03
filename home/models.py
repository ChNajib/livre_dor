# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.contrib.auth.models import Permission, User
from django.db import models


class Message(models.Model):
    user = models.ForeignKey(User, default=1)
    title = models.CharField(max_length=250)
    content = models.CharField(max_length=1000)
    date = models.CharField(max_length=1000,default= datetime.date.today())
    def __str__(self):
        return self.title

