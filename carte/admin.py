# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import *

admin.site.register(Restaurant)
admin.site.register(Hotel)
admin.site.register(Rate_Review)