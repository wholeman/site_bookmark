from django.db import models


# Create your models here.
class Bookmark(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField('url', unique=True)

    def __str__(self):       # 해당 메서드 호출시 돌려주는 값
       return self.title