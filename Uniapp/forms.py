import form
from django.forms import Form, ModelForm
from django.db import models

from Uniapp.models import *


class Fan_form(form.ModelForm):
    class Meta:
        model = Fan
        fields = "__all__"


class Yonalish_form(form.ModelForm):
    class Meta:
        model = Yonalish
        fields = "__all__"
