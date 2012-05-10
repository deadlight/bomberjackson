from django import template
from django.template import RequestContext, loader
from django.template.loader import render_to_string

from reviews.models import Review
register = template.Library()

@register.simple_tag
def get_reviews(number_of_reviews):
    reviews_list = Review.objects.all().order_by('-date')[:number_of_reviews]
    return render_to_string('reviews/_get_reviews.html', { 'reviews_list': reviews_list })
