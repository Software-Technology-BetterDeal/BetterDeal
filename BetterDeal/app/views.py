from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import DummyDatabase 

posts = [
    {
        'author': 'BetterDeal',
        'title': 'BetterDeal Post 1',
        'content': 'First post content',
        'date_posted': 'October 18, 2021'
    },
    {
        'author': 'BetterDeal2',
        'title': 'BetterDeal Post 2',
        'content': 'Second post content',
        'date_posted': 'October 17, 2021'
    }
]


# Create your views here.
def home(request):
    # with context we pass the data to the template
    context = {
        'posts': posts
    }
    return render(request, 'app/home.html', context)


def about(request):
    return render(request, 'app/about.html', {'title': 'About'})


class Search(TemplateView):
    template_name = 'app/search.html'

class SearchResultsView(ListView):
    model = DummyDatabase
    template_name = 'app/searchresults.html'