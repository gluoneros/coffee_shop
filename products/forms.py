from django import forms
from products.models import Product 

class ProductForm(forms.Form):
    name = forms.CharField(max_length=200, label='Nombre')
    price = forms.DecimalField(max_digits=10, decimal_places=2, label='Precio')
    description = forms.CharField(max_length=300, label='Descripción')
    available = forms.BooleanField(initial=True, label='Disponible')
    photo = forms.ImageField(label='Foto', required=False)
    
    def save(self):
        Product.objects.create(
            name=self.cleaned_data['name'],
            price=self.cleaned_data['price'],
            description=self.cleaned_dataa['description'],
            available=self.cleaned_data['available'],
            photo=self.cleaned_data['photo']
        )