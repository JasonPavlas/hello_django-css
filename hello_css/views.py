from django.shortcuts import render

def css(request):
    return render(request, 'hello_css/css.html', {'title': 'CSS'})

def noCss(request):
    return render(request, 'hello_css/noCss.html', {'title': 'No CSS'})