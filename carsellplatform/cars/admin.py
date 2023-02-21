from django.contrib import admin
from .models import Car, CarPhoto
from django.utils.html import format_html


class CarImageAdmin(admin.StackedInline):
    model = CarPhoto

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        html_code = '<img src = "{}" width= "40" style ="border-radius: 50px;"/>'
        return format_html(html_code.format(object.car_main_photo.url))
    
    inlines = [CarImageAdmin] #отображение машин
    list_display = ('thumbnail', 'car_title', 'model', 'color', 'year', 'fuel_type', 'is_featured') # отображение столбцов информации
    search_fields = ('car_title', 'model',  'fuel_type', 'body_style') #поиск происходит только по этим столбцам
    list_filter = ('fuel_type', 'color', 'year') #фильты по этим данным
    list_display_links = ('thumbnail', 'car_title', 'color') #столбцы на которые привязаны ссылки для детального просмотра данных
    list_editable = ('is_featured', 'year') # столбцы которые можно менять прямо в списке
    
    class Meta:
        model = Car
        
@admin.register(CarPhoto)
class CarImageAdmin(admin.ModelAdmin):
    pass