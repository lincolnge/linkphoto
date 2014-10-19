from django.shortcuts import render_to_response


def my_homepage_view(request):
    return render_to_response('index.html')
