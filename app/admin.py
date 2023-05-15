from django.contrib.admin import *
from .models import *


@register(Project)
class ProjectAdmin(ModelAdmin):
	list_display = ('id', 'project_title', 'github_link')
	list_display_links = ('id', 'project_title')


@register(Staff)
class StaffAdmin(ModelAdmin):
	list_display = ('id', 'first_name', 'last_name', 'field')
	list_display_links = ('id', 'first_name', 'last_name')
	ordering = ('id', 'field')


@register(Field)
class FieldAdmin(ModelAdmin):
	list_display = ('id', 'field_name')
	list_display_links = ('id', 'field_name')
	ordering = ('id',)

