from django.urls import path

from . import views

app_name = "home"
urlpatterns = [
    path("", views.home, name="home"),
    path("tests", views.tests, name="tests"),
    path("about", views.about, name="about"),
    path("blog", views.blog, name="blog"),
    path("tech", views.tech, name="tech"),
    path("projects", views.projects, name="projects"),
]
