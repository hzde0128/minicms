#!/usr/bin/env python
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2017 All rights reserved.
#
#   Author        : jerry
#   Email         : hzde0128@gmail.com
#   File Name     : urls.py
#   Last Modified : 2017-03-17 22:03
#   Describe      :
#
#   Log           :
#
# ====================================================

from django.conf.urls import url
from . import views

urlpatterns = [
		url(r'^$', views.index, name='index')
		]
