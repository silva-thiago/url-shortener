from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

import urllib

from .models import Url


def urls_list(request):
    return render(request, 'urls.html', {'objects': Url.objects.all()})


@csrf_protect
def shortener_url(request):
    if request.method == 'POST':
        # print(request.POST.get('urlInput', ''))
        urlinput = request.POST.get('urlInput', '')

        if urlinput:
            urlOutput = urllib.request.urlopen("http://tinyurl.com/api-create.php?url=%s" % urllib.parse.quote(urlinput)).read()
            # print(urlOutput)
            Url.objects.create(urlInput=urlinput, urlOutput=urlOutput.decode('utf8'))

    return render(request, 'dashboard.html', {'urlOutput': urlOutput.decode('utf8')})
