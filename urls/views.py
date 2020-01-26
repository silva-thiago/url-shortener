from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

import urllib

from .models import Url


def urls_list(request):
    return render(request, 'urls.html', {'objects': Url.objects.all()})


@csrf_protect
def shortener_url(request):
    if request.method == 'POST':
        url_input = request.POST.get('urlInput', '')

        if url_input:
            url_output = urllib.request.urlopen("http://tinyurl.com/api-create.php?url=%s" % urllib.parse.quote(url_input)).read()
            Url.objects.create(urlInput=url_input, urlOutput=url_output.decode('utf8'))

    return render(request, 'dashboard.html', {'urlOutput': url_output.decode('utf8')})
