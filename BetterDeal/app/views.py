from django.shortcuts import render

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
