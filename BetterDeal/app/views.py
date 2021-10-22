from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from .models import Product
from django.db.models import Q
from .forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

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
    model = Product
    template_name = 'app/searchresults.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(
            Q(product_name__icontains=query) 
        )
        return object_list


def register_request(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('search')
    else:
        form = UserCreationForm()
    return render(request, 'app/register.html', {'form': form})