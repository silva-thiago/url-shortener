from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required()
def signin(request):
    return render(request, 'dashboard.html', {})
