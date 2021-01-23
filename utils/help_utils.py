import os
import random
import string

from django.utils import timezone


def make_random(size=8, chars=(string.ascii_uppercase + string.digits)):
    """
    return string made of random ascii-chars and digits
    :param siz:
    :param chars:
    :return:
    """
    output = [random.choice(chars) for _ in range(size)]
    return "".join(output)


def create_instance_unid(instance):
    """
    create unique id for instanc based on random letters and digits
    :param instance:
    :return:
    """
    klass = instance.__class__
    start_unid = make_random()
    if klass.objects.filter(unid=start_unid).exists():
        instance.unid = make_random()
        return create_instance_unid(instance)
    return start_unid


def upload_to(instance, filename):
    """ save uploaded file into media folder
    initial file name changed for the following format:
    media/user/user_id/year-month-day-hour-seconds-milliseconds.extention
    """
    now = timezone.now()
    base, extension = os.path.splitext(filename.lower())
    timestamp = timezone.now().strftime("%Y-%m-%d-%H%M%S")
    milliseconds = now.microsecond // 1000
    return f"user/{instance.pk}/{timestamp}-{milliseconds}{extension}"
