#Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.db.models import fields

#Models
from users.models import Profile
from django.contrib.auth.models import User

@admin.register(Profile)
class Profileadmin(admin.ModelAdmin):
    list_display = ('pk','user', 'phone_number', 'website', 'picture',)
    list_display_links = ('user', 'phone_number', 'picture')
    list_editable = ('website',)
    search_fields = (
        'user__username',
        'user__email', 
        'user__first_name', 
        'user__last_name', 
        'phone_number'
        )
    list_filter = (
        'created',
        'modified',
        'user__is_active',
        'user__is_staff',
    )

    fieldsets = (
        ('Profile', {
            'fields': (('user', 'picture'),),

        }),
        ('Extra info', {
            'fields': (('phone_number', 'website'),
                        'biography')
        }),
        ('Metadata', {
            'fields': ('created', 'modified')
        })
    )

    readonly_fields = ('created', 'modified', 'user')


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)