from .models import Driver
from rest_framework import serializers as ser
from django.db.models import Min


#
# class RaceSerializer(ser.ModelSerializer):
#     best_time = ser.SerializerMethodField('_get_the_best_time')
#     class Meta:
#         model = Driver
#         fields = ('name', 'round_time','best_time')
#
#     def _get_the_best_time(self,obj):
#         dict_best = Driver.objects.aggregate(best_time=Min('round_time'))
#         return dict_best['best_time']

class RaceSerializer(ser.ModelSerializer):
    best_time = ser.SerializerMethodField('_get_the_best_time')
    best = 10000000  # random big int

    class Meta:
        model = Driver
        fields = ('name', 'round_time', 'best_time')

    def _get_the_best_time(self, obj):
        driver_time = getattr(obj, 'round_time')
        if obj.round_time and driver_time < self.best:
            self.best = driver_time
        return self.best

# UnboundLocalError: local variable 'best' referenced before assignment
# def _get_the_best_time(self, obj):
#     driver_time = getattr(obj, 'round_time')
#     if obj.round_time and driver_time < best:
#         best = driver_time
#     return best
