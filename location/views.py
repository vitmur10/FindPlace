from django.http import Http404
from django.shortcuts import render
from .models import Location, Region


# Create your views here.
def home(request):
    region = Region.objects.all()
    type_choices = Location.TYPE_CHOICES
    return render(request, 'base.html', {'region_list': region,
                                         'type_choices': type_choices})


def region_detail(request, region_id):
    try:
        region = Region.objects.get(id=region_id)
    except:
        raise Http404('Ми ще не добавили цей регіон(')
    loc = Location.objects.filter(region_id=region_id)

    return render(request, 'location/deteil_region.html', {'region': region,
                                                           'location': loc})


def location_detail(request, name_location):
    try:
        location = Location.objects.get(name_location=name_location)
    except:
        raise Http404('Ми ще не добавили цей регіон(')

    return render(request, 'location/location.html', {'location': location})


def type_loc(request, type_name):
    try:
        location = Location.objects.filter(type=type_name)
    except:
        raise Http404('Сталася помилка(')
    return render(request, 'location/type_loc.html', {'location': location})