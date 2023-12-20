from django.contrib import admin
from .models import Author, Book, BookInstance, Genre


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "last_name",
        "first_name",
    )
    list_filter = (
        "last_name",
        "first_name",
    )
    search_fields = (
        "last_name",
        "first_name",
    )


class BookInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    inlines = [BookInstanceInline]

    list_display = (
        "title",
        "display_genre",
        "author",
        "date_of_release",
    )
    list_filter = (
        "genre",
        "author",
    )
    search_fields = (
        "title",
        "genre",
        "author",
    )
    ordering = [
        "title",
    ]

    def display_genre(self, obj):
        return ",".join([genre.name for genre in obj.genre.all()])

    display_genre.short_description = "Genre"


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "book",
                    "imprint",
                )
            },
        ),
        (
            "Availability",
            {
                "fields": (
                    "status",
                    "due_back",
                ),
            },
        ),
    )

    list_display = (
        "book",
        "status",
        "borrower",
        "due_back",
    )
    list_filter = (
        "status",
        "due_back",
    )

    search_fields = (
        "book",
        "status",
    )
