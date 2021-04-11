from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand, CommandError
from checks.models import MySite, CheckSite

import requests
from django.utils import timezone

lst = ['https://www.houseofmydream.nl', 'https://www.memoryoverflow.nl']


class Command(BaseCommand):
    help = "check status for my sites"

    def handle(self, *args, **kwargs):
        for site in MySite.objects.all():
            resp = requests.head(site.url)
            site.last_resp = str(resp.status_code)
            site.last_time_check = timezone.now()
            self.stdout.write(self.style.SUCCESS(f"Done,status is  {resp.status_code}"))
            try:
                site.save()
            except Exception as err:
                self.stdout.write(self.style.ERROR(f"ERROR UPDATE site = {site}: {err}"))

            try:
                obj_check_site = CheckSite(resp_code=resp.status_code, site=site)
                obj_check_site.save()
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"ERROR:  {resp.status_code}"))
                raise CommandError(f'error adding check: {e}.')


