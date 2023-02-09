
import random
from django.http import HttpResponse

HTML_STRING = """
<h1>Hello World</h1>
<h2>Montana Big Sky Country</h2>
"""
def home_view(request):

    random_int = random.randint(10, 500010)
    new_return_str = f'{HTML_STRING} New Number: {random_int}'
    return HttpResponse(new_return_str)