from django.contrib import admin
from .models import User, Movie, Cast
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Register your models here.
class UserModelAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('id', 'email', 'username', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        ('User Credentials', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    # add_fieldsets is not a standard ModelAdmin attribute. UserModelAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email', 'id')
    filter_horizontal = ()


# Register the new UserModelAdmin...
admin.site.register(User, UserModelAdmin)

# Register the new MovieModelAdmin...
@admin.register(Movie)
class MovieAdminModel(admin.ModelAdmin):
    list_display = ['movie_id', 'title', 'created_at', 'updated_at', 'runtime', 'language', 'tagline']


# Register the new CastModelAdmin...
@admin.register(Cast)
class CastAdminMovie(admin.ModelAdmin):
    list_display = ['cast_id', 'name', 'gender', 'dob']
