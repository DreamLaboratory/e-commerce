from django import forms

from ..models.order import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
        exclude = ("order_number", "user", "ip", "status", "total_price", "cart_items")

    # generate order number
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"
