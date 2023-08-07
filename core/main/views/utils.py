
'''

    In This Python File You Find All Necessary Modules And Packages

'''

# Django Typing for Views `get_context_data``
from typing import Any, Dict
# Django Views
from django.views.generic import ListView , DetailView , CreateView
# Django JSON For Ajax
from django.http import JsonResponse
# Django Serializer For JSON Response In AJAX Handling
from django.core import serializers
# Django All Models
from main.models import *
# Django Current Project Forms
from ..forms.forms import NewsletterForm , MessageForm
# Django For Email Send
from django.core.mail import EmailMessage
# Django Reverse URL
from django.urls import reverse_lazy
# Django Mixin
from .mixin import DataMixin
# Django Pagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Django Render Function For 404 Page
from django.shortcuts import render
from django.contrib import messages