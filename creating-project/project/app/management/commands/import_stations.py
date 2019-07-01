import csv

from app.models import Route, Station
from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):

    def handle(self, *args, **options):

        with open('moscow_bus_stations.csv', 'r', encoding='cp1251') as f:
            reader = csv.reader(f, delimiter=';')
            next(reader)

            for row in reader:
                station = Station(id=int(row[0]),
                                  name=str(row[1]),
                                  longitude=float(row[2]),
                                  latitude=float(row[3]),
                                  )
                station.save()

                routes = [route for route in row[7].split('; ')]
                for route in routes:
                    obj = Route.objects.filter(name=route).first()
                    if obj:
                        station.routes.add(obj)
                    else:
                        route = Route(name=route)
                        route.save()
                        station.routes.add(route)
