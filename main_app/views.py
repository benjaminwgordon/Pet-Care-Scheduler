from django.shortcuts import render, redirect
from .models import Pet, Feeding
from .forms import Pet_Form

# Create your views here.
def home(request):
    return render(request, 'home.html')

def pets_index(request):
    if request.method == 'POST':
        #handle create
        pet_form = Pet_Form(request.POST)
        if pet_form.is_valid():
            pet_form.save()
            return redirect('pets_index')
    else:
        #handle index
        pets = Pet.objects.all()
        context = {
            'pets': pets,
            'pet_form': Pet_Form()
        }
        return render(request, 'pets/index.html', context)

def pets_detail(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    context = {
        'pet': pet
    }
    return render(request, 'pets/detail.html', context)

def pets_edit(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    if request.method == 'POST':
        #handle update
        pet_form = Pet_Form(request.POST, instance=pet)
        if pet_form.is_valid():
            pet_form.save()
            return redirect('pets_detail', pet_id = pet_id)
    else:
        #handle edit
        pet_form = Pet_Form(instance=pet)
        context = {
            'pet': pet,
            'pet_form': pet_form
        }
        return render(request, 'pets/edit.html', context)

def pets_delete(request, pet_id):
    Pet.objects.get(id=pet_id).delete()
    return redirect('pets_index')