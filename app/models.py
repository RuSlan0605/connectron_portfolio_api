# mporting modules
from django.db.models import *


'''--------------------------------------------------'''


# project DB model
class Project(Model):
	project_title = CharField(
		'Project Title', max_length=512
	)
	project_img = ImageField(
		'Project Image', upload_to='uploads/projects/'
	)
	github_link = CharField(
		'GitHub Link', max_length=2048, unique=True
	)
	description = TextField(
		'Description'
	)
	project_slug = SlugField(
		'Project Slug'
	)

	def __str__(self):
		return self.project_title

	class Meta:
		verbose_name = 'Project'
		verbose_name_plural = 'Projects'


# staff DB model
class Staff(Model):
	first_name = CharField(
		'First Name', max_length=512
	)
	last_name = CharField(
		'Last Name', max_length=512
	)
	field = ForeignKey(
		'Field', on_delete=CASCADE
	)
	info = TextField(
		'Information'
	)
	birth_date = DateField(
		'Birth Date'
	)
	phone = CharField(
		'Mobile Phone', max_length=512, unique=True
	)

	email = EmailField(
		'E-mail'
	)
	github_link = CharField(
		'GitHub Link', max_length=2048, unique=True, default='https://github.com/',
		blank=True, null=True
	)
	telegram = CharField(
		'Telegram Link', max_length=2048, unique=True, default='https://t.me/',
		blank=True, null=True
	)
	instagram = CharField(
		'Instagram Link', max_length=2048, unique=True, default='https://instagram.com/',
		blank=True, null=True
	)

	portfolio = CharField(
		'Portfolio Link', max_length=2048, unique=True, default='https://',
		blank=True, null=True
	)

	def __str__(self):
		return f'{self.first_name} {self.last_name}'

	class Meta:
		verbose_name = 'Worker'
		verbose_name_plural = 'Staff'


# field DB model
class Field(Model):
	field_name = CharField(
		'Field Name', max_length=128, unique=True
	)

	def __str__(self):
		return self.field_name

	class Meta:
		verbose_name = 'Field'
		verbose_name_plural = 'Fields'
