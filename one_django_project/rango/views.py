# Rango views
from django.shortcuts import render

from rango.models import Category, Page

def index(request):
    '''
    1. Query the database for list of all categories currently stored
    2. Order the categories in descending order by number of likes
    3. Retrieve only top 5 -- OR all if less than 5
    4. pass the list in the context_dict as template context that will be passed
    to the template engine
    '''

    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['pages'] = page_list
    return render(request, 'rango/index.html', context=context_dict)

def show_category(request, category_name_slug):
    '''
    Details page for a given category
    '''
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['category'] = category
        context_dict['pages'] = pages
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
    return render(request, 'rango/category.html', context=context_dict)

def about(request):
    '''
    Rango About page
    '''
    context_dict = {'authorname': 'Sameer Jain'}
    return render(request, 'rango/about.html', context=context_dict)
