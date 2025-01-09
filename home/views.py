from django.shortcuts import render


# home page url (will be a carousel for now)
def home(request):
    return render(request, 'home/carousel.html')


def tests(request):
    return render(request, 'home/tests.html')


def about(request):
    return render(request, 'home/about.html')


def blog(request):
    return render(request, 'home/blog.html')
