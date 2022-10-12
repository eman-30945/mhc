from django.contrib import admin
from .models import *

# Register your models here.

# admin.site.register(Section_Options)
admin.site.register(Employee_form)
admin.site.register(Departments)
admin.site.register(Administrator)
admin.site.register(Nursing)
admin.site.register(Doctor)

#def change_button(self, obj):
  #  return format_html('<a class="btn" href="/admin/em/Departments/{}/change/">Change</a>', obj.id)

#def delete_button(self, obj):
 #   return format_html('<a class="btn" href="/admin/em/Department/{}/delete/">Delete</a>', obj.id)

#list_display = ('__str__', 'change_button', 'delete_button')