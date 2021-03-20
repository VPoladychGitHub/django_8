import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class BookInstance(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""

    class BookStatus(models.IntegerChoices):
        AVAILABLE = 1, _("Available")  # a
        ORDERED = 2, _("Ordered")  # o

    id = models.UUIDField(  # noqa: A003
        primary_key=True, default=uuid.uuid4, help_text=_("Unique ID for this particular book across whole library")
    )
    owner = models.ForeignKey('auth.User', related_name='bookstore', on_delete=models.CASCADE)
    book = models.ForeignKey("Book", on_delete=models.SET_NULL, null=True)

    # comment_status = models.PositiveSmallIntegerField(choices=CommentStatus.choices, default=1)
    status = models.PositiveSmallIntegerField(choices=BookStatus.choices, default=1)
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['timestamp']


class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(_("title"), max_length=200)
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in file.
    summary = models.TextField(_("summary"), max_length=1000, help_text=_("Enter a brief description of the book"))
    isbn = models.CharField(_("ISBN"), max_length=13, help_text=_("13 character ISBN number"))
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['title', 'author']

    def __str__(self):
        """String for representing the Model object."""
        return self.title


class Author(models.Model):
    """Model representing an author."""
 #   owner = models.ForeignKey('auth.User', related_name='bookstore', on_delete=models.CASCADE)
    first_name = models.CharField(_("first name"), max_length=100)
    last_name = models.CharField(_("last name"), max_length=100)
    date_of_birth = models.DateField(_("date of birth"), null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        """String for representing the Model object."""
        return f"{self.last_name}, {self.first_name}"
