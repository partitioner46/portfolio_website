from django.shortcuts import render


# home page url (will be a carousel for now)
def home(request):
    return render(request, 'home/home.html')


def tests(request):
    return render(request, 'home/tests.html')


def about(request):
    return render(request, 'home/about.html')


def blog(request):
    return render(request, 'home/blog.html')


def tech(request):
    return render(request, 'home/tech.html')


def projects(request):
    return render(request, 'home/projects.html')
