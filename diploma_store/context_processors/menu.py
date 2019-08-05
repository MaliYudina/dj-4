from products.models import Section, Category


def menu_items(request):
    context = {'menu': Section.objects.all(),
               # 'categories_pr': Category.objects.all().prefetch_related('section'),
               }

    return context
