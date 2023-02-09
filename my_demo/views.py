
import random
from django.http import HttpResponse
from django.template.loader import render_to_string

from articles.models import Article

HTML_STRING = """
<h1>Hello World</h1>
<h2>Montana Big Sky Country</h2>
"""
def home_view(request):

    random_int = random.randint(10, 500010)
    database_rec = Article.objects.get(id=2)

    database_rec_dict = {

        'title': database_rec.title,
        'content': database_rec.content,
        'id': database_rec.id
    }

    #new_database_str = f'<b>Database info:</b> {database_rec.title}, content: {database_rec.content}'
    #new_database_str = '<b>Database info:</b> {title}, content: {content}'.format(**database_rec_dict)

    new_database_str = render_to_string('home-view.html', context = database_rec_dict)
    new_return_str = f'{HTML_STRING} New Number: {random_int}<br>'
    new_return_str += new_database_str
    return HttpResponse(new_return_str)