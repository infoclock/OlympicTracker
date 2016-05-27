from django.contrib import admin
#from django.utils.html import format_html_join
#from django.utils.safestring import mark_safe
#from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin
try:
    from django.utils.encoding import force_text
except ImportError:
    from django.utils.encoding import force_unicode as force_text

from .models import DemoUser, UserProfile
from .forms import DemoUserAdminForm


class UserProfileAdmin(admin.ModelAdmin):
    search_fields = ('user', 'dob')
    ordering = ('user',)
    list_select_related = ('user',)


admin.site.register(UserProfile, UserProfileAdmin)


class UserProfileAdminInline(admin.TabularInline):
    model = UserProfile


class DemoUserAdmin(UserAdmin):
    """The project uses a custom User model, so it uses a custom User admin model.

    Some related notes at:
    https://github.com/dabapps/django-email-as-username/blob/master/emailusernames/admin.py

    And:
    .../lib/python2.7/site-packages/django/contrib/auth/admin.py
    """

    inlines = [
        UserProfileAdminInline,
        ]

    #readonly_fields = ('private_uuid', 'public_id')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'display_name', 'codeforces_handle', 'problems_solved_first_exam', 'problems_solved_second_exam')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        #(_('Ids'), {'fields': ('private_uuid', 'public_id')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    list_display = ('email', 'first_name', 'last_name', 'display_name', 'is_staff')
    search_fields = ('first_name', 'last_name', 'display_name', 'email')
    ordering = ('email',)

    form = DemoUserAdminForm

admin.site.register(DemoUser, DemoUserAdmin)
