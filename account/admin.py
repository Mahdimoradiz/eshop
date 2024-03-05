from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . import models
from account.models import User
from . import forms



class UserAdmin(BaseUserAdmin):
      # The forms to add and change user instances
      form = forms.UserChangeForm
      add_form = forms.UserCreationForm

      # The fields to be used in displaying the User model.
      # These override the definitions on the base UserAdmin
      # that reference specific fields on auth.User.
      list_display = ["username", "email", "is_admin", "is_active"]
      list_filter = ["is_admin"]
      fieldsets = [
            (None, {"fields": ["username" ,"email", "password"]}),
            ("Personal info", {"fields": ["fullname", "first_name", "last_name"]}),
            ("Permissions", {"fields": ["is_admin", "is_active"]}),
      ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
      add_fieldsets = [
            (
            None,
                  {
                      "classes": ["wide"],
                      "fields": ["username", "email", "password1", "password2"],
                  },
            ),
      ]
      search_fields = ["email"]
      ordering = ["email"]
      filter_horizontal = []


# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
# register user profile

@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
      list_display = ["user" ,"picture", "join_date"]