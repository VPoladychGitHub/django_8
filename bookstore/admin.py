from django.utils import timezone

from django.contrib import admin
from django.core.checks import messages
from django.utils.translation import ngettext
from django.contrib import messages

from bookstore.models import BookInstance


class BookInstanceAddAdmin(admin.ModelAdmin):
    list_display = ['book', 'status', 'timestamp']
    ordering = ['timestamp']
    actions = ['make_ordered']

    def make_ordered(self, request, queryset):
        updated = queryset.update(status=BookInstance.BookStatus.ORDERED)
        self.message_user(request, ngettext(
            '%d ook Status was successfully marked as ORDERED.',
            '%d ook Status were successfully marked as ORDERED.',
            updated,
        ) % updated, messages.SUCCESS)

    make_ordered.short_description = "Mark selected Book Status as ORDERED"


admin.site.register(BookInstance,BookInstanceAddAdmin)

