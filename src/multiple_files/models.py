# models.py
import random
import string
import os

from django.db import models
from django.utils.timezone import now as timezone_now


def create_random_string(length=30):
    if length <= 0:
        length = 30

    symbols = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join([random.choice(symbols) for x in range(length)])


def upload_to(instance, filename):
    now = timezone_now()
    filename_base, filename_ext = os.path.splitext(filename)
    return 'my_uploads/{}_{}{}'.format(
        now.strftime("%Y/%m/%d/%Y%m%d%H%M%S"),
        create_random_string(),
        filename_ext.lower()
    )

# your object of form here
class Object(models.Model):
    name = models.CharField(max_length=18)
    description = models.CharField(max_length=100)
    # other yout fields here

class Attachment(models.Model):
    object = models.ForeignKey(Object, on_delete=models.CASCADE, null=True)
    attachment = models.FileField(upload_to=upload_to)
    

