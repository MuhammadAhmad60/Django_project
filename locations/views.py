from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Country, Province, City, Location

# Home page with form and list

def home(request):
    countries = Country.objects.all()
    saved_locations = Location.objects.select_related('country', 'province', 'city').all()
    return render(request, 'home.html', {'countries': countries, 'saved_locations': saved_locations})

def location_list(request):
    locations = Location.objects.select_related('country', 'province', 'city').all()
    return render(request, 'location_list.html', {'locations': locations})


# AJAX: Get provinces by country ID
def get_provinces(request):
    country_id = request.GET.get('country_id')
    provinces = list(Province.objects.filter(country_id=country_id).values('id', 'name'))
    return JsonResponse({'provinces': provinces})

# AJAX: Get cities by province ID
def get_cities(request):
    province_id = request.GET.get('province_id')
    cities = list(City.objects.filter(province_id=province_id).values('id', 'name'))
    return JsonResponse({'cities': cities})

# AJAX: Save location without redirect
def save_location(request):
    if request.method == 'POST':
        country_id = request.POST.get('country')
        province_id = request.POST.get('province')
        city_id = request.POST.get('city')
        Location.objects.create(
            country_id=country_id,
            province_id=province_id,
            city_id=city_id,
        )
        return JsonResponse({'success': True})

# AJAX: Delete location
#@csrf_exempt # type: ignore
def delete_location(request, pk):
    if request.method == "POST":
        try:
            location = Location.objects.get(pk=pk)
            location.delete()
            return JsonResponse({'success': True})
        except Location.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Location not found'})
    return JsonResponse({'success': False, 'error': 'Invalid request'})

# AJAX: Get location details for edit
def get_location(request, pk):
    location = get_object_or_404(Location, pk=pk)
    return JsonResponse({
        'id': location.id,
        'country': location.country.id,
        'province': location.province.id,
        'city': location.city.id,
    })

# AJAX: Update location
def update_location(request, pk):
    location = get_object_or_404(Location, pk=pk)
    if request.method == 'POST':
        location.country_id = request.POST.get('country')
        location.province_id = request.POST.get('province')
        location.city_id = request.POST.get('city')
        location.save()
        return JsonResponse({'success': True})

def edit_location(request, pk):
    if request.method == 'POST':
        try:
            location = Location.objects.get(pk=pk)
            country_id = request.POST.get('country')
            province_id = request.POST.get('province')
            city_id = request.POST.get('city')

            location.country_id = country_id
            location.province_id = province_id
            location.city_id = city_id
            location.save()
            return JsonResponse({'success': True})
        except Location.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Location not found'})
    return JsonResponse({'success': False, 'error': 'Invalid request'})
