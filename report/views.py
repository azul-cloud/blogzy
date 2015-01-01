from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render

from .models import PostView
from blog.models import Post

# Create your views here.
@staff_member_required
def admin_home(request):
	'''
	this is the home dashboard for admins, which currently just means staff.
	Other users that try to access this page will be redirected to login.
	'''
	views = PostView.objects.all()

	return render(request, 'reportcontent/admin_home.html', 
		{'views':views})