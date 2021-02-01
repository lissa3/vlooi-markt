from proj_help.help_utils import create_instance_unid
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Book


# before profile get saved in db |==> create unid
@receiver(pre_save, sender=Book)
def add_unid_to_book(sender, instance, **kwargs):
    if not instance.unid:
        instance.unid = create_instance_unid(instance)
