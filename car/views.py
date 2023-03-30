from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.http import HttpResponse


# не полная информация о товаре
def car_list_view(request):
    car_object = models.Cars.objects.all()
    return render(request, 'car_list.html', {'car_object': car_object})


#полная инфа об id
def car_detail_view(request, id):
    car_detail = get_object_or_404(models.Cars, id=id)
    return render(request, 'car_detail.html', {'car_detail': car_detail})


#добавление в базу данных
def create_car_view(request):
    method = request.method
    if method == 'POST':
        form = forms.CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("<h2>Машина успешно добавлена</h2>")
    else:
        form = forms.CarForm()
    return render(request, 'create_car.html', {'form': form})


#изменение базы данных
def update_object_view(request, id):
    car_object = get_object_or_404(models.Cars, id=id)
    if request.method == 'POST':
        form = forms.CarForm(instance=car_object, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h2>Данные успешно обновлены</h2>')
    else:
        form = forms.CarForm(instance=car_object)
    return render(request, 'update_car.html', {
                                                'form': form,
                                                'object': car_object
                                               })


#Удаление из базы данных
def delete_object_view(request, id):
    car_object = get_object_or_404(models.Cars, id=id)
    car_object.delete()
    return HttpResponse('<h2>Успешно удален из базы данных</h2>')