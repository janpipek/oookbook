from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    users = User.objects.all().order_by('username')
    context = { 'users' : users}
    return render(request, 'users/index.html', context)

@login_required
def show(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    context = {'user' : user}
    return render(request, 'users/show.html', context)