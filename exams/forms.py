from django.forms import ModelForm
from .models import order

class OrderForm(ModelForm):
    class Meta:
        model = order
        fields = ['name', 'address', 'city', 'state', 'zip_code', 'phone']
