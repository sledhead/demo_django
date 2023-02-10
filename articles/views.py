from django.shortcuts import render
from .models import Article

# Create your views here.
def article_detail_view(request, id=None):

    article_obj = None
    if id is not None:
        #get database record

        article_obj = Article.objects.get(id=id)

    context = {
        "single_object": article_obj,
    }

    print(f'Here is the object: {article_obj.title}')

    return render(request=request, template_name="articles/details.html", context=context)



def article_all_view(request):

    all_records = Article.objects.all()
    
    context = {
        "single_object": all_records,
    }

    

    return render(request=request, template_name="articles/all_records.html", context=context)


def article_search_view(request):

    query_dict = dict(request.GET)
    query_id = query_dict.get('query')
    request_rec = None
    if query_id is not None:
        request_rec = Article.objects.get(query_id)

    
    context = {
        'object':request_rec
    }

    return render(request, "articles/search.html", context=context)
