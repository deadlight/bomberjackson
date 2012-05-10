from django.template import RequestContext, loader
from django.http import HttpResponse
from events.models import Event
from django.shortcuts import render_to_response, get_object_or_404

def index(request, page_name):
    events_list = Event.objects.all().order_by('-date')
    t = loader.get_template('events/index.html')
    c = RequestContext(request, {
        'events_list': events_list,
        'page_name': page_name,
    })
    return HttpResponse(t.render(c))
