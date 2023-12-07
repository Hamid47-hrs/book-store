import uuid
from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Enter the book genre.")

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField(
        max_length=1000, help_text="Enter a brief description of the book."
    )
    isbn = models.CharField(max_length=13, help_text="13 character ISBN.", name="ISBN")

    # * ManyToManyField used because 'genre' can contain many books and 'book' can cover many genres.
    genre = models.ManyToManyField(Genre, help_text="Select a genre for the book.")
    date_of_release = models.DateField()

    # * ForeignKey is used because 'book' can only have ONE author but an 'author' can have multiple books.
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class BookInstance(models.Model):
    LOAN_STATUS = (
        ("m", "Maintenance"),
        ("o", "On Loan"),
        ("a", "Available"),
        ("r", "Reserved"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    book = models.ForeignKey("Book", on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=1, choices=LOAN_STATUS, default="m", help_text="Book availability."
    )

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        return f"{self.book.title} - ({self.id})" # type: ignore
