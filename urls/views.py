from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

import urllib

from .models import Url


def urls_list(request):
    return render(request, 'urls.html', {'objects': Url.objects.all().filter(user_id=request.session['user_id'])})


@csrf_protect
def shortener_url(request):
    if request.method == 'POST':
        url_in = request.POST.get('urlInput', '')

        if url_in:
            url_out = urllib.request.urlopen("http://tinyurl.com/api-create.php?url=%s" % urllib.parse.quote(url_in)).read()
            Url.objects.create(url_input=url_in, url_output=url_out.decode('utf8'), user_id=request.session['user_id'])

            return render(request, 'dashboard.html', {'urlOutput': url_out.decode('utf8')})
