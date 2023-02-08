
from django.http import HttpResponse

HTML_STRING = """
<h1>Hello World</h1>
<h2>Montana</h2>
"""
def home_view(request):
    return HttpResponse(HTML_STRING)