from django.forms import ModelForm
from ..models.order import Order

class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields='__all__'
        exclude=('order_number','ip','user','status','cart_items','total_price')
        

    def __init__(self,*args,**kwargs):
        super(OrderForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'

