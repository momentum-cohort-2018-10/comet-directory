from django.db import models
from ordered_model.models import OrderedModel


class LinkList(models.Model):
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(
        to='auth.User', on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Link(OrderedModel):
    list = models.ForeignKey(to=LinkList, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url = models.URLField()
    order_with_respect_to = 'list'

    class Meta(OrderedModel.Meta):
        ordering = (
            'list',
            'order',
        )

    def __str__(self):
        return self.title
