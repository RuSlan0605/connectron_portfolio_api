from django.shortcuts import render
from .models import *


def index(request):
	return render(
		request, 'index.html',
		{
			'projects_count': Project.objects.count(),
			'staff': Staff.objects.count(),
			'fields': Field.objects.count(),

		}
	)

