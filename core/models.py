from django.db import models


class LinkList(models.Model):
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(
        to='auth.User', on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True, blank=True)


class Link(models.Model):
    list = models.ForeignKey(to=LinkList, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url = models.URLField()
