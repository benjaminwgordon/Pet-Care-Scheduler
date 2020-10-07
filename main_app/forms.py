from django.forms import ModelForm
from .models import Pet, Feeding

class Pet_Form(ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'color', 'species']

class Feeding_Form(ModelForm):
    class Meta:
        model = Feeding
        fields = ['date', 'meal']