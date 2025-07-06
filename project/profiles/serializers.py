from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'surname', 'name', 'middlename', 'birthday', 'phone', 'email', 'logo')

	user = serializers.OneToOneField(User, on_delete=models.CASCADE, null=True, default=None, blank=True)
	username = serializers.CharField("Username", max_length=300, blank=True)
#####################################################
	surname = serializers.CharField(verbose_name="Фамилия", max_length=50, blank=True)
	name = serializers.CharField(verbose_name="Имя", max_length=50, blank=True)
	middlename = serializers.CharField(verbose_name='Отчества', max_length=50, blank=True)
	birthday = serializers.DateField(verbose_name="День рождение", blank=True, null=True, default=None)
	phone = serializers(verbose_name="Телефон", blank=True, help_text='Контактный номер телефона')
	email = serializers.EmailField(verbose_name="Email", max_length=70, blank=True, unique=True)
	logo = serializers.ImageField(verbose_name='Аватарка', blank=True, null=True, upload_to = make_upload_path)
	registration_date = serializers.DateField(verbose_name="Registration date", default=datetime.date.today)