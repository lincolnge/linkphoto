# Create your views here.
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.shortcuts import render_to_response

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext

from django.views.decorators.csrf import csrf_exempt


@login_required
def profile(request):
    # return render_to_response('/accounts/profile.html',
    # context_instance=RequestContext(request))
    return HttpResponseRedirect('/')


# @login_required
def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/")


@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    return render_to_response("registration/register.html", {
        'form': form,
    })
