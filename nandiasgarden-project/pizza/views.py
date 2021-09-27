from django.shortcuts import render
from .forms import PizzaForm

# Create your views here.

def home(request):
    return render(request, 'pizza/home.html')


def order(request):
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            note = f"Thanks for ordering! Your {filled_form.cleaned_data['size']} {filled_form.cleaned_data['topping1']} and {filled_form.cleaned_data['topping2']} pizza in on its way!"
            new_form = PizzaForm()
            return render(request, 'pizza/order.html', {
                'form': new_form,
                'note': note,
            })

    else:
        form = PizzaForm()
        return render(request, 'pizza/order.html', {
            'form': form,
        })
