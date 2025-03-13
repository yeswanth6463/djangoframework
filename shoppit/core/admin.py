from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customer

# Register your models here.
class customeradmin(UserAdmin):
    add_fields=(
        (None,{
            'classes':('wide',),
            'fields':('username',
              'email',
              'first_name',
              'last_name',
              'password1',
              'password2',
              'city',
              'state',
              'address'
                      )
        }),
    )
    
admin.site.register(Customer,customeradmin)