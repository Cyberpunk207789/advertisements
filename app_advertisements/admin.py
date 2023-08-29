from django.contrib import admin
from .models import Advertisement

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'auction', 'created_date']
    list_filter = ['auction', 'created_at']

    actions = ['disable_auctions', 'enable_auctions']

    @admin.action(description='Убрать возможность торга')
    def disable_auctions (self, request, queryset):
        queryset.update(auction = False)

    @admin.action(description='Вернуть возможность торга')
    def enable_auctions (self, request, queryset):
        queryset.update(auction = True)

    fieldsets = (
        ('Общее', 
            {
            'fields': ('title', 'description'),
            }
        ),

        ('Финансы',
            {
            'fields': ('price', 'auction'),
            'classes': ['collapse']
            }
        )
    )


admin.site.register(Advertisement, AdvertisementAdmin)
# Register your models here.
