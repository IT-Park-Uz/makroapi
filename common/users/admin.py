from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

User = get_user_model()

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "name", "is_superuser"]
    search_fields = ['name', "username"]

    save_on_top = True
    save_as = True

    def save_model(self, request, obj, form, change):
        if len(str(obj.password)) < 20:
            obj.set_password(obj.password)
        super(UserAdmin, self).save_model(request, obj, form, change)
