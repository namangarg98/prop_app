from django.contrib import admin
from .models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email',
                    'hire_date', 'photo')

    list_display_links = ('id', 'name')  # so that we can click on them
    list_filter = ('hire_date',)
    # list_editable = ('is_published', )
    search_fields = ('name',)
    list_per_page = 25


admin.site.register(Realtor, RealtorAdmin)
