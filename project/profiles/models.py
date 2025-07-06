import os
import datetime
from django.conf import settings
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField

from pytils import translit
#from multiselectfield import MultiSelectField

# Create your models here.
def make_upload_path(instance, filename):
	names = filename.split('.')
	new_filename = ''
	for name in names:
		if name != names[0]:
			new_filename += '.'
		new_filename += translit.slugify(name)

	path = 'profileimgs/%s' % ( new_filename)

	return path

class Profile(models.Model):

	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, default=None, blank=True)
	username = models.CharField("Username", max_length=300, blank=True)
#####################################################
	surname = models.CharField(verbose_name="Фамилия", max_length=50, blank=True)
	name = models.CharField(verbose_name="Имя", max_length=50, blank=True)
	middlename = models.CharField(verbose_name='Отчества', max_length=50, blank=True)
	birthday = models.DateField(verbose_name="День рождение", blank=True, null=True, default=None)
	phone = PhoneNumberField(verbose_name="Телефон", blank=True, help_text='Контактный номер телефона')
	email = models.EmailField(verbose_name="Email", max_length=70, blank=True, unique=True)
	logo = models.ImageField(verbose_name='Аватарка', blank=True, null=True, upload_to = make_upload_path)
	registration_date = models.DateField(verbose_name="Registration date", default=datetime.date.today)


	class Meta:
		verbose_name = 'Пользователь'
		verbose_name_plural = 'Пользователи'
		ordering = ['surname', 'name', 'middlename']

	def __str__(self):
		self.username

	def get_full_name(self):
		if self.surname:
			if self.middlename:
				return self.surname + ' ' + self.name + ' ' + self.middlename
			return self.surname + ' ' + self.name
		return self.name

	def get_name(self):
		if self.surname:
			if self.middlename:
				return self.surname + ' ' + self.name[0] + '.' + self.middlename[0] + '.'
			return self.surname + ' ' + self.name[0] + '.'
		return self.name

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.username = instance.username
	instance.profile.save()

@receiver(post_delete, sender = Profile)
def profile_post_delete_handler(sender, **kwargs):
	profile = kwargs['instance']

	if profile.logo:
		if os.path.isfile(profile.logo.path):
			os.remove(profile.logo.path)


@receiver(pre_save, sender = Profile)
def profile_pre_save_handler(sender, **kwargs):
	profile = kwargs['instance']

	try:
		old_file = Profile.objects.get(pk=profile.pk).logo

		if old_file:
			new_file = profile.logo
			if not old_file==new_file:
				if os.path.isfile(old_file.path):
					os.remove(old_file.path)

	except Profile.DoesNotExist:
		pass