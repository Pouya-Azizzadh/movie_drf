from django.contrib import admin
from .models import Movie,Genre,ListMovie,Comment
# Register your models here.
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(ListMovie)
admin.site.register(Comment)


