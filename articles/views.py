from django.shortcuts import render
from .models import Article

# Create your views here.
def article_detail_view(request, id=None):

    article_obj = None
    if id is not None:
        #get database record

        article_obj = Article.objects.get(id=id)

    context = {
        "object": article_obj
    }

    return render(request=request, template_name="/articles/details.html", context=context)
