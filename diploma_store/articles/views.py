from django.shortcuts import render
from .models import Article


def one_article(request, name=None):
    articles = Article.objects.filter(name=name)

    names_list = []

    for article in articles:
        names_list.append(str(article))

    context = {'articles': articles}


    if name in names_list:
        return render(request, 'articles.html', context)
    else:
        return render(request, 'error.html', context)



def all_articles(request):
    articles = Article.objects.order_by('created')
    context = {'articles': articles}
    return render(request, 'articles.html', context)
