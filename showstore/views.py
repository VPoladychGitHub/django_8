from collections import OrderedDict

import coreapi
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page


# @cache_page(10)
# def listing(request):
#     auth = coreapi.auth.BasicAuthentication(
#         username='admin',
#         password='admin'
#     )
#     client = coreapi.Client(auth=auth)
#     schema = client.get('http://localhost:8000/book/')
#     paginator = Paginator(client, 30)  # Show 30 contacts per page.
#
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'sale/city_list.html', {'page_obj': page_obj})


#@cache_page(10)
def book_list(request):
    auth = coreapi.auth.BasicAuthentication(
        username='admin',
        password='admin'
    )
    client = coreapi.Client(auth=auth)
    schema = client.get('http://localhost:8000/book/')
    # users = client.action(schema, ['users', 'list'])
    # users = client.action(schema)
    print('----------------pld----------------------')
    od = OrderedDict(schema)
    r = od['results']
    # print(schema)
    result_list: list = list()
    for key in r:
        author = key['author']

        print(key['title'])
        print(key['summary'])
        print(key['isbn'])
        print(key['author'])
        result_list.append((key['title'], key['author'], key['summary'], key['isbn']))

        print('                                  .......')

    print('--------------------------------------')
    paginator = Paginator(result_list, 30)  # Show 30 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "showstore/book_list.html", {'page_obj': page_obj})

