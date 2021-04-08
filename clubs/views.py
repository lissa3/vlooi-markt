from .models import Driver
from .serializer import RaceSerializer
from rest_framework import generics


class ShowRace(generics.ListAPIView):
    serializer_class = RaceSerializer
    queryset = Driver.objects.all()

    # def get_queryset(self):
    #
    #     dict_best = Driver.objects.aggregate(best_time=Min('round_time'))
    #     print("dict best:",dict_best)
    #     drivers = Driver.objects.all().annotate(best=Min('round_time'))
    #     for item in drivers:
    #         if hasattr(item,'best'):
    #             print(hasattr(item,'best'))
    #             print(getattr(item,'best'))
    #         else:
    #             print("no best found")
    #     queryset = Driver.objects.all()
    #     return queryset


