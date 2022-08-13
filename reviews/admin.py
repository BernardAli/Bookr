from django.contrib import admin
from .models import *


class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'publication_date'
    list_display = ('title', 'isbn13')
    list_filter = ('publisher__name', 'publication_date')
    search_fields = ('title', 'isbn', 'publisher__name')


admin.site.register(Book, BookAdmin)

admin.site.register(Review)
admin.site.register(Publisher)
admin.site.register(Contributor)
admin.site.register(BookContributor)
