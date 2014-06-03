#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

class UserRegisterForm(forms.Form):
  username = forms.CharField(max_length=100)
  password = forms.CharField(widget=forms.PasswordInput)
