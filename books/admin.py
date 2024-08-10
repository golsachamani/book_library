from django.contrib import admin

from . models import Genre, Book, Author
admin.site.register(Author)
admin.site.register(Genre)
@admin.display(description='genre')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published_at','get_genres' ]

    def get_genres(self, obj,):
            return [genre.name for genre in obj.genre.all()]
    get_genres.short_description ='genres'