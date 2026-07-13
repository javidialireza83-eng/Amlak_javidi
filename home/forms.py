
from django import forms
from .models import Home

class HomeForms(forms.ModelForm):
    class Meta:
        model = Home
        # fields = '__all__'
        exclude = ['owner']
        images = forms.ImageField(
            widget=forms.ClearableFileInput(attrs={'multiple': True},required=False),
            )
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'مثال: آپارتمان ۳خوابه'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'deposit': forms.NumberInput(attrs={'class': 'form-control'}),
            'area': forms.NumberInput(attrs={'class': 'form-control'}),
            'rooms': forms.NumberInput(attrs={'class': 'form-control'}),
            'floor': forms.NumberInput(attrs={'class': 'form-control'}),
            'year_built': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'owner_name': forms.TextInput(attrs={'class': 'form-control'}),
            'owner_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'property_type': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'hammam': forms.NumberInput(attrs={'class': 'form-control'}),
            'rent': forms.NumberInput(attrs={'class': 'form-control'}),
            # 'hammam': forms.Select(attrs={'class': 'form-control'}),
            # برای image نیازی به کلاس نیست چون مخفی شده است
        }