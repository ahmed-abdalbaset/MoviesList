from django.contrib import admin

# Register your models here.
from .models import Movies_Info, Publisher, Contributor,MovieContributor, Review
admin.site.register(Movies_Info)
admin.site.register(Publisher)
admin.site.register(Contributor)
admin.site.register(MovieContributor)
admin.site.register(Review)
