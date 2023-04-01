from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.http import HttpResponse
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView


# не полная информация о товаре
class CarListView(ListView):
    template_name = 'car_list.html'
    queryset = models.Cars.objects.all()

    def get_queryset(self):
        return models.Cars.objects.all()
# def car_list_view(request):
#     car_object = models.Cars.objects.all()
#     return render(request, 'car_list.html', {'car_object': car_object})


#полная инфа об id
class CarDetailView(DetailView):
    template_name = 'car_detail.html'

    def get_object(self, **kwargs):
        car_id = self.kwargs.get('id')
        return get_object_or_404(models.Cars, id=car_id)

# def car_detail_view(request, id):
#     car_detail = get_object_or_404(models.Cars, id=id)
#     return render(request, 'car_detail.html', {'car_detail': car_detail})


#добавление в базу данных
class CreateCarView(CreateView):
    template_name = 'create_car.html'
    form_class = forms.CarForm
    queryset = models.Cars.objects.all()
    success_url = '/car_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateCarView, self).form_valid(form=form)

# def create_car_view(request):
#     method = request.method
#     if method == 'POST':
#         form = forms.CarForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("<h2>Машина успешно добавлена</h2>")
#     else:
#         form = forms.CarForm()
#     return render(request, 'create_car.html', {'form': form})


#изменение базы данных
class CarUpdateView(UpdateView):
    template_name = 'update_car.html'
    form_class = forms.CarForm
    success_url = '/car_list/'

    def get_object(self, **kwargs):
        car_id = self.kwargs.get('id')
        return get_object_or_404(models.Cars, id=car_id)

    def form_valid(self, form):
        return super(CarUpdateView, self).form_valid(form=form)

# def update_object_view(request, id):
#     car_object = get_object_or_404(models.Cars, id=id)
#     if request.method == 'POST':
#         form = forms.CarForm(instance=car_object, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h2>Данные успешно обновлены</h2>')
#     else:
#         form = forms.CarForm(instance=car_object)
#     return render(request, 'update_car.html', {
#                                                 'form': form,
#                                                 'object': car_object
#                                                })


#Удаление из базы данных

class CarDeleteView(DeleteView):
    template_name = 'confirm_delete.html'
    success_url = '/car_list/'

    def get_object(self, **kwargs):
        car_id = self.kwargs.get('id')
        return get_object_or_404(models.Cars, id=car_id)

# def delete_object_view(request, id):
#     car_object = get_object_or_404(models.Cars, id=id)
#     car_object.delete()
#     return HttpResponse('<h2>Успешно удален из базы данных</h2>')


class CarCommentView(CreateView):
    template_name = 'car_comment.html'
    form_class = forms.CarComment
    queryset = models.CommentCar.objects.all()
    success_url = '/car_list/'

    def get_object(self, **kwargs):
        car_id = self.kwargs.get('id')
        return get_object_or_404(models.CommentCar, id=car_id)

    def form_valid(self, form):
        print(form.clean)
        return super(CarCommentView, self).form_valid(form=form)