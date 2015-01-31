# coding:utf8
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CalType(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=30, blank=True)

    def __unicode__(self):
        return unicode(self.name)


class EventName(models.Model):
    # user 其实不能为空, 在保存的时候, 一定会加数值, 这里只是为了 hack
    user = models.ForeignKey(User, null=True, blank=True)
    name = models.CharField(max_length=30)
    cal_type = models.ForeignKey(CalType)
    counts = models.IntegerField(blank=True)
    url = models.URLField(blank=True)

    # 为了解决 'EventName' object has no attribute '__getitem__'
    def __unicode__(self):
        return unicode(self.name)


class Calendar(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    title = models.ForeignKey(EventName)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    allDay = models.BooleanField(blank=True)

    def __unicode__(self):
        return unicode(self.title)

    # 按照起始时间排序
    class Meta:
        ordering = ['start']
