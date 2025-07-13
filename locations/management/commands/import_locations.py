import json
from django.core.management.base import BaseCommand
from locations.models import Country, Province, City


class Command(BaseCommand):
    help = 'Import countries, provinces, and cities'

    def handle(self, *args, **kwargs):
        # Load countries
        with open('countries.json', encoding='utf-8') as f:
            countries = json.load(f)

        country_map = {}
        for c in countries:
            country_obj, _ = Country.objects.get_or_create(name=c['name'])
            country_map[c['id']] = country_obj

        self.stdout.write(self.style.SUCCESS(f"✔ Imported {len(country_map)} countries"))

        # Load provinces (states)
        with open('states.json', encoding='utf-8') as f:
            states = json.load(f)

        state_map = {}
        for s in states:
            country = country_map.get(s['country_id'])
            if country:
                province_obj, _ = Province.objects.get_or_create(name=s['name'], country=country)
                state_map[s['id']] = province_obj

        self.stdout.write(self.style.SUCCESS(f"✔ Imported {len(state_map)} provinces"))

        # Load cities
        with open('cities.json', encoding='utf-8') as f:
            cities = json.load(f)

        count = 0
        for city in cities:
            province = state_map.get(city['state_id'])
            if province:
                City.objects.get_or_create(name=city['name'], province=province)
                count += 1

        self.stdout.write(self.style.SUCCESS(f"✔ Imported {count} cities"))

