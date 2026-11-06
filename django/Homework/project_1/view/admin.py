from django.contrib import admin
from view.models import Student

# Register your models here.

class Studentadmin(admin.ModelAdmin):
    list_display = ["id","firstname","lastname","email","password","course",
                    "department","guardian","contact"]
    search_fields = ["id","firstname","lastname","email","password","course",
                    "department","guardian","contact"]
    list_editable = ["firstname","lastname","password",
                    "guardian","contact"]
    list_filter = ["firstname","lastname","course",
                    "department"]
    list_display_links = ["email"]
    


admin.site.register(Student,Studentadmin)