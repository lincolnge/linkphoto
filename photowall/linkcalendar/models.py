# coding:utf8
from django.db import models

# Create your models here.

class Calendar(models.Model):
    title = models.CharField(max_length=30)
    cal_type = models.CharField(max_length=30, blank=True)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    allDay = models.BooleanField(blank=True)
    url = models.URLField(blank=True)

    def __unicode__(self):
        return self.title

    # 按照起始时间排序
    class Meta:
        ordering = ['start']
