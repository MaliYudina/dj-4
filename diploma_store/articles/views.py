from django.shortcuts import render
from .models import Article


def one_article(request, name=None):
    if name:
        articles = Article.objects.filter(name=name)
    context = {'articles': articles}
    return render(request, 'articles.html', context)


def all_articles(request):
    articles = Article.objects.order_by('created')
    context = {'articles': articles}
    return render(request, 'articles.html', context)
