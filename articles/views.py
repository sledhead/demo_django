from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render
from django.http import Http404
from .forms import ArticleForm
from .models import Article

# Create your views here.
def article_detail_view(request, slug=None):

    article_obj = None
    if slug is not None:
        #get database record
        try:
            article_obj = Article.objects.get(slug=slug)

        except Article.DoesNotExist:
            raise Http404
        
        except Article.MultipleObjectsReturned:
            article_obj = Article.objects.filter(slug=slug).first()
        
        except:
            raise Http404

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

    query_id = request.GET.get('query')
    #query_id = query_dict.get('query')

    

    #request_rec = None
    #print(f"Here is the query: {query_id}")
    qs = Article.objects.all()
    #print(f'Here is the Number: {query_id}')
    #print(f'Object type: {type(query_id)} ')
    if query_id is not None:
        #request_rec = Article.objects.get(id=query_id)
        lookups = Q(title__icontains=query_id) | Q(content__icontains=query_id)
        qs = Article.objects.filter(lookups)

    
    context = {
        'object_list':qs
    }

    return render(request, "articles/search.html", context=context)

@login_required
def article_create_view(request):

    #print(request.POST)
    form = ArticleForm( request.POST or None)
    context = {
        "form":form
    }
    
    if( form.is_valid() ):

        article_object = form.save()

        # new_title = form.cleaned_data.get('title')
        # new_content = form.cleaned_data.get('content')

        # print(f"Here is the data the user sent in: {new_title} - {new_content}")

        # article_object = Article.objects.create(title=new_title, content=new_content)

        context['object'] = article_object
    
        context['created'] = True

    
    return render(request=request, template_name="articles/create.html", context=context)

#ctrl K then ctrl C  comment
#ctrl K then ctrl U uncomment

# @login_required
# def article_create_view(request):

#     #print(request.POST)
#     context = {
#         "form":ArticleForm()
#     }
#     if( request.method == "POST"):
#         #adding new entry
#         form = ArticleForm(request.POST)
#         #show the data did not pass inspection in the form class
#         context['form'] = form
#         if( form.is_valid() ):

            # new_title = form.cleaned_data.get('title')
            # new_content = form.cleaned_data.get('content')

#             print(f"Here is the data the user sent in: {new_title} - {new_content}")

#             article_object = Article.objects.create(title=new_title, content=new_content)

#             context['object'] = article_object
        
#             context['created'] = True

    

    

#     return render(request=request, template_name="articles/create.html", context=context)
 

