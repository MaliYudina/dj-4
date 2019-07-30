from django.shortcuts import render, HttpResponse
from .models import Article


def one_article(request, name=None):
    articles = Article.objects.filter(name=name)
    context = {'articles': articles}

    # names_list = ['Канцелярия%20для%20школы:%20список%20покупок', '2b']
    # if name not in names_list:
    #      return render(request, 'error.html', context)

    return render(request, 'articles.html', context)



def all_articles(request):
    articles = Article.objects.order_by('created')
    context = {'articles': articles}
    return render(request, 'articles.html', context)
