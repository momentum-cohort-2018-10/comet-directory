from django.contrib import admin
from core.models import LinkList, Link
from ordered_model.admin import OrderedTabularInline, OrderedInlineModelAdminMixin


class LinkTabularInline(OrderedTabularInline):
    model = Link
    fields = (
        'title',
        'url',
        'order',
        'move_up_down_links',
    )
    readonly_fields = (
        'order',
        'move_up_down_links',
    )
    extra = 1
    ordering = ('order', )


class LinkListAdmin(OrderedInlineModelAdminMixin, admin.ModelAdmin):
    list_display = ('title', )
    inlines = (LinkTabularInline, )


# Register your models here.
admin.site.register(LinkList, LinkListAdmin)
