from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import ArticleForm
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

    query_dict = request.GET
    query_id = query_dict.get('query')

    try:
        query_id = int( query_dict.get('query') )

    except:
        query_id = None

    request_rec = None
    #print(f'Here is the Number: {query_id}')
    #print(f'Object type: {type(query_id)} ')
    if query_id is not None:
        request_rec = Article.objects.get(id=query_id)

    
    context = {
        'object':request_rec
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
 

