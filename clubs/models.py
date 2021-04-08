# import json
#
from django.db import models


# from django.core.serializers import serialize
# from users.models import User
class Cat(models.Model):
    name = models.CharField(max_length=100)


class Driver(models.Model):
    round_time = models.IntegerField()
    name = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    categ = models.ForeignKey(Cat,
                              null=True,
                              blank=True,
                              related_name='dr',
                              on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} made it in {self.round_time}'
"""
def get_categories():
...     filters = Q(dr__active=True)
...     return Cat.objects.annotate(foo=Count('dr', filters))
"""
#
#
# class TeamQuerySet(models.Manager):
#     def ser_whole_team(self):
#         """more efficient menthod to ser objects in qs"""
#         list_values = list(self.values('name','location','coach'))
#         # method json.dumps|=> list py dicts to json string
#         return json.dumps(list_values)

# def ser_whole_team(self):
#     """just for fun now you can work with py data extracted from json
#     but then again transform it into json"""
#     qs = self
#     final_arr = []
#     for obj in qs:
#         struct = json.loads(obj.serialize())
#         final_arr.append(struct)
# method json.dumps|=> list py dicts to json string
#     return json.dumps(final_arr)
# return serialize('json', qs, fields=('name', 'location', 'coach'))

#
# class TeamManager(models.Manager):
#     def get_queryset(self):
#         return TeamQuerySet(self.model, using=self._db)
#
#
# class Team(models.Model):
#     name = models.CharField(max_length=120)
#     location = models.CharField(max_length=120)
#     coach = models.ForeignKey(User, on_delete=models.CASCADE)
#
#     objects = TeamManager()
#
#     def __str__(self):
#         return f"{self.name} " \
#                f" coached by {self.coach}"
#
#     def ser_one_team(self):
#         json_data = serialize('json', self, fields=('name', 'location', 'coach'))
#         struct = json.loads(json_data)  # json |=> py dict (list with dict's)
#         print(struct)
#         data_json = json.dumps(struct[0]['fields'])
#         return data_json

class Country(models.Model):
    name = models.CharField(max_length=120)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'countries'

class City(models.Model):
    name = models.CharField(max_length=100)
    population = models.IntegerField()
    country = models.ForeignKey(Country,related_name='cities',on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.name} belongs to {self.country.name} has population {self.population}"
    class Meta:
        verbose_name_plural = 'cities'
