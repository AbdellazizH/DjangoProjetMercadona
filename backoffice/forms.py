from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext as _
from backoffice.models import Product, Category, Promotion


class AdminAuthenticationForm(AuthenticationForm):
    error_messages = {
        'invalid_login': _("Please enter a correct %(username)s and password. "
                           "Note that both fields may be case-sensitive."),
        'inactive': _("This account is inactive."),
    }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'image', 'category')


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)


class PromotionForm(forms.ModelForm):
    class Meta:
        model = Promotion
        fields = ('product', 'start_date', 'end_date', 'percentage',)
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'})
        }
