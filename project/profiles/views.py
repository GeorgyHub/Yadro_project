from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/sing_in/')
def my_profile(request):
	return render(request, 'profiles/my_page.html')