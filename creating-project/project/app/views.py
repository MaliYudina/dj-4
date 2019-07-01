from django.shortcuts import render

from .models import Route


def get_stations(request):
    routes = Route.objects.all()

    context = {
        'routes': routes,
        'stations': ''
    }
    route = request.GET.get('route', None)

    if route:
        stations = routes.get(name=route).stations.all()
        context['stations'] = stations

        # long = x, lat = y

        stations_long = stations.order_by('longitude')
        stations_lat = stations.order_by('latitude')

        first_long = stations_long.first().longitude
        first_lat = stations_lat.first().latitude

        last_long = stations_long.last().longitude
        last_lat = stations_lat.last().latitude

        x = (first_long + last_long) / 2
        y = (first_lat + last_lat) / 2

        context['center'] = {'x': x, 'y': y}
    else:
        default_y = '55.7515'
        default_x = '37.621'
        context['center'] = {'x': default_x, 'y': default_y}

    return render(request, 'stations.html', context)

