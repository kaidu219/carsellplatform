from .models import Car


def get_search_filters():
    model_search = Car.objects.order_by('model').values_list('model', flat=True).distinct
    city_search = Car.objects.order_by('city').values_list('city', flat=True).distinct   
    year_search = Car.objects.order_by('-year').values_list('year', flat=True).distinct   
    bs_search = Car.objects.order_by('body_style').values_list('body_style', flat=True).distinct
    transmission_search = Car.objects.order_by('transmission').values_list('transmission', flat=True).distinct
    price_search = Car.objects.order_by('price').values_list('price', flat=True)

    context = {
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'bs_search': bs_search,
        'transmission_search': transmission_search,
        'price_search':price_search,
    }

    return context
