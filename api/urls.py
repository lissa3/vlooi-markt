from django.urls import path
from rest_framework import routers
from .viewsets import BookViewset


router = routers.DefaultRouter()
router.register('books', BookViewset)
urlpatterns = []
urlpatterns += router.urls
