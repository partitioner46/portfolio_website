from django.shortcuts import render
import requests as rq
import os


def get_repos():
    repo_url = "https://api.github.com/users/partitioner46/repos"
    raw_repos = rq.get(url=repo_url).json()
    cleaned_repos = [{"name": repo['name'], "desc": repo['description'],
                      "html_url": repo['html_url']} for repo in raw_repos]
    print(cleaned_repos)
    return cleaned_repos


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
    """
    TODO add the repo languages
    https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#list-repository-languages
    """
    repos = get_repos()
    # access_token = os.getenv('GITHUB_API_TOKEN')
    context = {'data': repos}
    return render(request, 'home/projects.html', context=context)
