from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required

@login_required(login_url='aurora:login')
def user_status(request):
    context = {
        "page_title": "이용자 현황",
    }
    return render(request, 'aurora/apps/data/user_status.html', context)

