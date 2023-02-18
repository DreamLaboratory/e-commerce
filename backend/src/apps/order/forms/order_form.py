from django import forms

from ..models.order import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
        exclude = "order_number"
