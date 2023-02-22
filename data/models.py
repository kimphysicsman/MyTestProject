from django.db import models

# Create your models here.


class Data(models.Model):
    data_no = models.IntegerField("데이터 번호")
    name = models.CharField("데이터 이름", max_length=100)
