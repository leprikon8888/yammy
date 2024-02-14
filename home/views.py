from django.shortcuts import render
from django.views.generic import TemplateView
from .models import DishCategory, Event, Gallery, Chef, Contact
from .forms import ReservationForm


class MainPageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = DishCategory.objects.filter(is_visible=True)
        events = Event.objects.filter(is_visible=True)
        gallery = Gallery.objects.filter(is_visible=True)
        chef = Chef.objects.filter(is_visible=True)
        contact = Contact.objects.all()
        reservation_form = ReservationForm()

        context['categories'] = categories
        context['events'] = events
        context['gallery'] = gallery
        context['chef'] = chef
        context['contact'] = contact
        context['reservation_form'] = reservation_form
        return context

    def post(self, request, *args, **kwargs):
        reservation_form = ReservationForm(request.POST)
        if reservation_form.is_valid():
            reservation_form.save()
            return render(request, 'index.html', {'reservation_form': reservation_form})
        else:
            return render(request, 'index.html', {'reservation_form': reservation_form})
        # if reservation_form.is_valid():
        #     reservation_form.save()
        #     return render(request, 'index.html', {'reservation_form': reservation_form})
        # else:
        #     print(reservation_form.errors)
        #     return render(request, 'index.html', {'reservation_form': reservation_form})

# def main_page(request):
#     categories = DishCategory.objects.filter(is_visible=True)
#     events = Event.objects.filter(is_visible=True)
#     gallery = Gallery.objects.filter(is_visible=True)
#     chef = Chef.objects.filter(is_visible=True)
#     contact = Contact.objects.all()
#     context = {
#         'categories': categories,
#         'events': events,
#         'gallery': gallery,
#         'chef': chef,
#         'contact': contact
#     }
#     return render(request, 'index.html', context=context)
