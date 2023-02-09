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
