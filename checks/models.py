from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class MySite(models.Model):
    """let op: dubble attr about time and status code with CheckSite: recent info here
    need more => go for Hx to CheckSite"""
    url = models.URLField(max_length=120)
    description = models.TextField(default="test")
    last_time_check = models.DateTimeField()
    last_resp = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return f'{self.url}: {self.last_resp}'


class CheckSite(models.Model):
    """let op: dubble attr about time and status code with Site: Hx here"""
    time = models.DateTimeField(auto_now_add=True)
    resp_code = models.CharField(max_length=10)
    site = models.ForeignKey(MySite,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return f'info {self.site.url} - {self.resp_code}'
