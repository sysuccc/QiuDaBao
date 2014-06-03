#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AccountInfo(models.Model):
  user    = models.ForeignKey(User)
  balance = models.IntegerField()

DISH_NAME_MAX_LENGTH = 20

class Order(models.Model):
  offerer     = models.ForeignKey(User, related_name='offerer_order')
  submiter    = models.ForeignKey(User, related_name='submiter_order', null=True, blank=True)
  dish        = models.CharField(max_length=DISH_NAME_MAX_LENGTH)
  description = models.TextField(blank=True)
  place       = models.TextField()
