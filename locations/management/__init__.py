from django.core.management.base import BaseCommand
from locations.models import Country, Province, City

class Command(BaseCommand):
    help = 'Import example countries, provinces, and cities'

    def handle(self, *args, **kwargs):
        pakistan = Country.objects.create(name='Pakistan')
        punjab = Province.objects.create(name='Punjab', country=pakistan)
        sindh = Province.objects.create(name='Sindh', country=pakistan)

        City.objects.create(name='Lahore', province=punjab)
        City.objects.create(name='Multan', province=punjab)
        City.objects.create(name='Karachi', province=sindh)

        self.stdout.write(self.style.SUCCESS('Sample locations imported successfully!'))
