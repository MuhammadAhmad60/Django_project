import csv
from django.core.management.base import BaseCommand
from locations.models import Country, Province, City

class Command(BaseCommand):
    help = 'Import countries, provinces, and cities from CSV'

    def handle(self, *args, **kwargs):
        with open('google_maps/locations/worldcities.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                country_name = row['country']
                province_name = row['admin_name']
                city_name = row['city']

                # Create or get Country
                country, _ = Country.objects.get_or_create(name=country_name)

                # Create or get Province
                province, _ = Province.objects.get_or_create(name=province_name, country=country)

                # Create City
                City.objects.get_or_create(name=city_name, province=province)

            self.stdout.write(self.style.SUCCESS('Successfully imported location data.'))
