from django.contrib import admin
from links.models import *

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    list_display = ('target_url', 'description', 'identifier',
                    'author', 'created_date', 'active',)
    list_per_page = 30
admin.site.register(Link,LinkAdmin)





